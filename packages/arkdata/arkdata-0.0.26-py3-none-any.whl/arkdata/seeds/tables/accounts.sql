DROP TABLE IF EXISTS account;


-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	xuid VARCHAR(100) NOT NULL,
    player_id BIGINT UNSIGNED DEFAULT NULL,
    player_name VARCHAR(100) DEFAULT NULL,
    tribe_id BIGINT UNSIGNED DEFAULT NULL,
    tribe_name VARCHAR(100) DEFAULT NULL,
    berry_bush_seeds BIGINT UNSIGNED DEFAULT 0 NOT NULL,
    influence_points BIGINT UNSIGNED DEFAULT 0 NOT NULL,
    nitrado_id VARCHAR(100) NULL DEFAULT NULL,
    server_id VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(xuid) REFERENCES users(xuid) ON DELETE CASCADE,
    UNIQUE (xuid)
);


CREATE INDEX accounts_xuid
ON accounts (xuid);

CREATE INDEX accounts_nitrado_id
ON accounts (nitrado_id);
