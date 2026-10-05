# Write your MySQL query statement below
SELECT DISTINCT v1.author_id AS id
FROM Views v1
    INNER JOIN Views v2 ON v1.author_id = v2.viewer_id
WHERE v1.author_id = v2.author_id
ORDER BY id