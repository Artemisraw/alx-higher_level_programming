-- Lists all records of the table in order of score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC, name;
