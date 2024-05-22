-- Script creating the 'hbtn_0d_usa' database and the 'cities' table within it on MySQL server.
-- Description:
   -- 'hbtn_0d_usa' database
   -- 'cities' table with columns:
      -- id: INT unique, auto-generated, not null, primary key
      -- state_id: INT, not null, FOREIGN KEY referencing the 'id' column of the 'states' table
      -- name: VARCHAR(256), not null
-- If the 'hbtn_0d_usa' database or the 'cities' table already exist, the script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL
);
