# Write your MySQL query statement below
SELECT customer_id, COUNT(*) as count_no_trans 
FROM Visits v NATURAL LEFT JOIN Transactions t
WHERE t.transaction_id IS NULL
GROUP BY customer_id