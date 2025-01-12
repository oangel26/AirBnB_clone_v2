-- Create the database hbnb_dev_db in your MySQL server.
-- If the database hbnb_test_db already exists, the script should not fail.
-- Create a new user hbnb_dev (in localhost) and a password.
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database).
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database).


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
