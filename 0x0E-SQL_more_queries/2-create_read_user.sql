-- creating the database hbtn_0d_2 and the user user_0d_2
   -- the user_0d_2 should have only SELECT privileges in database hbtn_0d_2
   -- The user_0d_2 password should be set to user_0d_2_pwd
   -- If database hbtn_0d_2 is already existing the script should not fail
   -- If the user user_0d_2 is already existing the your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
