#include <iostream>
#define CROW_MAIN
#include "../include/crow_all.h"
#include "../include/schemas.hpp"
#include <pqxx/pqxx>
#include <pthread.h>

int main() {
  crow::SimpleApp app;
  pqxx::connection c("dbname=server user=server");

  CROW_ROUTE(app, "/auth")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([](const crow::request &req) {
        char *id = req.url_params.get("id");
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");
        char *salt = req.url_params.get("salt");

        if (id != nullptr && username != nullptr && password_hash != nullptr &&
            salt != nullptr) {
          // std::cout << "[AUTH] USER ID: " << user_id << "\nPASSWORD: " <<
          // password << std::endl;

          return crow::json::wvalue{{"id", id},
                                    {"username", username},
                                    {"password_hash", password_hash},
                                    {"salt", salt}};
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

  std::cout << "Ay Yo?\n";

  app.port(18080).multithreaded().run();

  return 0;
}
