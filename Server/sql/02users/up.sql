-- user table

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE Users (
    id uuid PRIMARY KEY,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL DEFAULT gen_salt('md5')
);

