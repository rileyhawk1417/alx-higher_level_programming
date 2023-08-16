-- Create database & user only grant new user SELECT access
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbnt_0d_2.*' TO 'user_0d_2'@'localhost';
