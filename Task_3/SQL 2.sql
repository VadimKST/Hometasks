SELECT a.model, COUNT(*) AS count_seats
FROM aircrafts AS a JOIN seats AS s
ON a.aircraft_code = s.aircraft_code
GROUP BY a.model
ORDER BY COUNT(*) DESC
LIMIT 1;