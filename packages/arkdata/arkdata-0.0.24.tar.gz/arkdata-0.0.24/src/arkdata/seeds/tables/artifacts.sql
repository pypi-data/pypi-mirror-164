DROP TABLE IF EXISTS artifacts;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS artifacts(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	class_name VARCHAR(100) DEFAULT NULL,
    stack_size SMALLINT UNSIGNED DEFAULT 1,
    image_url varchar(500) DEFAULT NULL,
    blueprint varchar(500) DEFAULT NULL,
    description TEXT DEFAULT NULL,
    summary TEXT DEFAULT NULL,
    url VARCHAR(500) DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX artifact_by_name
ON artifacts (name);


