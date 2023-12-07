Title: Issue 109: Speeding up data operations
Date: 2021-02-27 08:00
Tags: 
Category: Season 9
Slug: issue109
Author: J S Ng
Summary: 
Modified: 2021-02-27 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Safe writes ensure that all the data is written to disk sectors properly first before updating the file table. The result is that write operations take a longer time to complete.

If there’s anything to take away from the previous issue, it’s that *doing things the right way takes time*. And sometimes we are okay with taking shortcuts to get something done faster, the *left* way.

## The write cache

If you have a shipment coming in that urgently needs to be dumped into the warehouse quickly (e.g. because the ship needs to leave quickly for another delivery, or to free up space on the docks), how do we speed this up?

What usually happens is the goods will be offloaded onto some empty space **outside the warehouse**. The ship will leave first, and *assume* that the warehouse will be able to get the goods in just fine.

What is the OS equivalent of this? Hard disk writes are actually pretty slow; they can get up to 100 MB/s, but usually hit a sustained speed of 60 MB/s for system disks, and about 20 MB/s over USB. The operating system therefore sets up a “dumping space” in memory; files can be read from other disks at up to 200 MB/s, and written to memory at **a few GB/s**!

This space is known as the **write cache**. (I’ve previously covered the idea of caches in Issues [39]({filename}/season03/issue039/issue039.md)) and [57]({filename}/season05/issue057/issue057.md)), and the write cache works on a similar idea.)

## Speeding up file access ... and its drawbacks

So how do we speed up the process of copying data to a disk? We could dump the data into the write cache (assuming there is enough space), then update the file table first, and let the OS slowly copy the data from the write cache into the disk. Anyone who needs access to the file records will then be able to go about their merry way, and if they need data from the file, they can just copy it from the disk cache instead of the disk. Easy peasy!

This was what happened in Windows XP. File copying appears to be speeded up, and users are happy.

But remember what happens when power to the computer is accidentally cut, or if a program suddenly hangs, or the computer sometimes runs out of memory.

Yup ... it shuts down (or reboots), and the contents of memory are wiped clean. And any data that has not been written to disk is *lost forever*. And ... the file table has **already been updated to look like there is valid data**!

This is when things look really bad.

**Issue summary:** Fast writes dump the data to a write cache (in computer memory), then update the file table to look like the file is already written to disk. However, if power is cut before all data is properly moved from the write cache to disk, the data in memory is lost, and file corruption usually results.

Well okay ... it’s not a lost cause right? Yup, we do have ways to mitigate this kind of damage, and one such way is called a journal.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 110: Safeguarding against data corruption with a journal

Woot, answered another sometime-in-the-future question, albeit in a slightly different fashion from how I thought I would do it.

Next issue, I explain how we can still do things the fast way, *carefully*.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- ~~why does computer memory exist when apps can read directly from the hard disk? [Issue 105]~~
