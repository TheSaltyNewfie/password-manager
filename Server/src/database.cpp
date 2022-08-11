#include "database.hpp"
#include "schemas.hpp"
#include <iostream>
#include <pqxx/pqxx>

std::string cookie(User user, pqxx::work &conn) {
  std::string cookie = conn.query_value<std::string>(
      "SELECT hmac('" + pqxx::to_string(user.m_id) + "', '" +
      pqxx::to_string(user.m_salt) + "', 'sha256')");

  return cookie;
}

User get_user(const char *username, const char *password, pqxx::work &conn) {
  for (auto [id, salt] : conn.query<std::string, std::string>(
           "SELECT id, salt FROM users "
           "WHERE username = '" +
           pqxx::to_string(username) + "' AND password_hash = '" +
           pqxx::to_string(password) + "'"))
    return User(id, username, password, salt);

  return User("-1", "", "", "");
}
