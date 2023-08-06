DROP TABLE IF EXISTS saddles;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS saddles(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	creature_name_tag VARCHAR(100) NOT NULL,
    type ENUM('PLATFORM','TEK','REGULAR','OTHER') DEFAULT 'OTHER',
	stack_size SMALLINT DEFAULT 1,
	class_name VARCHAR(100) DEFAULT NULL,
    blueprint varchar(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    image_url varchar(500) DEFAULT NULL,
    summary TEXT DEFAULT NULL,
    url VARCHAR(500) DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX saddle_by_name
ON saddles (name);

CREATE INDEX saddle_by_creature_name_tag
ON saddles (creature_name_tag);
