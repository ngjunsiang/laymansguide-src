Title: Issue 56: Operating Systems and resource management
Date: 2020-01-18 08:00
Tags: 
Category: Season 5
Slug: lmg-s5-issue-56-operating-systems-and-resource
Author: J S Ng
Summary: 

**Previously:** The CPU just executes instruction after instruction after instruction. Each instruction may consist of loading data from a memory location, sending data to a memory location, or performing operations on the data it is holding.

If the CPU is mindless and simply carries out instructions, there must be some kind of a “higher mind” maintaining order and harmony within the CPU so that our programs don’t muck things up for each other.

In the early days of computing history, this higher mind was the programmer. In those days, a programmer had to mentally partition the limited memory space, and ensure that the programs being executed on the CPU don’t inadvertently muck up the memory in unexpected ways. This was manageable for a while: up to a few thousand, or tens of thousands of memory addresses, with a sensible set of rules. But as programs became more complex, and when multiple programs had to be run on the same computer, bugs started to creep in and become difficult to trace and fix.

Humans could no longer manage the CPU’s resources. It had to be automated. And so the operating system (**OS**) was born.

## The operating system manages the computer’s resources

An operating system has to do a few things at minimum:

1. Enumerate the devices on the computer: checking all its available interfaces and listing the devices connected to each interface, to be made available to programs upon request.
2. Registering device ports into the virtual memory address space. This includes physical memory, hard drive ports, printer ports, keyboard and mouse and other USB device ports, and so on. This makes the devices available to programs that need to load data from those devices, or send data to those devices.
3. Manage running programs, giving each program its own memory space, dividing up the available CPU time among programs so that each gets some runtime, allocating more memory to programs that request it, reclaiming memory from programs that release it.
4. Enforce security by ensuring that programs only carry out instructions that they are allowed to. This is why Windows keeps bugging you about program permissions. This also ensures that guest users cannot access the data of other guest users, and cannot modify important system files.

This is both an art and a science, and getting it right is an ongoing study. When an OS works well, instructions from different programs can be mixed into the same queue and executed by the CPU without the data somehow getting mixed up. And programs will not be able to dabble into the private memory area of other programs.

But cybersecurity is a multi-billion dollar industry with good reason. Black hat hackers and cybersecurity researchers are constantly trying to find loopholes in the OS logic so as to access data they are not supposed to be able to access. In Meltdown and Spectre, the loophole is not a fault in the OS logic, but in a hardware feature of the CPU which I will explain in the next issue: the CPU cache.

**Issue summary:** The operating system is responsible for listing and managing the computer’s resources, making them available to programs running on the computer, and making sure they only use what they are allowed to.

## What I’ll be covering next

**Next issue:** Cache, the CPU’s working space

The pieces are in place now for me to introduce the crux of the matter: the CPU cache. This is where the heart of Meltdown and Spectre takes place, and yet we cannot do away with it. Stay tuned to learn why.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
