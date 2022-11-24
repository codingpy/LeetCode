/*
DELETE
  FROM person
 WHERE id NOT IN
       (SELECT *
          FROM (SELECT MIN(id)
                  FROM person
                 GROUP BY email) AS t);
*/

DELETE p1
  FROM person AS p1,
       person AS p2
 WHERE p1.email = p2.email
   AND p1.id > p2.id;
