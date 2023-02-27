-- displays the average temperature(Fahreheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp
FORM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
