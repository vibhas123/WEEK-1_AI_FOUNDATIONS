USE Students;


SELECT * FROM students;


SELECT
name,
(python+math)/2 AS average
FROM students;


SELECT *
FROM students
WHERE python > 80;


SELECT *
FROM students
ORDER BY python DESC;