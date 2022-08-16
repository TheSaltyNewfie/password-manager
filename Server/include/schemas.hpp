#pragma once

#include <string>

class User {
public:
  std::string m_id;
  std::string m_username;
  std::string m_password_hash;
  std::string m_salt;

public:
  User(std::string id, std::string username, std::string password_hash,
       std::string salt)
      : m_id(id), m_username(username), m_password_hash(password_hash),
        m_salt(salt) {}
};

class Password {
public:
  std::string m_id;
  std::string m_user_id;
  std::string m_account_name;
  std::string m_password;
  std::string m_salt;

public:
  Password(std::string id, std::string user_id, std::string account_name,
           std::string password, std::string salt)
      : m_id(id), m_user_id(user_id), m_account_name(account_name),
        m_password(password), m_salt(salt) {}
};

class Account {
public:
  std::string m_account_name;
  std::string m_password;
  std::string m_title;

public:
  Account(std::string name, std::string password, std::string title)
      : m_account_name(name), m_password(password), m_title(title) {}
};
