/*
This script prepares a MySQL server for the project by creating a new database,
a new user with the specific privileges, and setting up their password.
*/

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if they don't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the new user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Tell MySQL to reload the grant tables, making all changes take effect immediately
FLUSH PRIVILEGES;
