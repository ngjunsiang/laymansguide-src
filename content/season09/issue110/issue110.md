Title: Issue 110: Safeguarding against data corruption with a journal
Date: 2021-03-06 08:00
Tags: 
Category: Season 9
Slug: lmg-s9-issue-110-safeguarding-against-data
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Fast writes dump the data to a write cache (in computer memory), then update the file table to look like the file is already written to disk. However, if power is cut before all data is properly moved from the write cache to disk, the data in memory is lost, and file corruption usually results.

Last issue, I showed how a write cache can “speed up” file write operations by allowing data to be dumped to a write cache in memory first. The OS “completes” the operation, making it look the file has been successfully written to disk, when in actuality parts of it are still in memory waiting to be written. This works fine as long as we don’t suffer catastrophic power loss before everything gets put on disk; once power is cut, all the contents of the write cache in memory are lost!

All right, we are into worst-case scenarios here. How do we recover from something like this?

The first thing we’ll need to know is what had happened; what data made it through and was written, and what data didn’t make it. We need a record of changes to the disk.

## File journals

This record, in a filesystem, is called a journal. Keeping a journal requires more CPU cycles and can slow down file write operations somewhat, but as disk performance increases, this is increasingly considered a worthwhile tradeoff for data reliability.

The default filesystems on major OSes today are all journalled, and NTFS is no exception. I’m not going into details of how this is done, and instead will list the things that a journal enables Windows 10 to do.

## Disk recovery with a journal

So what happens when power is cut and a computer reboots? It goes into recovery mode, where it checks the log for incomplete operations, and attempts to complete them. Any files that were “lost” (i.e. file table records that have been separated or desynced from the actual data) get moved to a separate folder, and the disk is considered okay for use again.

## Disk transaction rollbacks

When installing a new application, sometimes you encounter that odd screen where the installation fails because something that needed to happen couldn’t happen. Oh great, the application could not complete installing, and now we have to remove it ... how do we undo all the things that were done?

The journal lets you see a list of all the changes that were made to the disk from the start of the installation, so that you can perform the equivalent steps to reverse their effect.

## System restore with journals

The same thing happens with some Windows updates. Windows stores a lot of the old data as backup, in case you ever want to roll back some system changes, or return to an older version of Windows (minus some breaking updates, for example). And again, the filesystem journal lets you do that, by identifying which changes were responsible for the update.

**Issue summary:** Filesystem journals are a record of changes made to the disk, so as to enable those changes to be rolled back, or to be completed properly in case of sudden interruption.

Journals are serious magic, and are what enable OSes to recover gracefully from a crash. They are kind of divorced from everyday experience, because it is usually unwise to mess with them directly, but I hope the past few issues explain why it is important to not get impatient with your computer when it seems a little slow moving data round.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 111: Copying, moving, and deleting files

I am done with the more technical stuff! Now we can really move on to more everyday experiences, like copying, deleting, and moving files :)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
