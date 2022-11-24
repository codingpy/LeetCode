SELECT c.name AS customers
  FROM Customers AS c
       LEFT JOIN Orders AS o
       ON c.id = o.customerId
 WHERE o.id IS NULL;
