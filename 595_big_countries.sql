/*
SELECT name, population, area
  FROM world
 WHERE population >= 25000000
    OR area >= 3000000;
*/

(SELECT name, population, area
   FROM world
  WHERE population >= 25000000)

  UNION

(SELECT name, population, area
   FROM world
  WHERE area >= 3000000);
