DROP TABLE IF EXISTS armours;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS armours(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	class_name VARCHAR(100) DEFAULT NULL,
    type ENUM('CLOTH','HIDE','DESERT','FUR','GHILLIE','CHITIN','HAZARD','SCUBA','FLAK','RIOT','TEK','OTHER') DEFAULT 'OTHER',
    stack_size SMALLINT UNSIGNED DEFAULT 1,
    body ENUM('MASK','CHESTPIECE','LEGGINGS','GAUNTLETS','BOOTS','OTHER') DEFAULT 'OTHER',
    image_url varchar(500) DEFAULT NULL,
    blueprint varchar(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    summary TEXT DEFAULT NULL,
    url VARCHAR(500) DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX armour_by_name
ON armours (name);


