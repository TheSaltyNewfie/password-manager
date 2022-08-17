#define CROW_MAIN
#include "database.hpp"
#include "schemas.hpp"
#include <crow_all.h>
#include <iostream>
#include <openssl/err.h>
#include <openssl/ssl.h>
#include <pqxx/pqxx>
#include <pthread.h>
#include <vector>

int main() {
  crow::SimpleApp app;
  pqxx::connection c("dbname=server user=server");

  CROW_ROUTE(app, "/auth")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&c](const crow::request &req) {
        pqxx::work conn = pqxx::work(c);
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");

        User user = get_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", user.m_username}};
        }
        std::string token = cookie(user, conn);

        if (username != nullptr && password_hash != nullptr) {
          return crow::json::wvalue{{"token", token.c_str()}};
        }

        return crow::json::wvalue{{"error", "error details would be here"}};
      });

  CROW_ROUTE(app, "/create")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&c](const crow::request &req) {
        pqxx::work conn = pqxx::work(c);
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");

        User user = create_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", user.m_username.c_str()}};
        }

        return crow::json::wvalue{{"success", "true"}};
      });

  CROW_ROUTE(app, "/delete")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)(
          [](const crow::request &req) { // Add the lambda later on
            char *username = req.url_params.get("username");
            char *password_hash = req.url_params.get("password_hash");

            return crow::json::wvalue{{"Success", "Account deleted"}};

          });

  CROW_ROUTE(app, "/new-password")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&c](const crow::request &req) {
        pqxx::work conn = pqxx::work(c);
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");
        char *token = req.url_params.get("token");
        char *title = req.url_params.get("title");
        char *pass_user = req.url_params.get("pass_user");
        char *pass_pass = req.url_params.get("pass_pass");

        // Find user
        User user = get_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", user.m_username}};
        }

        // Verify auth token
        if (token != cookie(user, conn)) {
          return crow::json::wvalue{{"error", "Unauthorized request."}};
        }

        // Insert password
        Password password = create_password(user, pass_user, pass_pass, title, conn);
        if (password.m_id == "-1") {
          return crow::json::wvalue{{"error", password.m_user_id}};
        }

        return crow::json::wvalue{{"success", "true"}};
      });

  CROW_ROUTE(app, "/get-passwords")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&c](const crow::request &req) {
        pqxx::work conn = pqxx::work(c);
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");
        char *token = req.url_params.get("token");

        // Find user
        User user = get_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", user.m_username}};
        }

        // Verify auth token
        if (token != cookie(user, conn)) {
          return crow::json::wvalue{{"error", "Unauthorized request."}};
        }

        std::vector<Account> accounts = get_passwords(user, conn);
        std::vector<crow::json::wvalue> final;
        for (auto acc : accounts)
          final.push_back(crow::json::wvalue{{"username", acc.m_account_name},
                                             {"password", acc.m_password},
                                             {"title", acc.m_title}});

        return crow::json::wvalue{crow::json::wvalue::list{{final}}};
      });

  CROW_ROUTE(app, "/delete-password")
      .methods(crow::HTTPMethod::GET,
               crow::HTTPMethod::PATCH)([&c](const crow::request &req) {
        pqxx::work conn = pqxx::work(c);
        char *username = req.url_params.get("username");
        char *password_hash = req.url_params.get("password_hash");
        char *token = req.url_params.get("token");
        char *pass_user = req.url_params.get("pass_user");
        char *pass_pass = req.url_params.get("pass_pass");

        // Find user
        User user = get_user(username, password_hash, conn);
        if (user.m_id == "-1") {
          return crow::json::wvalue{{"error", user.m_username}};
        }

        // Verify auth token
        if (token != cookie(user, conn)) {
          return crow::json::wvalue{{"error", "Unauthorized request."}};
        }

        if (delete_password(user, pass_user, pass_pass, conn) == "-1") {
          return crow::json::wvalue{{"error", "Password does not exist."}};
        }

        return crow::json::wvalue{{"success", "true"}};
      });

#if defined(IS_PROD) && IS_PROD == 1
  CROW_LOG_INFO << "Connecting over https";
  app.ssl_file("/ssl_key/certificate.crt", "/ssl_key/private.key");
#endif

  app.port(18080).multithreaded().run();

  return 0;
}
