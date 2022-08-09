#include <iostream>
#define CROW_MAIN
#include "../include/crow_all.h"
#include <pthread.h>

int main() {

    crow::SimpleApp app;

    //Perhaps we can get params in the link? and get the keys and what not via that
    CROW_ROUTE(app, "/")([](){
        return "Hello world";
    });

    std::cout << "Ay Yo?";

    app.port(18080).multithreaded().run();

    return 0; 
}
