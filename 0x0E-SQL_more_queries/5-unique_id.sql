-- This script creates the 'unique_id' table on MySQL server if it doesn't already exist.
-- Description of 'unique_id':
   -- id: INT with default value 1, must be unique
   -- name: VARCHAR(256)
-- The database name will be provided as an argument to the mysql command.
-- If the 'unique_id' table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS unique_id (
   id INT DEFAULT 1,
   UNIQUE (id),
   name VARCHAR(256)
);
