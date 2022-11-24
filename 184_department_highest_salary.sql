SELECT d.name AS department,
       e.name AS employee,
       e.salary
  FROM Department AS d
       JOIN Employee AS e
       ON d.id = e.departmentId
 WHERE (e.departmentId, e.salary) IN
       (SELECT departmentId, MAX(salary)
          FROM Employee
         GROUP BY departmentId);
