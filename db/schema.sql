CREATE DATABASE food_nutrition_db;
\c food_nutrition_db;


-- CREATE TABLE foods(
--   id SERIAL PRIMARY KEY,
--   name TEXT,
--   image_url TEXT
-- );

-- SELECT * FROM foods; 
-- q to quit table
-- DROP TABLE foods;

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT
);

ALTER TABLE users ADD COLUMN password_digest TEXT;

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  food_id INTEGER
);

-- This table will store the information I require
CREATE TABLE foods(
  id SERIAL PRIMARY KEY,
  name TEXT,
  calories TEXT, 
  protein TEXT,
  carbohydrates TEXT,
  image_url TEXT
);

ALTER TABLE foods ALTER COLUMN calories TYPE NUMERIC USING calories::numeric; -- I had to change the calories from TEXT to Numeric so I could properly read foods that 200 calories or less
SELECT * FROM foods WHERE calories <= 200; -- This will correctly show the desired foods at 200 calories or less



-- Lets get ALL columns for ALL users from our table:                                           -- SELECT * FROM users;

-- What if we only want "name" and "location" from users table:                                 --SELECT name, location FROM users;

-- What if we want ONLY the users from adelaide?                                                --SELECT * FROM users WHERE location = 'adelaide';

-- What if we ONLY want users starting with the letter "r" in their name:                       --SELECT * FROM users WHERE name ILIKE 'r%';

-- What if we ONLY want users containing the letter "r" in their name:                          --SELECT * FROM users WHERE name ILIKE '%r%';

-- U = Update records in a table:
-- NOTE: ALWAYS use a WHERE clause with Update
                                                                                                --UPDATE users SET name = 'kasun maldeni' WHERE id = 1;

-- D = Delete records in a table:
-- NOTE: ALWAYS use a WHERE clause with Delete
                                                                                                -- DELETE FROM users WHERE id = 1;
-- If I wanted to quickly re-add a food for testing purposes
-- Canned Tuna
-- 85
-- 16g
-- 0g
-- https://assets.epicurious.com/photos/5ae7955643d4bc0a5b3f3e34/1:1/w_3643,h_3643,c_limit/Tuna-Taste-Test-25022018.jpg