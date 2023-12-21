Title: Issue 108: Safeguarding data operations
Date: 2021-02-20 08:00
Tags: 
Category: Season 09
Slug: issue108
Author: J S Ng
Summary: Safe writes ensure that all the data is written to disk sectors properly first before updating the file table. The result is that write operations take a longer time to complete.
Modified: 2021-02-20 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) When write operations are interrupted prematurely, filesystem corruption often results.

When a batch of data (shipment of cargo)) arrives at our warehouse, there are two things that need doing:

1) The data needs to be written into sectors (the smallest unit of storage that the disk handles),
2) The file table needs to be updated.

## Writing data the safe way

If the write operation gets interrupted, it is preferable that our file table is not updated; this way, we will not find any reference to the data in the file table, and we can attempt the write operation again.

This will appear strange in a warehouse analogy; the cargo, damaged or intact, is still occupying space on the racks! But remember that when we are talking about a hard disk storing data, there is no *physical cargo*; the data exists as a specific arrangement of electrons/atoms. We can override the existing arrangement of electrons/atoms without having to reset it first.

## Drawbacks of safe writing

This way of storing data first before updating the file table is advantageous in its security; if the write operation is interrupted halfway, we are less likely to suffer filesystem corruption.

But for large batches of data (or large shipments of cargo), this means a long wait ... and in the meantime, nothing else can happen! Hard drives only have one writing needle, which is like a warehouse only having one forklift. If you have other applications waiting for that file (similar to other employees waiting for the file record to appear in the file table), they will be twiddling their thumbs until the last sector of data is written, the last pallet of cargo loaded onto the racks.

But this is the *right thing to do*, isn’t it? It doesn’t matter; [Windows Vista did it this way](https://blog.codinghorror.com/actual-performance-perceived-performance/), waiting for write operations to complete before updating the file metadata in the file table, and the result is that *people complained that it was slower*. People do not like things slow!

Why did Windows XP feel faster, then? Because it did it the other way round!

**Issue summary:** Safe writes ensure that all the data is written to disk sectors properly first before updating the file table. The result is that write operations take a longer time to complete.

Actually, Windows 10 uses a system similar to this for mounting portable devices (USB hard drives, flash drives, etc) by default. They sped it up in other ways. So if you accidentally unplug a drive before it is completely done writing ... usually it won’t completely screw things up.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 109: Speeding up data operations

If you want, there are settings you can adjust to make Windows 10 access a portable device *the fast way*. I don’t teach it here, because this is not the newsletter for it. But we’ll see how *the fast way* works in the next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- why does computer memory exist when apps can read directly from the hard disk? [Issue 105]
