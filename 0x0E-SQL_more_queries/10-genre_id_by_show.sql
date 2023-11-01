-- Query tv shows that have linked genres then join them together
-- Then sort title & genres in ascending order
SELECT `tv_shows.title`, `tv_show_genres.genre_id` FROM `tv_shows`
INNER JOIN `tv_show_genres` ON `tv_shows.id` = `tv_show_genres.show_id`
ORDER BY `tv_shows.title` ASC, `tv_show_genres.genre_id` ASC;