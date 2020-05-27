[**Previously:**](https://buttondown.email/laymansguide/archive/) Modern webpages rely on many third-party resources for their functionality. Blocking access to some domains may cause these webpages to break and stop working.

We start a new season this issue, and now I circle back to the theme of data again. In Season 4, I laid out the broad categories of data, and showed how these basic data types get put together into more complex containers, such as video and documents. Let’s take it one step further.

> **base**
>
> *noun*  
  the bottom of something considered as its support: [foundation]

Whatever you do, I doubt your entire life can fit into a single document. Heck, even your household data, your work data … whatever it is, it is probably too complex and varied to fit into a single container. So many numbers and paragraphs, related in some ways, all interconnected … how to make sense of it?

We need a foundation for all this data, a base on which we can build our lives and our worlds. We need **databases**.

Let’s start from square 1: plain text.

## Text files and CSV

Starting simple, let’s try to put our data into a text file. Inside the computer, a text file is just a long string of text:

    This is the first line\nThis is the second line\nThis is the third line\n…

That `\n`? That is the newline character ([Issue 41](https://buttondown.email/laymansguide/archive/lmg-s4-issue-41-ascii-the-typewriter-digitised/)), an unprintable code that tells the computer “the subsequent parts go on a new line”. Without it, Everything would just be one long, continuous string. The newline character determines the limits of each line; it **delimits** the line. `\n`, the newline character, is therefore a line **delimiter**.

Not all our data is just a single line like that. In spreadsheets, for example, we want multiple data types in the same row. How do we get the computer to understand that these data are not one big bundle, but separate pieces? We need a **separator**. Commonly, commas are used to separate data, like this:

    5,bubbleSort,1.734122735215351e-06
    5,insertionSort,1.0771698807366193e-06
    5,mergeSort,5.6086346949450675e-06
    5,quickSort,4.135697910096496e-06

That’s some data I was compiling to compare different sorting methods. The first piece of data, a number, represents how many numbers I was sorting. The second piece of data is the sorting method, and the third piece of data is the time taken. and they are separated by commas.

This format is known as **comma-separated values**, and referred to by the acronym **CSV**.

## Searching through data in CSV

In [Issue 41](https://buttondown.email/laymansguide/archive/lmg-s4-issue-41-ascii-the-typewriter-digitised/), I mentioned that each character takes up a standard number of bytes (1 byte, in the case of the characters on your keyboard; anything outside of that, it’s complicated). That makes it easy for the computer to retrieve characters. First character, first byte. 100th character, 100th byte.

What about the 5th row? Which byte is that?

Now the computer has to start searching from byte 1 all the way, count the number of newlines (`\n`), and after the 4th newline it knows “this is the fifth line”. That works for a small amount of data, perhaps even for a household, but for businesses with thousands of customers and millions, even billions of lines of data, this is unworkable. What can we do about this?

If you recognise the themes that have been recurring so far, you probably know it subconsciously: we need *standardisation*.

If we could decide beforehand—a big *IF*, but possible—how many data pieces each row should have, and the largest number of bytes each data piece will take up, things will be much easier. If each row only has 3 pieces of data, and each piece of data takes up no more than 8 bytes (64 bits), then each row takes up 28 bytes. The 5th row starts from byte 113.

This process is much faster for a computer. It does not need to read every single byte and count newlines anymore; it can just jump to the position of byte 113 and start reading from there.

## Reducing data size

One more problem to resolve: 112 bytes for 4 rows is a lot of data! A chunk of data in text form, such as “`$1,234.56`” is 9 characters, which means 9 bytes. If we could somehow *standardise* this data type (say, let’s just call it *currency*), and reduce it to just the number form `1234.56`, we could store it in just 2 bytes! That’s much fewer bytes to retrieve, store, and transfer.

The tradeoff is that now we can no longer just open that file in Notepad to peek at the data. We would need a program that:

- remembers how many bytes each row and piece of data should take up,
- remembers what type each piece of data is.

This program will figure out where to start reading the file from, retrieve the data we want, and return it. Compared to managing data in CSV, the data will be more compact, and the program will be faster. And we would have taken one step away from plain text files, towards a full database.

**Issue summary:** Comma-separated value (CSV) files store all data in text form. Within each row, a separator divides each chunk of data, and rows are separated by a line delimiter. To keep the data compact and read it more quickly, we have to decide beforehand what *data type* each chunk should be, and how much space it is allowed to take up. Such a data form can no longer be opened in a simple text editor program like Notepad.

For tech junkies and programmers, it is easy to get into the blind pursuit of performance. I wanted this issue to start right, by demonstrating the tradeoffs involved in increasing performance. We started from a data format so simple it can be opened in Notepad and read by a human, to a format that needs a program to read.

At least this program is simple to write; I could do it in less than fifty lines of Python code. Let’s look at more tradeoffs in the next issue.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 80: From blobs to trees

We are so used to seeing data in a single **blob**—as a dense spreadsheet table, as densely packed lines of text, etc—that it is difficult to see it as a loosely organised tree structure.

But in our daily lives, that is much more commonly the way data is organised. Data in organisations is never all put in a single document or place; it is loosely spread across departments, each of which manage a portion of it, and these departments send information updates to each other to update their separate sections.

In the next issue, I’ll apply this idea to the way computers manage information.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
