/*
SELECT user_id,
       MAX(time_stamp) AS last_stamp
  FROM logins
 WHERE YEAR(time_stamp) = 2020
 GROUP BY user_id;
*/

SELECT user_id,
       MAX(time_stamp) AS last_stamp
  FROM logins
 WHERE time_stamp BETWEEN '2020-01-01' AND '2021-01-01'
 GROUP BY user_id;
