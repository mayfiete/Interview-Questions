
-- Talk about your SQL experience. What databases have you used? What have you done with them?

-- What's wrong with this query?
SELECT * 
FROM person
    JOIN person_location
        ON person.id = person_location.person_id
WHERE person = 'Terry'; 


-- What's this called? 
-- What does CTE stand for? 
-- Why do this? 
;WITH CTE AS ( 
    SELECT person_name, phone_number
    FROM person
    UNION ALL SELECT person_name, phone_number
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
