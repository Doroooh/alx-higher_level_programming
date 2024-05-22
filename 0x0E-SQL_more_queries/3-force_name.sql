-- This script creates the 'force_name' table on your MySQL server if it doesn't already exist.
-- Description of 'force_name':
   -- id: INT
   -- name: VARCHAR(256) cannot be null
-- The database name will be provided as an argument to the mysql command.
-- If the 'force_name' table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS force_name (
   id INT,
   name VARCHAR(256) NOT NULL
);
