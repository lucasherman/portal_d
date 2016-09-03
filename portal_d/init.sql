CREATE SCHEMA `portal_d` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci ;
CREATE USER  'portal_d'@'localhost' IDENTIFIED BY '6121f28d';
GRANT ALL PRIVILEGES ON portal_d . * TO 'portal_d'@'localhost';