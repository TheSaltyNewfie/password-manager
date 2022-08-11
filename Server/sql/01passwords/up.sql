-- password table
CREATE TABLE Passwords (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES Users(id),
    account_name TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL
);

