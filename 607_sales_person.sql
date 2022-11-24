/*
SELECT name
  FROM SalesPerson
 WHERE sales_id NOT IN
       (SELECT o.sales_id
          FROM Orders AS o
               JOIN Company AS c
               USING (com_id)
         WHERE c.name = 'RED');
*/

SELECT sp.name
  FROM Orders AS o
       JOIN Company AS c
       ON o.com_id = c.com_id
          AND c.name = 'RED'

       RIGHT JOIN SalesPerson AS sp
       ON o.sales_id = sp.sales_id

 WHERE o.order_id IS NULL;
