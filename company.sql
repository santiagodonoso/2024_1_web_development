-- Create the users table
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk         TEXT,
    user_name       TEXT,
    user_price      TEXT,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;

-- Insert data into the users table
INSERT INTO users (user_pk, user_name, user_price) VALUES ("842d9ed8-1e4c-438a-8980-b67f0d5e9994", "One", 10);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f2113e620f", "Two", 20);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f3113e630f", "Three", 30);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f4113e640f", "Four", 40);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f5113e655f", "Five", 50);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e660f", "Six", 60);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e670f", "Seven", 70);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e680f", "Eight", 80);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e690f", "Nine", 90);
INSERT INTO users VALUES ("f6912761-b085-4e9c-ad26-74f6113e611f", "Ten", 100);

-- Show all users
SELECT * FROM users;

SELECT * FROM users ORDER BY user_name ASC;
SELECT * FROM users ORDER BY user_name DESC;

SELECT * FROM users ORDER BY user_price ASC;



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

















