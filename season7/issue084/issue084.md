[**Previously:**](https://buttondown.email/laymansguide/archive/) Structured Query Language (SQL) is a computer language for managing data in databases. It has keywords and keyphrases that let you filter rows and columns, group and order data, perform basic arithmetic on data, and more. It is complex and powerful, but astute and efficient requires specialised training.

## VLOOKUP: The bread-and-butter of spreadsheets

If I have a `Customer` data table that looks like this:

![Screenshot of a Customer data table, with custID, custName, custEmail, and custContact columns.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_01.png)

And a `Sales` data table that looks like this:

![Screenshot of a Sales data table, with salesID, orderDate, and custID columns.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_02.png)

I could add a `custName` column to the sales table that *looks up* the `custID`, and inserts the `custName` info from the same row. This feature of spreadsheets is known as **VLOOKUP** (vertical lookup)[^1]. This is what the formula for each cell in `custName` would look like:

[^1]: There is an equivalent feature for columns known as HLOOKUP (horizontal lookup) that looks up info in a row and inserts data from the same column, but it is not as popular. So the VLOOKUP name is more commonly used for this kind of operation.

![Screenshot of a Sales data table, with salesID, orderDate, and custID columns.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_03.png)

Let’s break down each part of that formula:

`=VLOOKUP(C2,Customer!A:D,2)`

This means “in columns **A:D** of the **Customer** table, look for the value from cell **C2** (which is `1`) in the first column, and return the value from the same-row cell in the **2**\nd column.”

What if you needed to insert more than one column? What if you need to “join” two or more tables? Your spreadsheet would soon be filled with VLOOKUP cells, and this really slows down the performance of the spreadsheet. This method is not suitable for data involving millions of rows, for sure.

## SQL JOIN: VLOOKUP on steroids

In a database, there is no “standard view” of the data. All data you want to see has to be retrieved with a **query**. So it makes no sense to require cells filled with VLOOKUPS; we just need to figure out how to do the equivalent in a query. The keyword for that is called **JOIN**.

To join the `Customer` and `Sales` data so that we get the sales data along with `custName`, we would write a SQL query like this:

```
SELECT salesID, orderDate, custID FROM Sales
JOIN Customer ON Sales.custID = Customer.custID
```

Here, `Sales.custID` refers to the `custID` of the `Sales` table, while `Customer.custID` refers to the `custID` of the `Customer` table. This query effectively says “select the `salesID`, `orderDate`, and `custID` columns from `Sales` table, and add data from the `Customer` table where the `custID` column matches”. This will return:

![Screenshot of an INNER JOIN operation between the Sales and Customer data tables, merged using custID values.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_04.png)

That is much easier—once you’ve been trained in SQL syntax—than writing separate VLOOKUP formulas for each column you want, and having the maintain a whole table of formulas!

You can even join more than two tables together with a query like:

```
SELECT salesID, orderDate, custID, invoiceID, Customer.custName, Customer.custContact, invoiceDate, invoiceAmt FROM Sales
JOIN Customer ON Sales.custID = Customer.custID
JOIN Invoice ON Sales.invoiceID = Invoice.invoiceID
```

This is barely scratching the surface of what SQL can do; it has at least 4 types of JOINs, and many more ways of crafting queries to return specifically the data you want.

SQL queries are a whole different way of talking to your computer, and they can be really frustrating to write for people who are new to it. But they are behind many of the interfaces you see, which seem to seamlessly pull data from multiple sources together into a coherent view.

**Issue summary:** SQL queries let you join multiple tables based on specified conditions using the JOIN keyword. This enables crafting complex queries to return only the specific data that is required.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 85: SQL injections

Databases are immensely powerful software systems when it comes to searching for information. One recurring challenge that all admins face is ensuring that only authorised use is permitted; how do we prevent malicious activity from being able to access the database?

Next week, I will introduce a common **vulnerability** that web developers always have to guard against: SQL injection.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
