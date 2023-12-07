Title: Issue 107: The challenges of storage
Date: 2021-02-13 08:00
Tags: 
Category: Season 9
Slug: issue107
Author: J S Ng
Summary: 
Modified: 2021-02-13 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) A hard disk is organised into sectors, which are the smallest unit of storage. The OS’s filesystem determines how and where to store each file on the hard disk. The filesystem manages the file metadata in a file table, separate from the actual contents of the file.

Last issue I painted the picture of a warehouse, where cargo gets stored in racks, their contents and details are stored in the file table (in the warehouse office), and we can easily look up the details of each shipment of cargo without having to inspect rack by rack.

Let’s screw things up here, shall we?

## Read/write failure

As mechanical devices, hard disks are prone to failure; I’ll go into detail why in a future season on hardware. Remember that when this hard drive is housed in a computer, that computer can get disturbed by shocks or jolts. If it is housed in an external USB enclosure, sometimes we do terrible things to that enclosure ... like when we drop them (usually accidentally 😬).

This is like the warehouse experiencing an earthquake. Sometimes, a small earthquake may be uneventful ... other times, we might even get away with a moderate earthquake, if nothing is happening in the warehouse. But if it happens while a forklift is carrying out a precarious loading operation ... 🙈

Well, that’s terrible. We’ll have to write off that shipment. Luckily, we can analogy here; data can always be re-copied again. The problem is ... when a shipment comes in, we have to load the shipment onto the rack, *and* update the file table, so that its contents match whatever is on the racks. Which should we do first? If the loading is uneventful, it doesn’t really matter; after 5 minutes or so, both the file table and the racks will be in sync. But if the earthquake happens during this loading, they won’t be!

We don’t need an earthquake to screw things up. Remember that a hard drive, or even a flash drive, needs power to run. When we unplug a hard disk or flash drive while it is still operating, it’s like cutting power to the entire warehouse (including its forklifts) at the same time. If nothing is happening in the warehouse, it is safe to do so. But if there are ongoing operations, well you don’t need me to tell you that’s not a good idea.

## Reads are usually safe

Okay, we’ll have to step away from the warehouse analogy for a bit when we talk about reading data from a hard drive; this is usually safe, because unlike cargo, reading data does not destroy the existing copy. We can mount a filesystem (i.e. gain access to it) for reading only, which will protect it from accidentally having its data overwritten.

It is the writes that always get us. When a write operation does not go smoothly, the result is usually filesystem corruption; the file table is no longer up to date, or worse, some parts of it might be improperly written, resulting in the company no longer knowing what is on the warehouse racks.

**Issue summary:** When write operations are interrupted prematurely, filesystem corruption often results.

There are two ways we can try to get data onto the disk (get cargo into the warehouse): Write the data first, then update the file table, or vice-versa. Which way is better? We’ll compare the pros and cons in the next issue.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 108: Safeguarding data operations

That remove-safely thing we all hate to do when we unplug our hard drives? Yeah I’m getting to that part.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- why does computer memory exist when apps can read directly from the hard disk? [Issue 105]
