-- Create the users table
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk         TEXT,
    user_name       TEXT,
    user_price      INTEGER,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;

-- Insert data into the users table
INSERT INTO users (user_pk, user_name, user_price) VALUES ("1", "One", 10);
INSERT INTO users VALUES ("2", "Two", 20.20);
INSERT INTO users VALUES ("3", "Three", 30);
INSERT INTO users VALUES ("4", "Four", 40);
INSERT INTO users VALUES ("5", "Five", 50);
INSERT INTO users VALUES ("6", "Six", 60);
INSERT INTO users VALUES ("7", "Seven", 70);
INSERT INTO users VALUES ("8", "Eight", 80);
INSERT INTO users VALUES ("9", "Nine", 90);
INSERT INTO users VALUES ("10", "Ten", 100);

-- Show all users
SELECT * FROM users;

SELECT * FROM users ORDER BY user_name ASC;
SELECT * FROM users ORDER BY user_name DESC;

SELECT * FROM users ORDER BY user_price ASC;


--                                            start  get
SELECT * FROM users ORDER BY user_price ASC LIMIT 0, 2;

-- LIKE wildcards
-- Name that start with an specific letter
SELECT * FROM users WHERE user_name LIKE "a%";
SELECT * FROM users WHERE user_name LIKE "mi%";
SELECT * FROM users WHERE user_name LIKE "%sen";
SELECT * FROM users WHERE user_name LIKE "%en";
SELECT * FROM users WHERE user_name LIKE "%oa%";  -- soap

-- Create a SQL command that gets any user containing the "i" in the name
SELECT * FROM users WHERE user_name LIKE "%i%";

-- Create a SQL command that gets any user containing the "f" at the end
SELECT * FROM users WHERE user_name LIKE "%f";

-- SQL you can use AND, you can also use OR
-- Create a SQL command that gets any user name 
-- containing the "i" in the name AND the price is above 1
-- above >
SELECT * FROM users WHERE user_name LIKE "%i%" AND user_price > 60;

-- Delete user by id
DELETE FROM users WHERE user_pk = "842d9ed8-1e4c-438a-8980-b67f0d5e9994";


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

















