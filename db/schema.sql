CREATE DATABASE food_nutrition_db;
\c food_nutrition_db;


CREATE TABLE foods(
  id SERIAL PRIMARY KEY,
  name TEXT,
  image_url TEXT
);

-- SELECT * FROM foods; 
-- q to quit table
-- DROP TABLE foods;


INSERT INTO foods(name, image_url)
VALUES
  ('Tacos', 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80'),
  ('Burger', 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=699&q=80');

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
-- CREATE TABLE foods(
--   id SERIAL PRIMARY KEY,
--   name TEXT,
--   calories TEXT, 
--   protein TEXT,
--   carbohydrates TEXT,
--   image_url TEXT
-- );




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
