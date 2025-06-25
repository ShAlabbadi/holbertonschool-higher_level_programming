-- Write a script that displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) As max_temp FROM temperatures GROUP BY state ORDER BY max_temp ABC LIMIT 3;
