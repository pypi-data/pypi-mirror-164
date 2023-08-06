-- Commands


DROP TABLE IF EXISTS servers;


-- -------------- --
-- Table Commands --
-- -------------- --

CREATE TABLE IF NOT EXISTS servers(
	id SMALLINT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(100) NULL DEFAULT 'UNKNOWN',
    xuid VARCHAR(100) UNIQUE DEFAULT NULL,
    player_id VARCHAR(100) DEFAULT NULL,
    nitrado_id VARCHAR(200) DEFAULT NULL,
	map VARCHAR(100) DEFAULT NULL,
	address VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
);




CREATE INDEX by_address_xuid
ON servers (address, xuid);


