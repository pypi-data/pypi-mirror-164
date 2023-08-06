DROP TABLE IF EXISTS weapons;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS weapons(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	class_name VARCHAR(100) DEFAULT NULL,
    type ENUM('MELEE', 'PROJECTILE', 'EXPLOSIVE', 'OTHER') DEFAULT 'OTHER',
    stack_size SMALLINT UNSIGNED DEFAULT 1,
    image_url VARCHAR(500) DEFAULT NULL,
    blueprint VARCHAR(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    summary TEXT DEFAULT NULL,
    url VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX weapon_by_name
ON weapons (name);


