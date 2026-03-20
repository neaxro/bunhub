-- ----------------------
-- STATUSES
-- ----------------------
INSERT INTO statuses (status_id, name) VALUES
(1, 'Pending'),
(2, 'In Progress'),
(3, 'Ready'),
(4, 'Delivered'),
(5, 'Cancelled');

-- ----------------------
-- INGREDIENTS
-- ----------------------
INSERT INTO ingredients (ingredient_id, name, is_available) VALUES
(1, 'cheese', TRUE),
(2, 'lettuce', TRUE),
(3, 'paradicsom', TRUE),
(4, 'onion', TRUE),
(5, 'majonese', TRUE),
(6, 'hot sauce', TRUE),
(7, 'pickle', TRUE);

-- ----------------------
-- BURGERS
-- ----------------------
INSERT INTO burgers (burger_id, name, description) VALUES
(1, 'Step-Bun Gets Toasted', 'It’s awkward, it’s messy, it’s exactly what the internet warned you about. You’ll love every bite anyway.'),
(2, 'POV: You’re the Patty', 'The patty’s in the spotlight… and so are you. Extreme heat, extreme flavor, zero regrets.'),
(3, 'Pickle Me Daddy', 'Tangy, briny, and borderline inappropriate. Crunchy domination in every bite.'),
(4, 'Juicy AF Bun', 'Dripping with flavor and dripping in chaos. You may need a towel. Or two.'),
(5, 'Hot Sauce & Chill', 'Netflix is optional. Spicy, messy, and guaranteed to ruin your social life (in a good way).'),
(6, 'Crybaby Crunch', 'Tears, laughter, and regret. Not necessarily in that order.'),
(7, 'The Dirty Secret Menu', 'Everything you weren’t supposed to order. Everything you secretly wanted.'),
(8, 'Quick & Filthy', 'Fast. Messy. Unapologetically addictive. You know what’s coming.'),
(9, 'Sauce Overload XXX', 'Creamy. Spicy. Absolutely uncensored. Only for the brave.');

-- ----------------------
-- BURGER INGREDIENTS
-- ----------------------

-- Step-Bun Gets Toasted
INSERT INTO burger_ingredients VALUES
(1,1,1),(1,2,1),(1,3,1),(1,5,1);

-- POV: You're the Patty
INSERT INTO burger_ingredients VALUES
(2,1,1),(2,4,1),(2,6,1),(2,5,1);

-- Pickle Me Daddy
INSERT INTO burger_ingredients VALUES
(3,1,1),(3,7,1),(3,4,1),(3,5,1);

-- Juicy AF Bun
INSERT INTO burger_ingredients VALUES
(4,2,1),(4,3,1),(4,1,1),(4,5,1);

-- Hot Sauce & Chill
INSERT INTO burger_ingredients VALUES
(5,1,1),(5,4,1),(5,7,1),(5,6,1);

-- Crybaby Crunch
INSERT INTO burger_ingredients VALUES
(6,4,1),(6,1,1),(6,5,1),(6,2,1);

-- The Dirty Secret Menu
INSERT INTO burger_ingredients VALUES
(7,1,1),(7,4,1),(7,7,1),(7,6,1),(7,5,1);

-- Quick & Filthy
INSERT INTO burger_ingredients VALUES
(8,1,1),(8,7,1),(8,5,1);

-- Sauce Overload XXX
INSERT INTO burger_ingredients VALUES
(9,5,1),(9,6,1),(9,4,1),(9,2,1);

-- ----------------------
-- ORDERS (TEST DATA)
-- ----------------------
INSERT INTO orders (burger_id, status_id, guest_name, email, comment) VALUES
(3, 1, 'John Doe', 'john@example.com', 'Extra pickles please 😏'),
(5, 2, 'Jane Smith', 'jane@example.com', 'Make it REALLY spicy'),
(1, 3, 'BurgerFan99', NULL, 'No comment, just hungry'),
(7, 1, 'SecretEater', 'secret@bunhub.dev', 'Don’t tell anyone I ordered this'),
(8, 4, 'QuickBite', NULL, 'Fast delivery pls'),
(9, 2, 'SauceLover', 'sauce@lover.com', 'More sauce if possible'),
(4, 5, 'MessyGuy', NULL, 'Changed my mind'),
(2, 3, 'POV_Master', 'pov@bunhub.dev', 'This better be good'),
(6, 1, 'CryingInside', NULL, 'I know what I signed up for');