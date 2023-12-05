[**Previously:**](https://buttondown.email/laymansguide/archive/) Applications are assigned a thread by the OS for running a sequence of instructions. The instructions are executed sequentially, and the app cannot proceed if it gets stuck on any instruction.

## Multithreading

An app can hang if its sole thread gets stuck. In some cases, an app can be written to make use of multiple threads. This is possible when a computer has more than one processing core, or if an operating system is designed to divide computing time among multiple threads.

## Race conditions

Trying to design apps to use multiple threads is hard! Apps running into an error is one thing; a more subtle form of failure is known as a **race condition**. This happens when the success of two or more tasks depend on near-perfect timing which the threads have little control over.

## Main and secondary threads

A common pattern is to have the app’s graphical interface and main code run in its own thread, with any subsidiary tasks (such as opening files) running in a secondary thread. If the task in the secondary thread is taking too long, the main thread can still issue instructions to terminate the secondary thread’s task, and thereby restore order and control.

Sounds fair enough. How might this fail?

Lets take an example: the main thread has a task that involves sending a signal to secondary thread, and then waiting for a response from it. Secondary thread has a task that involves sending a signal to main thread, and then waiting for a response from it. Both tasks complete successfully when they are carried out independently. But what if the main and secondary threads both run those tasks near-simultaneously, before the other thread has a chance to respond? They both get stuck waiting for a response. The app has just hung!

## Multiple worker threads

Another pattern is to split the job up into multiple parts, and have multiple threads each take a part of the job. When they have all completed, the completed parts are then stitched back together into the finished result.

But this has its own ways of failing too.

The threads have to coordinate their job status, and often do so by updating a common set of data. Thread 1 might request access to that data to update it. To ensure that the data doesn’t change before it is done, it will usually request a lock ([Issue 82]({filename}/season7/issue082/issue082.md

One way this can fail in practice is if two or more worker threads request a lock simultaneously. They both get a lock, because at the moment their requests are processed, nothing else has locked the resource. But now they can’t proceed to modify the data because it has been locked by another thread that isn’t them.

This situation is known as a **deadlock**. This and similar situations are just one out of many ways that apps can hang.

**Issue summary:** A race condition happens when threads depend on instructions happening with coincidental timing for success. When instructions are not executed with appropriate timing, one or more threads can get stuck waiting on a response that never comes.

Yep, multithreaded programming is hard.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 104: Storing sensitive data

To wrap up this season on apps, I’ll look at one last question: how do apps keep our data secure

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
