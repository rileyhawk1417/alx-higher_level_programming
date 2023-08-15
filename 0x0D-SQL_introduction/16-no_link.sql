-- Select score, name from second_table where name != NULL then order by score desc
SELECT `score` `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
