-- This script creates the 'hbtn_0d_usa' database and the 'states' table on the MySQL server if not already existing.
-- Description of 'states':
   -- id: INT unique, auto-generated, cannot be null, primary key
   -- name: VARCHAR(256), cannot be null
-- If the 'hbtn_0d_usa' database or the 'states' table already exist, the script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
