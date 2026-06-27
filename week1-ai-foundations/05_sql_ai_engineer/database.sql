CREATE DATABASE Students;


USE Students;


CREATE TABLE students(


id INT PRIMARY KEY,


name VARCHAR(50),

python INT,

math INT

);


INSERT INTO students VALUES

(1,'teja',50,75),

(2,'sabareesh',80,95),

(3,'vibhas',90,98);
SELECT * FROM students;