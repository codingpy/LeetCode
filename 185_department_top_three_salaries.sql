/*
SELECT d.name AS department,
       e.name AS employee,
       e.salary
  FROM Department AS d
       JOIN Employee AS e
       ON d.id = e.departmentId
 WHERE (SELECT COUNT(DISTINCT salary)
          FROM Employee
         WHERE e.departmentId = departmentId
           AND e.salary < salary) < 3;

SELECT d.name AS department,
       e.name AS employee,
       e.salary
  FROM Department AS d
       JOIN (SELECT e1.*
               FROM Employee AS e1,
                    Employee AS e2
              WHERE e1.departmentId = e2.departmentId
                AND e1.salary <= e2.salary
              GROUP BY e1.id
             HAVING COUNT(DISTINCT e2.salary) <= 3) AS e
       ON d.id = e.departmentId;
*/

SELECT d.name AS department,
       e.name AS employee,
       e.salary
  FROM Department AS d
       JOIN (SELECT *,
                    DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS `rank`
               FROM Employee) AS e
       ON d.id = e.departmentId
 WHERE `rank` <= 3;
