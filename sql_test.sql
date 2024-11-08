
-- Talk about your SQL experience. What databases have you used? What have you done with them?

-- What's wrong with this query?
SELECT * 
FROM person P 
    JOIN person_location PL 
        ON p.id = pl.person_id
WHERE person = 'Terry'; 


-- What's this called? 
-- Why do this? 
;WITH CTE AS ( 
    SELECT person_name, phone_number
    FROM person
    UNION ALL 
    SELECT person_name, phone_number
    FROM person_location
)
SELECT * 
FROM CTE
WHERE person_name = 'Terry';


--  Write an SQL query to find the average salary in the employees table.

--  How would you find the total number of employees in each department in the employees table?

-- USE PARTITION BY
SELECT 
    department_id, 
    COUNT(*) OVER (PARTITION BY department_id) AS department_count -- What is this doing?
FROM employees;

SELECT 
    department_id, 
    COUNT(*) 
FROM employees
GROUP BY department_id;
