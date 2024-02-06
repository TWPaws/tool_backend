create database Twitch_API_Repo;

use Twitch_API_Repo;

CREATE TABLE users (
    Email CHAR(100) PRIMARY KEY,
    broadcaster_id CHAR(100),
    access_token CHAR(50)
);

CREATE TABLE channel_VIP_follower (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    broadcaster_id INT,
    FOREIGN KEY(broadcaster_id) REFERENCES users(broadcaster_id),
    user_name CHAR(100)
);

CREATE TABLE channel_MOD_follower (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    broadcaster_id INT,
    FOREIGN KEY(broadcaster_id) REFERENCES users(broadcaster_id),
    user_name CHAR(100)
);

show tables;

select * from users;

DROP TABLE users ;

DROP TABLE channel_VIP_follower;

DROP TABLE channel_MOD_follower;