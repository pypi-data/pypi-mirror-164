DROP TABLE IF EXISTS order_items;

-- -------------- --
-- Table Orders --
-- -------------- --

CREATE TABLE IF NOT EXISTS order_items(
	id BIGINT UNSIGNED AUTO_INCREMENT,
	order_id VARCHAR(100) NOT NULL,
	xuid VARCHAR(100) NOT NULL,
	product_id MEDIUMINT UNSIGNED NOT NULL,
    quantity MEDIUMINT UNSIGNED NULL DEFAULT 1,
    delivered BOOL NULL DEFAULT FALSE,
    date DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(xuid) REFERENCES users(xuid) ON DELETE CASCADE,
    FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE,
    UNIQUE (order_id, xuid, product_id)
);


CREATE INDEX by_order_items
ON order_items (xuid, order_id, product_id);

