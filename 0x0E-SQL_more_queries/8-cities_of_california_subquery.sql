-- Query states with name 'California' & order by ascending
-- With those id's then fetch the cities
SELECT `id`, `name` FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = `California`)
ORDER BY `id` ASC;
