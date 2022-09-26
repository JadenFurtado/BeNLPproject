CREATE DATABASE caterNinja;

CREATE TABLE usersData(
    userId INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userName VARCHAR(100),
    userPassword VARCHAR(100),
    userEmail VARCHAR(50),
    userPhoneNumber VARCHAR(10)
);