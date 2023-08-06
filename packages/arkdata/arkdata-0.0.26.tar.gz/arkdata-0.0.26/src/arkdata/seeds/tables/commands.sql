-- Commands


DROP TABLE IF EXISTS command;


-- -------------- --
-- Table Commands --
-- -------------- --

CREATE TABLE IF NOT EXISTS commands(
	id BIGINT UNSIGNED AUTO_INCREMENT,
    xuid VARCHAR(100) DEFAULT NULL, -- player who sent the command
    operation VARCHAR(100) NULL DEFAULT 'OTHER',
    operation_id MEDIUMINT UNSIGNED DEFAULT NULL,
	code TEXT NOT NULL,
    executed BOOL NULL DEFAULT FALSE,
    address VARCHAR(100) DEFAULT NULL,
    player_id VARCHAR(100) DEFAULT NULL, -- admin's player id
    server_id INT UNSIGNED DEFAULT NULL,
    PRIMARY KEY(id)
    -- FOREIGN KEY(xuid) REFERENCES users(xuid) ON DELETE CASCADE,
    -- FOREIGN KEY(address) REFERENCES servers(address) ON DELETE CASCADE
);



CREATE INDEX by_player_id
ON users (id);



