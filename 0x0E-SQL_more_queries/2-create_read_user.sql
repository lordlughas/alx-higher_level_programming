-- creates the database hbtn_0d_2 and user user_0d_2
CREATE USER user_0d_2 IF NOT EXISTS IDENTIFIED BY 'user_0d_2_pwd'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
