-- List shows in desending order according to the sum of their rating
SELECT `title`, SUM(`tv_show_ratings.rate`) `rating`
FROM `tv_shows`
LEFT JOIN `tv_shows` ON `tv_show_ratings.show_id` = tv_shows._id
GROUP BY `title`
ORDER BY `rating` DESC;
