-- password table
CREATE TABLE Passwords (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL REFERENCES Users(id),
    account_name TEXT NOT NULL,
    password TEXT NOT NULL,
    title TEXT NOT NULL,
    salt BYTEA NOT NULL DEFAULT gen_random_bytes(16)
);

