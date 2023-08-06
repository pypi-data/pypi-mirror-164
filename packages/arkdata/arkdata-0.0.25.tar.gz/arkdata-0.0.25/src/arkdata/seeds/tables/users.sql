DROP TABLE IF EXISTS user;


-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS users(
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	xuid VARCHAR(100) NOT NULL,
	gamertag VARCHAR(100) NOT NULL,
	password_digest VARCHAR(100) DEFAULT NULL,
	session_token VARCHAR(100) DEFAULT NULL,
	authentication_token VARCHAR(200) DEFAULT NULL,
	authenticated BOOL DEFAULT FALSE,
	discord_username VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (id),
	UNIQUE (xuid),
	UNIQUE (gamertag)
);

CREATE INDEX by_user_gamertag
ON users (gamertag);

CREATE INDEX by_user_xuid
ON users (xuid);

CREATE INDEX by_user_session_token
ON users (session_token);

CREATE INDEX by_user_authentication_token
ON users (authentication_token);

