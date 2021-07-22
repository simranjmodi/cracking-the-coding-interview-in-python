### 14.4 Joins

#### What are the different types of joins? Explain how they differ and why certain types are better in certain situations.

**Solution**

JOIN is used to combine the results of two tables. To perform a JOIN, each of the tables must have at least one field that will be used to find matching records from the other table. The join type defines which records will go into the result set.

- INNER JOIN: The result set would only contain the data where the criteria match.
- OUTER JOIN: The result set will always contain the results of INNER JOIN, but it may also contain some records that have no matching record in the other table. OUTER JOINs are divided into the following subtypes:
- 1. LEFT OUTER JOIN or simply LEFT JOIN: The result will contain all records from the left table. If no matching records were found in the right table, then its fields will contain the NULL values. 
- 2. RIGHT OUTER JOIN or simply RIGHT JOIN: This type of join is the opposite of LEFT JOIN. It will contain every record from the right table; the missing fields from the left table will be NULL. 
- 3. FULL OUTER JOIN: THis type of join combines the results of the LEFT and RIGHT JOINS. All records from both tables will be included in the result set, regardless of whether or not a matching record exists in the other table. If no matching record was found, then the corresponding result fields will have a NULL value.  
