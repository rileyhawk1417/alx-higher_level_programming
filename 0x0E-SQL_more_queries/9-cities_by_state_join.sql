-- Query cities.id, cities.name, states.name & order cities.id by ascending
-- Use left join to combine results
SELECT `cities.id`, `cities.name`, `states.name` FROM `cities`
LEFT JOIN states ON states.id = cities.state_id
ORDER BY `cities.id` ASC;
