DROP TABLE IF EXISTS creatures;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS creatures(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
    name_tag VARCHAR(100) DEFAULT NULL,
    category VARCHAR(100) DEFAULT NULL,
	class_name VARCHAR(100) DEFAULT NULL,
	-- type ENUM('FLYER','GROUND','GLIDER','AQUATIC','TITAN','OTHER') DEFAULT 'OTHER',
    entity_id VARCHAR(100) DEFAULT NULL,
    blueprint varchar(500) DEFAULT NULL,
    small_image_url VARCHAR(500) DEFAULT NULL,
    large_image_url VARCHAR(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    url VARCHAR(500) DEFAULT NULL,
    color_id SMALLINT UNSIGNED DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX creature_by_name
ON creatures (name);

CREATE INDEX creature_by_name_tag
ON creatures (name_tag);


