SELECT tn.person_emp_length, tn.person_home_ownership, tn.loan_number, tn.person_age,
    CASE 
        WHEN tn.person_age >= 65 THEN 'Seniors'
        WHEN tn.person_age >= 60 THEN 'Sixties'
        WHEN tn.person_age >= 50 THEN 'Fifties'
        WHEN tn.person_age >= 40 THEN 'Forties'
        WHEN tn.person_age >= 30 THEN 'Thirties'
        WHEN tn.person_age >= 20 THEN 'Twenties'
        WHEN tn.person_age >= 12 THEN 'Teens'
        ELSE 'Kids'
    END as salary_category
FROM table_name tn;