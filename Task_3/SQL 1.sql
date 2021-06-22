create extension cube;
create extension earthdistance;

SELECT first_airport, first_point, second_airport, second_point, 
(first_point <@> second_point) as distance
FROM(
SELECT a.airport_name AS first_airport, a.coordinates AS first_point, 
b.airport_name AS second_airport, b.coordinates AS second_point
FROM airports AS a CROSS JOIN 
(SELECT airport_name, coordinates FROM airports) AS b
) AS d
ORDER BY distance DESC
LIMIT 1;