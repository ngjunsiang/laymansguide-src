[**Previously:**](https://buttondown.email/laymansguide/archive/) To increase the performance of a distributed database, we can scale up/scale vertically by increasing the computers’ performance, or scale out/scale horizontally by adding more computers. Distributed databases can only prioritise two of the following three factors: consistency, availability, partitioning (CAP theorem).

I’ve already discussed one big strength of relational databases in [Issue 84](https://buttondown.email/laymansguide/archive/lmg-s7-issue-84-join-supercharged-vlookup/) when I illustrated how the JOIN keyword, one of many SQL commands ([Issue 83](https://buttondown.email/laymansguide/archive/lmg-s7-issue-83-structured-query-language/)), can join our data from multiple tables into a single view. This is where we look under the surface to see what makes that possible.

## Linking tables through foreign keys

From [Issue 84](https://buttondown.email/laymansguide/archive/lmg-s7-issue-84-join-supercharged-vlookup/):

> To join the `Customer` and `Sales` data so that we get the sales data along with `custName`, we would write a SQL query like this:
>
> ```
> SELECT salesID, orderDate, custID FROM Sales
> JOIN Customer ON Sales.custID = Customer.custID
> ```
>
> Here, `Sales.custID` refers to the `custID` of the `Sales` table, while `Customer.custID` refers to the `custID` of the `Customer` table. This query effectively says “select the `salesID`, `orderDate`, and `custID` columns from `Sales` table, and add data from the `Customer` table where the `custID` column matches”. This will return:
>
> ![Screenshot of an INNER JOIN operation between the Sales and Customer data tables, merged using custID values.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_04.png)

Did you catch the fact that there were actually *two* `custID` columns? One in the `Sales` table, and one in the `Customer` table ... by linking two tables like that, we actually introduce a point of potential breakage.

Suppose one day, a customer goes out of business, or changes name, and the corresponding `Customer` entry gets deleted. Now if we accidentally attempt to retrieve `Sales` to that customer, the SQL command will fail because it is unable to find the entry.

We can protect ourselves from this kind of error by declaring `Sales.custID` as a **foreign key** in `Customer`, thus informing the database that `Sales.custID` is actually a column from `Customer`. If we attempt to delete that customer again, the database will help to check if that entry is referenced by other tables as a foreign key. Entries can only be deleted if they are not referenced by other entries.

These and other constraints allow us to protect ourselves from inadvertent harm, but over time, they accumulate and make a relational database very hard to modify. Database administrators will tell you to think about your database tables in advance, as even attempting to add a column or change a column type is going to be a pain in future!

## The tradeoff: downtime for database maintenance and migrations

To modify a relational database, we have to shut it down[^1], and **migrate** the database from the old schema to the new schema. In essence, we are exporting our data and re-importing it again. Attempting to migrate while the database is active—known as a **live migration**—is strongly discouraged, as changing a database while a migration is in progress can introduce data inconsistency; a real headache with constraints!

[^1]: There are ways to avoid this, but I’ll let a **real** database administrator tell you about how to make it happen.

Relational databases can also develop problems that require them to be shut down and rectified. It’s the tradeoff for having a consistent and structured way to store our data, and automated rules to enforce this structure.

## Relational databases: excellent for predictable data needs

If you don’t expect to be changing your database schema often, or if you are able to design the schema to minimise such migrations, relational databases can be quite excellent for your needs. Please consult a professional database engineer if you are planning to use a database for your business needs.

**Issue summary:** Relational databases are designed to maintain a well-structured set of data tables through constraint rules. This makes them very useful for preventing accidental inconsistencies in data, but make any changes to the data schema difficult to implement. Changing from one schema to another involves downtime and a migration.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 88: Document Databases

Relational databases work well for data that we can imagine as an Excel table. But often, we have data that might not share the same set of properties, or might not have a predictable structure (such as online collaboration data). Such data is more intuitively imagined as a set of documents than as a set of tables. What do databases that encourage a document-based model of data look like?

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
