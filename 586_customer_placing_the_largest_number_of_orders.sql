/*
SELECT customer_number
  FROM orders
 GROUP BY customer_number
 ORDER BY COUNT(*) DESC
 LIMIT 1;

SELECT customer_number
  FROM orders
 GROUP BY customer_number
HAVING COUNT(*) >= ALL (SELECT COUNT(*)
                          FROM orders
                         GROUP BY customer_number);
*/

SELECT customer_number
  FROM (SELECT *,
               RANK() OVER(ORDER BY COUNT(*) DESC) AS `rank`
          FROM orders
         GROUP BY customer_number) AS t
 WHERE `rank` = 1;
