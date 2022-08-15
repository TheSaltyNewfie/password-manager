#pragma once

#include "schemas.hpp"
#include <pqxx/pqxx>
#include <string>
#include <vector>

std::string cookie(User user, pqxx::work& conn);
User get_user(const char *username, const char *password, pqxx::work& conn);
User create_user(const char *username, const char *password_hash, pqxx::work &conn);
Password create_password(User user, const char* username, const char* password, pqxx::work& conn);
std::vector<Account> get_passwords(User user, pqxx::work& conn);

