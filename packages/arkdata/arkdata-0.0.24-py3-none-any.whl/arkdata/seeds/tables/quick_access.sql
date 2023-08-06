DROP TABLE IF EXISTS quick_access;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS quick_access(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
    product_id MEDIUMINT UNSIGNED DEFAULT 0,
    creature_id MEDIUMINT UNSIGNED DEFAULT 0,
	CONSTRAINT UNIQUE (product_id, creature_id), -- UNIQUE permits NULLs
    CONSTRAINT CHECK (product_id is not NULL or creature_id is not null),
    PRIMARY KEY (id)
);