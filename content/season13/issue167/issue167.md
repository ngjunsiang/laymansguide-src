Title: Issue 167: Database fragmentation
Date: 2022-04-09 08:00
Tags: 
Category: Season 13
Slug: lmg-s13-issue-167-database-fragmentation
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) There are easy and quick ways to check the validity of the most common advice for resolving system slowdown. But it still seems to happen even after these tips have been tried.

Last issue, we talked about caches and why they are no longer as effective as a performance-boosting measure.

This issue, let’s look into a solved problem that is not-as-solved on Android: file fragmentation.

## Storage fragmentation on mobile devices

I mentioned in [Issue 119]({filename}/season10/issue119/issue119.md)) that fragmentation is not an issue for faster SSDs; the much lower latency of SSDs makes the retrieval of multiple file chunks from multiple locations trivially easy. But for slower storage devices, whether they are hard disk drives or SSDs over a UFS interface, fragmentation is very real. Unfortunately, its not just a simple matter of defragmenting a disk regularly[^1]. the source of this fragmentation comes from the way apps themselves store data.

[^1]: Defragmentation is discouraged on solid-state devices, as each read/write operation causes the storage medium to degrade. Under typical usage, a solid-state device can be expected to last many years. Defragmentation involves lots of read/write (as you are reading files and storing them elsewhere on the disk), hastens the degradation, and will shorten the lifespan of solid-state devices unnecessarily.

## SQLite, a blessing and a curse

[SQLite](https://sqlite.org/index.html) is a popular file-based relational database ([Issue 87]({filename}/season7/issue087/issue087.md))) used by many Android apps (including WhatsApp!). This means that unlike other databases, which require a separate database program to run, SQLite just requires the programmer to bundle an appropriate library for their programming language instead of running a separate program. It makes management of data much easier for the app developers, and it is also fast—usually.

However, [a 2016 study found that it contributes to fragmentation](https://www.tuxera.com/blog/why-is-my-android-phone-slowing-down/) on the Android filesystem. Even after clearing the app’s data, once SQLite starts storing data again, it tends to store them in many small chunks instead of fewer but larger chunks. On Android devices, which use the slower UFS interface, searching through the database involves reading each database chunk to see if the requested data is there; this gets slower as the database grows, and SQLite adds more chunks to the storage device.

The study ends on a pretty pessimistic note: there doesn’t seem to be any feasible mitigation other than making upstream code changes to SQLite, or designing a different filesystem that overcomes this limitation. But that was five years ago; with any luck some positive developments might have been made into this area. I’m still looking into it!

**Issue summary:** Fragmentation is likely a contributor of system slowdown, particularly for mobile devices: the databases used by most mobile apps tend to store data in many small chunks rather than fewer big chunks, which slows down data search operations. The most effective measure for improving device responsiveness is usually to clear the app cache, so the app does not attempt to read previous data from storage.

That’s all I’ve managed to find out from reading; further research will either involve detailed tinkering and experimentation, or deeper reading, both of which are time-consuming.

Short issue this time, because if I made it any longer I think it would be more technical than I would really like. Enjoy the brain-break!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 168: Search engines

How do search engines ... know everything?
