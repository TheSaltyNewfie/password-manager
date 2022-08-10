#include <iostream>
#define CROW_MAIN
#include "../include/crow_all.h"
#include <pthread.h>

int main() {

    crow::SimpleApp app;

    CROW_ROUTE(app, "/auth").methods(crow::HTTPMethod::GET, crow::HTTPMethod::PATCH)
    ([](const crow::request& req)
    {

        char* user_id = req.url_params.get("userid");
        char* password = req.url_params.get("password");

        if(user_id != nullptr && password != nullptr)
        {
            std::cout << "[AUTH] USER ID: " << user_id << "\nPASSWORD: " << password << std::endl;
            return crow::json::wvalue{{"user_id", user_id}, {"password", password}};
        }

        return crow::json::wvalue{{"error", "error details would be here"}};
    });
    std::cout << "Ay Yo?\n";

    app.port(18080).multithreaded().run();

    return 0; 
}
