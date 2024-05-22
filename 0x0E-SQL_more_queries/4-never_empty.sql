-- This script creates the 'id_not_null' table on your MySQL server if it doesn't already exist.
-- Description of 'id_not_null':
   -- id: INT with default value 1
   -- name: VARCHAR(256)
-- The database name will be provided as an argument to the mysql command.
-- If the 'id_not_null' table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
   id INT DEFAULT 1,
   name VARCHAR(256)
);
