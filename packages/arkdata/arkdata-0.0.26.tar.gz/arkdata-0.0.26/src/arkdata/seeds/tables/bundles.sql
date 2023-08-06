DROP TABLE IF EXISTS bundles;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS bundles(
	id MEDIUMINT UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
    group_id MEDIUMINT UNSIGNED NOT NULL,
    type_id MEDIUMINT UNSIGNED NOT NULL,
    type ENUM('CREATURE','ARMOUR','AMMUNITION','STRUCTURE','WEAPON','TOOL','CONSUMABLE','SADDLE','ARTIFACT','RESOURCE'),
    PRIMARY KEY (id)
);

CREATE INDEX bundles_by_name
ON bundles (name);
