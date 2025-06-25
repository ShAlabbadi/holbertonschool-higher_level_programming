-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id , name FROM hbtn_0d_usa.states WHERE name = California;
SELECT id , state_id , name FROM hbtn_0d_usa.cities WHERE name = California ORDER BY cities.id ASC;
