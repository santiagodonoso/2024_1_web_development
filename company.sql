-- Delete the whole table
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk         INTEGER,
    user_name       TEXT,
    user_last_name  TEXT
);

INSERT INTO users VALUES(1, "Santiago", "Donoso");
INSERT INTO users VALUES(2, "Two", "Two2");
INSERT INTO users VALUES(3, "Three", "Three3");


-- Delete user with id 2
DELETE FROM users WHERE user_pk = 2;

-- Show all users
SELECT * FROM users;

