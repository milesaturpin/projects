/*
Enter your query here.
*/

SELECT Department.NAME, COALESCE(COUNT(Department.NAME),0) AS Cnt
FROM Employee RIGHT OUTER JOIN Department 
GROUP BY Department.NAME
ORDER BY Cnt DESC, Department.NAME ASC;