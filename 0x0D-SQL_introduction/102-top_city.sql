-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

WITH jul_aug AS (
	SELECT *
	FROM `temperatures`
	WHERE `month` BETWEEN 7 AND 8
) SELECT `city`, AVG(`value`) AS avg_temp
FROM jul_aug
GROUP BY `city`
ORDER BY avg_temp DESC
LIMIT 3;
