/*
This script prepares a MySQL server for the project by creating a new database,
a new user with specific privileges, and setting up their password.
*/

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if they don't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant SELECT privilege on the performance_schema database to the new user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Tell MySQL to reload the grant tables, making all changes take effect immediately
FLUSH PRIVILEGES;
