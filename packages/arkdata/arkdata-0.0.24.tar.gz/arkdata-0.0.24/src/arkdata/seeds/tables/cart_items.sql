-- Cart

DROP TABLE IF EXISTS cart_items;


-- -------------- --
-- Table Creation --
-- -------------- --

CREATE TABLE IF NOT EXISTS cart_items(
	id INT UNSIGNED AUTO_INCREMENT UNIQUE,
	xuid VARCHAR(100) NOT NULL,
	product_id MEDIUMINT UNSIGNED NOT NULL,
    quantity MEDIUMINT UNSIGNED NOT NULL DEFAULT 1,
    PRIMARY KEY(id),
    FOREIGN KEY(xuid) REFERENCES users(xuid) ON DELETE CASCADE,
    FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE,
    UNIQUE (id, xuid, product_id)
);


CREATE INDEX by_cart_items
ON cart_items (id, xuid, product_id);