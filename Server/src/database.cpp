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

  return User("-1", "User does not exist.", "", "");
}

User create_user(const char *username, const char *password_hash,
                 pqxx::work &conn) {
  try {
    pqxx::row row =
        conn.exec1("INSERT INTO users (username, password_hash) VALUES ('" +
                   conn.esc(username) + "', '" + conn.esc(password_hash) +
                   "') RETURNING *");
    std::string id = row[0].c_str(), user = row[1].c_str(), password = row[2].c_str(), salt = row[3].c_str();
    conn.commit();
    return User(id, user, password, salt);
  } catch (std::exception const &e) {
    return User("-1", e.what(), "", "");
  }
}
