[**Previously:**](https://buttondown.email/laymansguide/archive/) Structured Query Language (SQL) is a computer language for managing data in databases. It has keywords and keyphrases that let you filter rows and columns, group and order data, perform basic arithmetic on data, and more. It is complex and powerful, but astute and efficient requires specialised training.

## VLOOKUP: The bread-and-butter of spreadsheets

If I have a customer data table that looks like this:



And a sales data table that looks like this:



I could add a column to the sales table that *looks up* the `customerID`, and inserts the `CustomerName` info from the same column. This feature of spreadsheets is known as VLOOKUP (vertical lookup). There is an equivalent feature for columns known as HLOOKUP (horizontal lookup) that looks up info in a row and inserts data from the same column, but it is not as popular. So the VLOOKUP name has stuck ever since.

What if you needed to insert more than one column? What if you need to “join” two or more tables? Your spreadsheet would soon be filled with VLOOKUP cells, and this really slows down the performance of the spreadsheet. This method is not suitable for data involving millions of rows, for sure.

## SQL JOIN: VLOOKUP on steroids

In a database, there is no “standard view” of the data. All data you want to see has to be retrieved with a **query**. So it makes no sense to require cells filled with VLOOKUPS; we just need to figure out how to do the equivalent in a query.

the keyword we are looking for is called JOIN.

To join the `Customer` and `Sales` data so that we get the sales data along with `CustomerName` and `CustomerContact`, we would write a SQL query like this:

`SELECT * FROM Sales JOIN Customer ON CustomerName,CustomerContact ORDER BY Sales.Date`



**Issue summary:**

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 85: Database security on the Internet



**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
