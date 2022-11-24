/*
SELECT DISTINCT l1.num AS consecutiveNums
  FROM Logs AS l1,
       Logs AS l2,
       Logs AS l3
 WHERE l1.id = l2.id - 1
   AND l1.id = l3.id - 2
   AND l1.num = l2.num
   AND l1.num = l3.num;
*/

SELECT DISTINCT num AS consecutiveNums
  FROM (SELECT *,
               LEAD(num, 1) OVER() AS num1,
               LEAD(num, 2) OVER() AS num2
          FROM Logs) AS t
 WHERE num = num1
   AND num = num2;
