Title: Issue 102:  Threading
Date: 2021-01-09 08:00
Tags: 
Category: Season 8
Slug: issue102
Author: J S Ng
Summary: 
Modified: 2021-01-09 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) An app crashes when it encounters a situation it can’t handle, or when it attempts to perform an operation that is disallowed by the operating system.

This post is a prelude to talking about app hangs. Hangs are both simple yet complicated to talk about, but there’s a piece of the puzzle that has to come into the picture first. That piece is about how apps work.

In a computer, the operating system (OS) has to coordinate the requested actions of so many different apps. How does it know which action came from which app?

Through a mechanism known as threads.

## Threading

When you run an app, the OS creates a separate thread. A thread is a sequence of programmed instructions, like a thread of thought. Or a thread of bureaucracy. The OS completes each instruction in the thread, and if it gets stuck on any single task, it cannot move on.

Sometimes, this is good and necessary, like when you need input from the user (don’t be doing anything else until I tell you what I need!). Other times, it is unnecessary waiting.

## What causes threads to get stuck?

Some of us really hate math, but not computers! The math is hardly ever what causes threads to stop.

Like in the workplace, it is often other ~~people~~ devices.

When an app (running in a thread) tries to open a file to read data from it, the operating system has to look up the virtual memory  address ([Issue 55]({filename}/season05/issue055/issue055.md))), follow it to the hard disk or solid state disk, and then wait for the disk to respond with the data.

And in that moment, *lots* of things can go wrong.

If the disk is failing, and unable to read the sector where the data resides, it will usually keep attempting to do so. Meanwhile, back in the operating system, the thread is stuck. It cannot move on, because the previous instruction to open the file has not completed. It can’t even decide to abort the currently-running instruction—telling the app to stop **is already another instruction** which has to wait!

The only thing to do now is wait for the OS to realise that this thread is taking too long to do its thing, and forcibly terminate the thread. This is known as a thread **timeout**.

Is there any way to work around this? Yep! The termination instruction has to come from a separate thread. This means the app has to run multiple threads.

**Issue summary:** Applications are assigned a thread by the OS for running a sequence of instructions. The instructions are executed sequentially, and the app cannot proceed if it gets stuck on any instruction.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 103: Why apps hang even with multiple threads

Processors today already have multiple cores, and many apps can already run on multiple threads. Why do they still hang? I’ll answer this in the next issue :)

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
