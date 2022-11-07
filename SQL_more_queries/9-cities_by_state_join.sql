-- 9-cities_by_state_join.sql

SELECT cities.id, cities.name, states.name FROM cities JOIN states on states.id = cities.state_id ORDER BY cities.id;