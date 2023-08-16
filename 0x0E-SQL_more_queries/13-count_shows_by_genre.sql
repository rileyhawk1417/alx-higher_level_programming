-- Query tv shows that have genres & list number of shows
-- Then sort genres & number of shows in descending order
SELECT `tv_genres.name` AS `genre`, COUNT(`tv_show_genres.genre_id`) AS `number_of_shows`
FROM `tv_shows`
RIGHT JOIN `tv_show_genres` ON `tv_genres.id` = `tv_show_genres.genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows` DESC;
