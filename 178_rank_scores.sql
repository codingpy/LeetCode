/*
SELECT s1.score,
       COUNT(DISTINCT s2.score) AS `rank`
  FROM scores AS s1,
       scores AS s2
 WHERE s1.score <= s2.score
 GROUP BY s1.id
 ORDER BY s1.score DESC;
*/

SELECT score,
       DENSE_RANK() OVER(ORDER BY score DESC) AS `rank`
  FROM scores;
