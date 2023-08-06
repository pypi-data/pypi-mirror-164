-- Open the terminal
-- terminal> mysql -u user -p
-- mysql> source /path/to/this/init.sql


-- Drop the test database --
DROP DATABASE IF EXISTS test_ark;
CREATE DATABASE IF NOT EXISTS test_ark;
CREATE SCHEMA IF NOT EXISTS test_ark;


-- Use the new database --
USE test_ark;

SOURCE bundles.sql;
SOURCE creatures.sql;
SOURCE ammunitions.sql;
SOURCE saddles.sql;
SOURCE products.sql


-- Drop the database --
DROP DATABASE IF EXISTS ark;
CREATE DATABASE IF NOT EXISTS ark;
CREATE SCHEMA IF NOT EXISTS ark;


-- Use the new database --
USE ark;

SOURCE bundles.sql;
SOURCE creatures.sql;
SOURCE ammunitions.sql;
SOURCE saddles.sql;
SOURCE products.sql
