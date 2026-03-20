-- Statuses table
CREATE TABLE statuses (
    status_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Burgers table
CREATE TABLE burgers (
    burger_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description  TEXT
);

-- Ingredients table
CREATE TABLE ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
);

-- Burger_Ingredients table (many-to-many)
CREATE TABLE burger_ingredients (
    burger_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (burger_id, ingredient_id),
    FOREIGN KEY (burger_id) REFERENCES burgers(burger_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    burger_id INT NOT NULL,
    status_id INT NOT NULL,
    guest_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (burger_id) REFERENCES burgers(burger_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(status_id)
);
