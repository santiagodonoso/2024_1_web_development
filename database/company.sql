PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS counter;
CREATE TABLE counter(
    total_users     INTEGER DEFAULT 0
);

INSERT INTO counter VALUES(0);
SELECT * FROM counter;


DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_pk                 TEXT,
    user_name               TEXT,
    user_updated_at         TEXT,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;


-- Only index if there is a search on that column
CREATE INDEX index_user_name ON users(user_name);


-- Trigger to update a user on update_at
CREATE TRIGGER IF NOT EXISTS trigger_update_user AFTER UPDATE ON users
BEGIN
    UPDATE users 
    SET user_updated_at = "Wed 14 Feb 2024"
    WHERE user_pk = OLD.user_pk;
END;

-- CREATE A TRIGGER THAT SETS THE "user_deleted_at" to the actual data
-- whenever a user is deleted. You are doing a soft delete



CREATE TRIGGER IF NOT EXISTS trigger_update_total_users 
AFTER INSERT ON users
BEGIN
    UPDATE counter SET total_users = total_users + 1;
END;



-- SEED
INSERT INTO users VALUES("1", "One", "0");
INSERT INTO users VALUES("2", "Two", "0");
INSERT INTO users VALUES("3", "Three", "0");
INSERT INTO users VALUES("4", "Four", "0");


UPDATE users SET user_name = "Santiago" WHERE user_pk = "1" ;



SELECT * FROM users;


DROP TABLE IF EXISTS phones;
CREATE TABLE phones(
    phone_user_fk   TEXT,
    phone           TEXT,
    -- FOREIGN KEY(phone_user_fk) REFERENCES users(user_pk) ON DELETE CASCADE,
    FOREIGN KEY(phone_user_fk) REFERENCES users(user_pk) ON DELETE RESTRICT,
    PRIMARY KEY(phone_user_fk, phone)
) WITHOUT ROWID;

-- SEED
INSERT INTO phones VALUES("1", "111");
INSERT INTO phones VALUES("1", "112");
INSERT INTO phones VALUES("3", "333");

SELECT * FROM phones;



-- DELETE FROM users WHERE user_pk = "1";
-- SELECT * FROM users;
-- SELECT * FROM phones;


PRAGMA foreign_keys = ON;
DELETE FROM users WHERE user_pk = "1";

DELETE FROM phones WHERE phone_user_fk = "1"

SELECT * FROM phones;

DELETE FROM users WHERE user_pk = "1";

-- TRIGGER
-- Update the number of users in a table whenever a new user is inserted
-- in the users table
-- Capitalize the user's name whenever it is inserted
-- Combine the name and the last name
-- INSERT UPDATE DELETE





-- CREATE TRIGGER update_customer_address UPDATE OF address ON customers 
-- BEGIN
--     UPDATE orders SET address = new.address WHERE customer_name = old.name;
-- END;

















