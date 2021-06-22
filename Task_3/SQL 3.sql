SELECT a.aircraft_code, a.model, s.seat_no, s.fare_conditions, rank()
OVER (PARTITION BY a.aircraft_code ORDER BY s.seat_no)
FROM aircrafts AS a JOIN seats AS s
ON a.aircraft_code = s.aircraft_code
WHERE a.aircraft_code = '773' AND s.fare_conditions = 'Economy';