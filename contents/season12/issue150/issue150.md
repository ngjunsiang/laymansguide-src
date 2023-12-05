Title: Issue 150: System VMs vs Process VMs
Date: 2021-12-11 08:00
Tags: 
Category: Season 12
Slug: lmg-s12-issue-150-system-vms-vs-process-vms
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Containers are one layer of virtualisation above virtual machines: containerisation systems virtualise access to the operating system, presenting a virtual interface that provides software with the resources it needs, without being aware of software running in other containers on the same system.

## Recap

If I need to configure an entire machine to install and configure my own operating system (OS), I can rent a virtual machine — this is system virtualisation.

If I just need to run a set of software *on a particular OS* but don’t want the hassle of managing the rest of the OS, I can containerise them for the OS — this is containerisation.

What if I want to write software that will work the same on multiple OSes? Is that possible?

Before 1995, no!

## OS-level details are tricky

OSes mediate access to resources through libraries ([Issue 17]({filename}/season2/issue017/issue017.md)). Instead of having to deal with storage disk sectors and blocks, you can just use library features to ask the OS to help you create a file and write data to it. The OS and filesystem ([Issue 106]({filename}/season9/issue106/issue106.md)) take care of the details.

I don’t know how to explain this more clearly without showing some programming code; the OS controls a lot of things! Which is a problem when it comes to multi-OS support, because different OSes control different things differently.

The library features for lots of things — storage, searching through directories, networking, etc — are different between Windows, Linux, MacOS, ...

## Abstracting away the details

Can’t we program in a higher-level language, and use another program (the code interpreter) to break it down to different types of operations on different operating systems? E.g. `python.exe` on Windows will try to make my Python code work in Windows by using Windows libraries, `python` on Linux will do so using Linux libraries, and `python` on MacOS will do so using macOS libraries. Javascript, Ruby, Perl, VBScript, and other **interpreted programming languages** work this way too[^1].

[^1]: As opposed to **compiled programming languages** ([Issue 54]({filename}/season5/issue054/issue054.md)), where code is compiled into CPU instructions for one hardware platform for one OS only.

To a large extent, this is possible. But there remain some irreconcilable differences:

- if you need to use Python to run a command-line program, such as a shell script ([Issue 16]({filename}/season2/issue016/issue016.md)), those will depend on terminal availability: not all terminals have cross-OS support!
- If you need to specify a file location, Windows and Linux do not use the same path separators (the character that separates folder names in a folder hierarchy); Windows uses `\` to separate directory names, while Linux and MacOS uses `/`. This is often a source of bugs and headaches.
- Important advanced features, such as multiprocessing (on multiple CPU cores simultaneously), are [handled differently in different OSes](https://rhodesmill.org/brandon/2010/python-multiprocessing-linux-windows/) in ways that may be incompatible within the same program.

## Virtualising processes vs virtualising hardware

So it looks like we need something more. We need a programming language that can be interpreted into intermediate instructions (these are called *bytecode*), and we need a program for each OS that can carry out these intermediate instructions.

That program is also called a virtual machine (VM), but this is not hardware virtualisation. It is *process* virtualisation.

The OS interacts with virtual hardware without directly accessing the underlying hardware. Similarly, we want our code to interact with a virtual process instead of using OS libraries directly.

This is how the Java programming language works. It provides a (process) VM, called the Java VM, for each operating system. Your Java program interacts with the Java VM only; it mediates all access to the operating system.

**Issue summary:** System VMs provide a set of virtualised hardware that the OS interacts with. Process VMs provide a set of libraries that a program (written in that programming language) interacts with.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 151: the Java VM

The idea sounds pretty cool ... so why don’t we write more programs this way? And what *is* the Java VM anyway?

Light discussion on code-adjacent issues next issue!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
