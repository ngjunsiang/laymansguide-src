Title: Issue 101: Why apps crash
Date: 2021-01-02 08:00
Tags: app, memory, operating system
Category: Season 08
Slug: issue101
Author: J S Ng
Summary: An app crashes when it encounters a situation it can’t handle, or when it attempts to perform an operation that is disallowed by the operating system.
Modified: 2021-01-02 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Windows systems categorise data into two types: files, and settings. Files are stored under an appropriate subfolder in `C:\`, while other storage devices and network locations are stored elsewhere or given their own drive letters. Settings are managed through the Windows Registry, which is stored in `C:\Windows\System32\Config\` and `C:\Windows\Users\Name\`.

Besides general slowness, two of the most frustrating experiences we have with computers is when they crash, and when they hang.

You mean there’s a difference? Sometimes we use the two terms interchangeably, but they are really not the same.

Remember: applications are just a list of computer instructions telling the computer what to do: where to get the data, how to process it, and what to return. When the instructions make perfect sense, everything goes well. But sometimes they don’t.

## Crashing

A crash happens when the app receives **(a)** a response that it does not know how to handle, or **(b)** is not allowed to carry out.

### Unhandled responses

A common error made by many programming newbies (including me) is failing to account for all the ways that things can go wrong. For example, if I am writing a simple app to read a text file and perform some calculations, an obvious step in the app is sending a request to the operating system (OS) to open the text file.

Even that simple step is fraught with many possible failures! The text file may have been locked by another app (which is writing data to the file), or the user running the app might not have permission to open the file (especially if it is in another user’s home directory), or ...

Well, a whole bunch of things can go wrong. And when they do, the OS throws an error. If the app does not have any code to handle that error ... game over, it cannot proceed and it crashes abruptly.

This is a lot more common than you think, even for experienced programmers, especially when a process that isn’t expected to throw an error actually does it. And sometimes it just can’t be helped: when your computer runs out of memory, and an app requests for more memory but doesn’t get it, and it just cant go on without that memory ... it crashes.

### Illegal instructions

Memory in the computer is managed by the OS ([Issue 65]({filename}/season05/issue065/issue065.md))), which partitions it into different zones. The memory used by OS processes is protected from access by other apps (for your privacy and protection), and memory used by an app cannot be used by another app, unless it is shared memory space.

So when an app sends an instruction requesting to access memory space it does not have authorisation to, or when the OS itself attempts to access an address that it can’t (especially addresses that point to hardware devices) ... it crashes. An app crash just brings you back to your desktop, but an OS crash usually leads to the famous Blue Screen Of Death (BSOD).

These days, OSes are better at handling crashes. If the crash occurs in the window management system (the part that lets apps create windows on screen and icons in the taskbar), Windows can often just restart it without restarting or touching the rest of the OS. But if it happens in a critical part that can’t be restarted by itself, then ... BSOD :)

**Issue summary:** An app crashes when it encounters a situation it can’t handle, or when it attempts to perform an operation that is disallowed by the operating system.

Definitely oversimplified for ease of understanding, but I see no point going into the technical details unless a future issue calls for it.

Before going into app hangs, I’ll need to talk about threads first. If you have heard of multithreading before, yep I am going to talk about that next issue!

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 102: Threading

“Many hands make light work” is true for computers as well, and I’ll go into more detail about how a computer uses its many hands to speed up the work it does :) Before that, let’s examine the simple case of an app doing only one thing at a time: the single-threaded app.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- a password hash? [Issue 63]
- a driver file and why do I need one? [Issue 98]
