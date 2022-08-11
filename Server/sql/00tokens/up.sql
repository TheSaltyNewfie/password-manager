-- session management
CREATE TABLE Tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES Users(id),
    token TEXT NOT NULL
);

