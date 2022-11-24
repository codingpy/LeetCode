SELECT t.request_at AS day,
       ROUND(AVG(t.status <> 'completed'), 2) AS `cancellation rate`
  FROM trips AS t
       JOIN users AS u1
       ON t.client_id = u1.users_id
          AND u1.banned = 'No'

       JOIN users AS u2
       ON t.driver_id = u2.users_id
          AND u2.banned = 'No'
 WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
 GROUP BY t.request_at;
