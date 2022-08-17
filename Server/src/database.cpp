#include "database.hpp"
#include "schemas.hpp"
#include <array>
#include <crow_all.h>
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
                 std::string salt, pqxx::work &conn) {
  try {
    pqxx::row row = conn.exec1(
        "INSERT INTO users (username, password_hash, salt) VALUES ('" +
        conn.esc(username) + "', '" + conn.esc(password_hash) + "', '" +
        conn.esc(salt) + "') RETURNING *");
    std::string id = row[0].c_str(), user = row[1].c_str(),
                password = row[2].c_str(), salt = row[3].c_str();
    conn.commit();
    return User(id, user, password, salt);
  } catch (std::exception const &e) {
    return User("-1", e.what(), "", "");
  }
}

Password create_password(User user, const char *username, const char *password,
                         const char *title, pqxx::work &conn) {
  try {
    pqxx::row row = conn.exec1(
        "INSERT INTO passwords (user_id, account_name, password, title) VALUES "
        "('" +
        conn.esc(user.m_id) + "', '" + conn.esc(username) + "', '" +
        conn.esc(password) + "', '" + conn.esc(title) + "') RETURNING *");
    conn.commit();
    return Password(row[0].c_str(), row[1].c_str(), row[2].c_str(),
                    row[3].c_str(), row[4].c_str());
  } catch (std::exception const &e) {
    return Password("-1", e.what(), "", "", "");
  }
}

std::vector<Account> get_passwords(User user, pqxx::work &conn) {
  try {
    std::vector<Account> accounts;
    for (auto [username, password, title] :
         conn.query<std::string, std::string, std::string>(
             "SELECT account_name, password, title FROM passwords WHERE "
             "user_id = '" +
             pqxx::to_string(user.m_id) + "'::uuid")) {
      accounts.push_back(Account(username, password, title));
    }
    return accounts;
  } catch (std::exception const &e) {
    std::cout << "Error: " << e.what() << std::endl;
    return std::vector<Account>();
  }
}

std::string delete_password(User user, std::string username,
                            std::string password, pqxx::work &conn) {
  try {
    conn.exec0("DELETE FROM passwords WHERE account_name = '" +
               conn.esc(username) + "' AND password = '" + conn.esc(password) +
               "' AND user_id = '" + pqxx::to_string(user.m_id) + "'");
    conn.commit();
    return "success";
  } catch (std::exception const &e) {
    return "-1";
  }
}

std::string get_salt(pqxx::work &conn) {
  try {
    for (auto [salt] : conn.query<std::string>("SELECT gen_salt('md5')"))
      return salt;
  } catch (std::exception const &e) {
    CROW_LOG_ERROR << "Couldn't get salt: " << e.what();
    exit(1);
  }
  return "";
}

std::string get_salt(const char *username, pqxx::work &conn) {
  try {
    for (auto [salt] :
         conn.query<std::string>("SELECT salt FROM users WHERE username = '" +
                                 std::string(username) + "'"))
      return salt;
  } catch (std::exception const &e) {
    CROW_LOG_ERROR << "Couldn't get init_vec: " << e.what();
    exit(1);
  }
  return "";
}

std::string get_init_vec(pqxx::work &conn) {
  try {
    for (auto [init_vec] :
         conn.query<std::string>("SELECT gen_random_bytes(16)"))
      return init_vec;
  } catch (std::exception const &e) {
    CROW_LOG_ERROR << "Couldn't get init_vec: " << e.what();
    exit(1);
  }
  return "";
}
