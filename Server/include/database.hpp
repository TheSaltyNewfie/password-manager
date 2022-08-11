#pragma once

#include "schemas.hpp"
#include <pqxx/pqxx>
#include <string>

std::string cookie(User user, pqxx::work& conn);
User get_user(const char *username, const char *password, pqxx::work& conn);

