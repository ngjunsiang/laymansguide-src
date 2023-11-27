[**Previously:**](https://buttondown.email/laymansguide/archive/) SQL queries let you join multiple tables based on specified conditions using the JOIN keyword. This enables crafting complex queries to return only the specific data that is required.

SQL databases are really powerful; this is usually a good thing since it allows developers to do amazing things with the data inside. But it can also lead to disastrous consequences in the unsupervised hands of inexperienced developers. And matters can be even worse if these powers are not carefully granted. A malicious actor could “borrow” these powers to wreak havoc on the database!

![XKCD comic: Exploits of a Mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)<br/>
<small>[Relevant xkcd comic](https://xkcd.com/327/)</small>

## Adding data to an SQL database

Adding data to an SQL database is easy. If our `Customer` table looks like this (from [Issue 84](https://buttondown.email/laymansguide/archive/lmg-s7-issue-84-join-supercharged-vlookup/)):

![Screenshot of a Customer data table, with custID, custName, custEmail, and custContact columns.](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season7/issue084/issue084_01.png)

The relevant SQL query to add another customer is:

```
INSERT INTO Customer
VALUES (Ernest, ernest@lmn.com, 57564986)
```

What could go wrong?

## Interacting with an SQL database

The most direct way of managing and interacting with a database is through its commandline tool. Needless to say, this is not how you would want your users using it. It’s just a terrible user experience, and gives them *waaaay* too much power.

So we usually design a frontend—an app, webpage, or database form—that formats and lays out the data nicely for them, and limits the things they can do to the data. This frontend will usually only allow users to edit or delete existing data, and add new data. Then it constructs an SQL query to be sent to the database. The code to do this might look like the following:

```
custName = request.form['custName']
custEmail = request.form['custEmail']
custContact = request.form['custContact']
sql.execute(f'INSERT INTO Customer VALUES ({custName}, {custEmail}, {custContact})')
```

This code naïvely inserts data from the submitted form into the database without any checks. That’s not smart; the contact number might have the wrong number of digits, the email might not even have an '@', and people often type the wrong things in the wrong fields.

What else could go wrong?

## SQL Injections: sending SQL commands through an unsecured form

A malicious/clever user might attempt to submit the following form data:

Customer Name: Ernest
Customer Email: ernest@lmn.com
Customer Contact: 10); DROP TABLE Customers--

Why would they do that? When inserted into the template above, the full SQL query becomes:

```
INSERT INTO Customer VALUES (Ernest, ernest@lmn.com, 10); DROP TABLE Customers--)
```

Two things to explain:
- the semicolon (`;`) indicates the end of an SQL query. It is used to write two or more queries in one line.
- The database ignores everything after the `--`. It is a useful way to add comments to SQL queries (for human consumption) ... or to make the database ignore invalid syntax (such as the standalone `)`), which is what happens in this case.

So the database ends up executing this:

```
INSERT INTO Customer VALUES (Ernest, ernest@lmn.com, 10);
DROP TABLE Customers
```

Goodbye, `Customer` table ...

## Data leakage through SQL injections

This app is probably going to have some kind of search or filtering feature, where we enter a name to search for and get results that match. If we were searching for a user named George, an inexperienced developer might send this as the SQL query:

```
SELECT * FROM Customer WHERE custName = George
```

If I submit the following in the search box:

Customer Name: George OR 1=1

It might get naïvely substituted to form the following query:

```
SELECT * FROM Customer WHERE custName = George OR 1=1
```

The database will attempt to parse this, and come across `custName = George OR 1=1`. It gets interpreted as “return all results from `Customer` table where the `custName` column matches the result of `George OR 1=1`”.

It will then attempt to evaluate `George OR 1=1`. By the unintuitive reasoning of computer logic, this always evaluates to True, and results in the database returning ... all the rows in `Customer`.

## Conclusion

If you’re going to use a database with a frontend, get an experienced developer to do it. If all you have are inexperienced developers, send them for the appropriate training. If you don’t have developers, use an established product over an untested one. If in doubt, find someone with the relevant credentials to ask for advice.

**Issue summary:** Forms that naïvely inject user-submitted data into a SQL query template may end up sending valid (but otherwise unathorised) SQL commands to the database, with disastrous consequences.

This would have been 3–5 times as long if I had started going into some basic ways to prevent this kind of mistake. Fortunately, this is just a layman’s guide, and I can foist that responsibility off to the rest of the internet.

On a serious note, database security is a whole field of study. If you are using a database for enterprise purposes, please give database security the resources it needs; there are just so many ways that things can go wrong!

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 86: Distributed databases

So far, we have been assuming that the database runs from a single computer, and all its data is stored on one as well. What happens when it outgrows this single computer? Why, it then gets transmitted and infects another computer ... just kidding, we then have to spread that database over two or more computers. And keep them constantly synchronised. If that sounds like a pain, you are exactly right! More on this next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
