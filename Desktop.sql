create database Twitch_API_Repo;

use Twitch_API_Repo;

SELECT * FROM mysql.user;

CREATE TABLE users (
	ID INT AUTO_INCREMENT PRIMARY KEY,
    username CHAR(100),
    email CHAR(100),
    hash_password CHAR(255),
    access_token CHAR(100) DEFAULT '',
    boradcaster_id CHAR(100) DEFAULT ''
);

INSERT INTO users (username, email, hash_password, access_token, boradcaster_id) 
VALUES ('john_doe', 'john@example.com', 'hashed_password123', '', '');

UPDATE users SET broadcaster_id = 'new_broadcaster_id' WHERE id = 'your_user_id';

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

SELECT * FROM users WHERE username = 'benson' and hash_password = '28627344';

UPDATE users SET access_token = '6mp6ju1bnrid8t3hjpg7nx8ulfhq5c' WHERE ID = '1';

DROP TABLE users ;

SHOW PROCESSLIST;

DROP TABLE channel_VIP_follower;

DROP TABLE channel_MOD_follower;