-- Fetch genres for 'Dexter' tv show
SELECT `name` FROM `tv_genres`
LEFT JOIN `tv_show_genres` ON `tv_show_genres.id` = `tv_show_genres.genre_id`
LEFT JOIN `tv_shows` ON `tv_show_genres.id` = `tv_shows.id`
WHERE `tv_shows.title` = `Dexter`
GROUP BY name
ORDER BY name ASC;
