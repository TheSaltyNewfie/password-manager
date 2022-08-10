#include <iostream>
#define CROW_MAIN
#include "../include/crow_all.h"
#include "../include/schemas.hpp"
#include <pthread.h>
#include <pqxx/pqxx>

int main() {
    crow::SimpleApp app;
    pqxx::connection c("dbname=server user=server");

    //Perhaps we can get params in the link? and get the keys and what not via that
    CROW_ROUTE(app, "/")([](){
        return "Hello world";
    });

    std::cout << "Ay Yo?";

    app.port(18080).multithreaded().run();

    return 0; 
}
