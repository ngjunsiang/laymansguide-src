Title: Issue 80: Indexing
Date: 2020-07-18 08:00
Tags: 
Category: Season 07
Slug: issue080
Author: J S Ng
Summary: 
Modified: 2020-07-18 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Comma-separated value (CSV) files store all data in text form. Within each row, a separator divides each chunk of data, and rows are separated by a line delimiter. To keep the data compact and read it more quickly, we have to decide beforehand what *data type* each chunk should be, and how much space it is allowed to take up. Such a data form can no longer be opened in a simple text editor program like Notepad.

Last issue, we were still looking at how to speed up a text-based data storage solution. When we finished, we had a program that could skip the process of reading every single line and counting line breaks, but it could no longer be opened in Notepad. (That’s not a big loss really; Notepad can’t really handle text files larger than 0.5–1 GB anyway …)

No matter, so long as our program does not need to read in everything at a go!

## The search problem

Right now, our data is still stored in a huge, continuous text block. Retrieving information from this block is easy if you already know the row number you want; our data program can quickly calculate the required row and jump to its starting byte.

Most if not all of the time, you would have no idea which row to retrieve, although you might know something to tell you what data to look for—a name, a date of birth, etc. You would need to **search** for this row. And blocks are just not really optimised for such operations.

Nonetheless, this is not a new challenge. Paper books are often dense and long, especially textbooks. If you wanted to find a passage in there to quote, you would not be flipping through more than 800 pages and scanning paragraph by paragraph just to find it again! You would just flip to the **index**, look up the term you were hoping to find, and simply check those page references.

Why not do that here?

## Indexes

To create an index, we would need to create another block of data. This data block would contain select pieces of data from our table for indexing—names, dates, or other select pieces of data from our table—along with the corresponding row number(s) where they are found.

Yes, that would take up more space, but it would speed up the search immensely, and that is often a worthy tradeoff. This index would be stored together with the table in our database. When the database is opened, this index would be read into memory, because accessing memory is much faster than accessing physical storage ([Issue 57]({filename}/season05/issue057/issue057.md))). Our database would use it to look up the row number of the record containing the name we want, and retrieve it with the row number much more quickly than a row-by-row lookup could.

## Tradeoffs

You can see how an index would greatly speed up searches, which do not modify the database. But what if we need to store data?

Each row we add to the database would necessitate updating the index. Instead of updating one table with our original database format, we now have two tables to update; that is definitely slower. You would not want to include an index for tables that are often written to.

Now that creates a conundrum for us: if I have customer records, should I add an index, or not? I would often have to search these records for a customer’s information, but I would also be adding to this information often. So it looks like indexes would greatly speed up the lookup, but slow down the adding of records.

I’ll examine this issue next week with **data normalisation**.

**Issue summary:** An index is a separate table containing key terms in the database (usually names, IDs, or some other key identifier), alongside the row numbers where they are found. An index greatly speeds up row lookups, but slows down the writing of new rows.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 81: Data Normalisation

In a spreadsheet, we sometimes love to split a page into multiple tables, with lovely table labels and such. With our database now optimised for fast access with constant-width rows and specific data types, we can no longer do that.

How should we organise our data then? More on this in the next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
