#define CROW_MAIN
#include "crow_all.h"
#include "database.hpp"
#include "schemas.hpp"
#include <iostream>
#include <pqxx/pqxx>
#include <pthread.h>

int main() {
  crow::SimpleApp app;
  pqxx::connection c("dbname=server user=server");
  pqxx::work conn = pqxx::work(c);

  CROW_ROUTE(app, "/auth")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&conn](const crow::request &req) {
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");

        User user = get_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", "User does not exist."}};
        }
        std::string token = cookie(user, conn);

        if (username != nullptr && password_hash != nullptr) {
          return crow::json::wvalue{{"token", token}};
        }

        return crow::json::wvalue{{"error", "error details would be here"}};
      });

  CROW_ROUTE(app, "/create")
      .methods(crow::HTTPMethod::GET, crow::HTTPMethod::PATCH)([]() {
        return "You technically created an account, but not really cause this "
               "doesnt work yet :)";
      });

  CROW_ROUTE(app, "/login")
      .methods(crow::HTTPMethod::GET, crow::HTTPMethod::PATCH)([]() {
        return "You technically logged into an account, but not really cause "
               "this doesnt work yet :)";
      });

  app.port(18080).multithreaded().run();

  return 0;
}
