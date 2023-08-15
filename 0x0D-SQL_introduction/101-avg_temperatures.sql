-- Select city and average temp values. Then group by city & order by avg_temp in descent
SELECT `city`, AVG(`value`)
AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC; 
