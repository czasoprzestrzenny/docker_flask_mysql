CREATE DATABASE user_data;
use user_data;

CREATE TABLE animals_rank (
  name VARCHAR(20),
  value VARCHAR(10)
);

INSERT INTO animals_rank
  (name, value)
VALUES
  ('Python', '1'),
  ('Dog', '2');