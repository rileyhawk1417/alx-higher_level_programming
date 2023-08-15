-- Select name, score from second table where score >=10 then order by descent
SELECT `name`, `score`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
