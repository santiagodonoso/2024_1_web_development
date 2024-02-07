-- Create the users table
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk         TEXT,
    user_name       TEXT,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;

-- Insert data into the users table
INSERT INTO users (user_pk, user_name) VALUES ("842d9ed8-1e4c-438a-8980-b67f0d5e9994", "A");
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e650f", "B");

-- Show all users
SELECT * FROM users;

-- Create a table to test how to build a compound/composite key
-- DROP TABLE IF EXISTS demo;

-- CREATE TABLE demo(
--     user_fk         TEXT,
--     role_fk         TEXT,
--     PRIMARY KEY(user_fk, role_fk)
-- ) WITHOUT ROWID;

-- INSERT INTO demo VALUES("1", "10");
-- INSERT INTO demo VALUES("2", "20");

-- SELECT * FROM demo;

















