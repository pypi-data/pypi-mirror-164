DROP TABLE IF EXISTS product_to_blueprint;

-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS product_to_blueprint(
	product_id MEDIUMINT UNSIGNED UNIQUE,
	blueprint_id MEDIUMINT UNSIGNED,
    FOREIGN KEY(product_id) REFERENCES product(id),
    FOREIGN KEY(blueprint_id) REFERENCES blueprint(id),
    PRIMARY KEY (product_id)
);
