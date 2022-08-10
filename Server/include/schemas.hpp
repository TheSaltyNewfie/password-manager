#pragma once

#include <string>

class User 
{
public:
    uint64_t m_id;
    std::string m_username;
    std::string m_password_hash;
    std::string m_salt;
public:
    User(uint64_t id, std::string username, std::string password_hash, std::string salt)
        : m_username(username), m_password_hash(password_hash), m_id(id), m_salt(salt)
    {
    }
};

class Password
{
public:
    uint64_t m_id;
    std::string m_account_name;
    std::string m_password;
    std::string m_salt;
public:
    Password(uint64_t id, std::string account_name, std::string password, std::string salt)
        : m_id(id), m_account_name(account_name), m_password(password), m_salt(salt)
    {
    }
};

