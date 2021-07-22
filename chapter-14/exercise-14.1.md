### 14.1 Multiple Apartments

#### Write a SQL query to get a list of tenants who are renting more than one apartment. 

**Solution**

<pre>
SELECT TenantName
FROM Tenants
INNER JOIN
    (SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING count(*) > 1) C
ON Tenants.TenantID = C.TenantID
</pre>