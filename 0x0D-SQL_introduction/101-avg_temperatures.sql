-- displays the average temperator by city

SELECT city, avg(value) AS avg_temperature FROM temperatures GROUP BY city ORDER BY avg_temperature DESC;
