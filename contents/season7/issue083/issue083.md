[**Previously:**](https://buttondown.email/laymansguide/archive/) A database system follows rules that enable multiple users to send commands to the database at the same time. The system attempts to execute each action one at a time, locking data that is in use by other users, and ensuring that each user does not carry out actions that they are not permitted to. Such systems are better able to prevent data corruption compared to a text-based system.

Have you experienced the pain of having really huge tables in your spreadsheet, sometimes spanning more than a hundred columns? Then you might know how painful it can be trying to filter data from it, e.g. if your boss just wants a few columns of info from certain rows. Like if he asks for the performance numbers of employees who are up for promotion.

In a spreadsheet, you would have to apply filters for `nextPromoYear` to only show the appropriate rows, then you'll have to hide all the other irrelevant columns. Or you'd just copy all more-than-a-hundred columns for those rows into another new spreadsheet, and manually delete the unnecessary columns.

Database designers don’t want to to do that. You should be able to ask the database to do this querying and filtering for you, and return you only the data you want. But how would that be designed?

## Structured Query Language: the universal database language

Structured Query Language (SQL) is another computer language designed to manage data in databases. It reads *almost* like English, but more logical and less poetic. It has its own syntax and grammar, which are not the same as in English. And sending a proper SQL query to any database that supports it will get you what you want.

Here’s what an SQL query for the above info might look like:

    SELECT employeeName, teamName, salesCount, salesTotal FROM SalesData
    WHERE nextPromoYear = 2020
    GROUP BY teamName
    ORDER BY salesTotal;

- The `SELECT` keyword lets you filter only the columns you want `FROM` a table
- The `WHERE` keyword lets you filter only the rows you want, based on one or more criteria
- The `GROUP BY` keyphrase lets you group the returned data based on values in a column
- The `ORDER BY` keyphrase lets you sort the returned results according to values in a column

## A database has no “main view”

One difficulty many people have in “upgrading” from a spreadsheet mindset to a database mindset is that they expect to have a “main spreadsheet” where (almost) all the data lives, and where sub-spreadsheets pull data from. In a database, all data lives in separate tables, and are joined only when a query is executed. The only way to get data from a database is to use queries!

Most websites or software you are using which retrieves data for you usually end up executing one or more queries such as the above to get that data. And the job of the database software is to interpret such commands, pull the data from the various tables together, collate it correctly, and send it to you.

## A database can give you almost exactly what you want

By using these and many other keywords and keyphrases, it is possible to put together a query that gives you only the data you want. SQL has arithmetic functions such as count, average, sum, and it can even return only unique values.

The tradeoff is that you have to learn another language, and use it regularly enough to understand the ins and outs. This is why every big corporation has a data team that can do this!

**Issue summary:** Structured Query Language (SQL) is a computer language for managing data in databases. It has keywords and keyphrases that let you filter rows and columns, group and order data, perform basic arithmetic on data, and more. It is complex and powerful, but using it in an astute and efficient manner requires specialised training.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 84: JOIN – supercharged VLOOKUP

I haven’t even touched on SQL’s really powerful features yet. Filtering data from a table is fine, but if my data is spread across many tables, how do I pull that data together? Excel folks have a command they rely on heavily to do this, and it is called `VLOOKUP`. I’ll show you the SQL version next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
