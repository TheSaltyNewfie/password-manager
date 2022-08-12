-- user table

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE Users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL DEFAULT gen_salt('md5')
);

