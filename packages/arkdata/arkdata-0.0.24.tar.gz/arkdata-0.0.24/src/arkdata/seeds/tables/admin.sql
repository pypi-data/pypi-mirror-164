-- Commands


DROP TABLE IF EXISTS admin;


-- -------------- --
-- Table Admins --
-- -------------- --


CREATE TABLE IF NOT EXISTS admin(
    xuid VARCHAR(100) NOT NULL,
    gamertag VARCHAR(100) NOT NULL,
    admin_player_id BIGINT UNSIGNED NOT NULL,
    map VARCHAR(100) NOT NULL,
    player_name VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY(xuid, map)
);