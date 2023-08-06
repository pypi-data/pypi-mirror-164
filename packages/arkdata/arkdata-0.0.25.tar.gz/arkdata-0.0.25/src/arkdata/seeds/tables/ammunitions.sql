DROP TABLE IF EXISTS ammunitions;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS ammunitions(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	class_name VARCHAR(100) DEFAULT NULL,
    type ENUM('PROJECTILE','EXPLOSIVE','OTHER') DEFAULT 'OTHER',
    stack_size SMALLINT UNSIGNED DEFAULT 1,
    image_url varchar(500) DEFAULT NULL,
    blueprint varchar(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    summary TEXT DEFAULT NULL,
    url VARCHAR(500) DEFAULT NULL,
    weapon_id SMALLINT UNSIGNED DEFAULT NULL,
    weapon_type ENUM('WEAPON','STRUCTURE','SADDLE') DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX armour_by_name
ON ammunitions (name);


