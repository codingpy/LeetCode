/*
(SELECT e.employee_id
   FROM employees AS e
        LEFT JOIN salaries AS s
        USING (employee_id)
  WHERE s.employee_id IS NULL)

  UNION

(SELECT s.employee_id
   FROM employees AS e
        RIGHT JOIN salaries AS s
        USING (employee_id)
  WHERE e.employee_id IS NULL)

  ORDER BY employee_id;
*/

SELECT *
  FROM (SELECT employee_id
          FROM employees

         UNION ALL

        SELECT employee_id
          FROM salaries) AS t
 GROUP BY employee_id
HAVING COUNT(*) = 1
 ORDER BY employee_id;
