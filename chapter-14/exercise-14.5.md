### 14.5 Denormalization

#### What is denormalization? Explain the pros and cons

**Solution**

Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database.

By contrast, in a traditional normalized database, we store data in separate logical tables and attempt to minimize redundant data. We may strive to have only one copy of each piece of data in the database.

For example, in a normalized database, we might have a Courses table and a Teachers table. Each entry in Courses would store the teacherID for a Course but not the teacherName. When we need to retrieve a list of all Courses with the Teacher name, we would do a join between these two tables.

In some ways, this is great; if a teacher changes his or her name, we only have to update the name in one place.

The drawback, however, is that if the tables are large, we may spend an unnecessarily long time doing joins on tables.

Denormalization, then, strikes a different compromise. Under denormalization, we decide that we're okay with some redundancy and some extra effort to update the database in order to get the efficiency advan­ tages of fewer joins.

**Cons of Denormalization**

- Updates and inserts are more expensive.
- Denormalization can make update and insert code harder to write.
- Data may be inconsistent. Which is the "correct" value for a piece of data?
- Data redundancy necessitates more storage.

**Pros of Denormalization**

- Retrieving data is faster since we do fewer joins.

- Queries to retrieve can be simpler (and therefore less likely to have bugs), since we need to look at fewer tables.

