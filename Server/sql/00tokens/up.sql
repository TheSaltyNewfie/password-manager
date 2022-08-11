-- session management
CREATE TABLE Tokens (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL REFERENCES Users(id),
    token TEXT NOT NULL
);

