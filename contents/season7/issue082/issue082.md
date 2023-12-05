[**Previously:**](https://buttondown.email/laymansguide/archive/) Putting all data into one table results in unnecessary duplication of data. Making data atomic by splitting it up into multiple tables makes the data easier to work with, but requires multiple lookups and joins to get the required data. A standard database language, SQL, makes it possible to write queries that are supported by multiple databases.

This issue is going to be a short one, because it is simple enough to explain :)

> “The action can’t be completed because the file is open. Close the file and try again.”

This happens in File Explorer because the operating system treats a text file as a single block of data. When a user opens this file, they do not expect data inside to change. To prevent other users inadvertently modifying it, the operating system “locks” the file, preventing any changes—including deletion!

How do we resolve this with a database? In the previous issue ([Issue 81]({filename}/season7/issue081/issue081.md

## Locking specific data

Now that the data is atomic, the database is better able to figure out which data needs to be locked. If a user is requesting data from a particular table and from certain rows only, we do not need to lock the entire database and prevent other users from accessing it. Such systems are called row-locking systems, and some databases (but not all) support this feature.

## Action deconflicting

When multiple users access a database and attempt to write data to it at the same time, the database takes these requests and puts them in a queue, processing them one by one so that no two conflicting actions end up causing the data to be corrupted.

But sometimes, conflicting actions can end up getting queued. For instance, User 1 might send a command to delete a table while User 2 send a command to retrieve data from that table (because it had not been deleted at the point when User 2 accessed it). User 1’s command gets through first and deletes the table, and when the database reaches User 2’s command, it is no longer able to execute it. What happens then?

Well, that’s when the database throws an error. A database system is able to detect actions whose logic conflict with other actions. With our previous text-based system, even with the table gone, the program could still continue to search for results, and finding none, return empty data instead of alerting the user.


**Issue summary:** A database system follows rules that enable multiple users to send commands to the database at the same time. The system attempts to execute each action one at a time, locking data that is in use by other users, and ensuring that each user does not carry out actions that they are not permitted to. Such systems are better able to prevent data corruption compared to a text-based system.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 83: Structured Query Language

If you have an Excel maven in your workplace who writes `VLOOKUP`s, `INDEX-MATCH`s and other chained functions with ease, you will know how spreadsheets can do downright amazing things. But wait till you see Structured Query Language (SQL); it will blow your mind! It *almost* looks like Excel code, except with fewer nested parentheses, and reads a little (deceptively) more like English. I’ll show you next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
