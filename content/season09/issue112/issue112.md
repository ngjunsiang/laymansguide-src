Title: Issue 112: Bootstrapping into existence (bootup)
Date: 2021-03-20 08:00
Tags: 
Category: Season 9
Slug: issue112
Author: J S Ng
Summary: 
Modified: 2021-03-20 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Moving a file (within the same disk region) merely updates its file table record, and this happens really quickly. Copying a file, or moving it to a different disk/region, involves copying the contents and then updating the file table record, and is considerably slower. Deleting a file only requires that its file table record be removed, and is a very fast operation (if it does not involve the Recycle Bin).

We humans wake up in the morning and magically there is information in our heads. We open our eyes, trust that all our limbs and body parts are there, and we just get up and make coffee.

Computers, they are different in that regard. After they light up the power LED, there is just … nothing. Computer memory needs power to hold its information[^1], so once you really power down your computer, all data in memory is gone. Your operating system (OS), your open programs, your file data … all that now resides only in your hard disk. Whatever was not written to hard disk would have been lost by now ([Issue 108]({filename}/season09/issue108/issue108.md))).

[^1]: Memory comprises lots of capacitors wired together, and capacitors slowly leak charge when they are not powered. Memory chips need periodic “refreshing” every few milliseconds to avoid losing data due to this charge leakage.

Before anything can be done, the computer needs to read all that information back in to memory. But there’s *nothing* in memory … you need a program loaded in memory to do that, but that program is still residing in file storage—it’s a Catch-22! The OS has to *bootstrap* itself into existence first, in a process known as the **bootup**.

## Bootup

The way to sidestep the bootup paradox is to have a very tiny chip perform the bootstrap. This tiny chip is already wired up in a particular way from birth; it contains a program called the BIOS (short for Basic Input/Output System)[^2], which does only three things:

[^2]: Modern BIOSes are no longer stored permanently on a chip, but written to flash storage (similar to a thumbdrive) that is soldered directly to the motherboard.

1. Check that the core parts are present: CPU, memory, video card, keyboard, storage disk.  
   At the BIOS screen[^3], you can press a button to configure BIOS settings.
2. The BIOS checks the available disks to see if they are “bootable”, i.e. contain information in a specific part of the disk that contains a **bootloader**. In modern BIOSes, you can override this process by specifying a valid disk containing the bootloader.
3. The BIOS loads the bootloader into memory, and runs it.

[^3]: Today, this process is hidden by a branded startup screen on machines that come with Windows pre-installed. You can usually disable that screen if you like to see this bootstrap process happening.

## The bootloader

The BIOS is not optimised—it’s only a *basic* system after all—and would take forever to try to get the OS running on its own. So, with its limited resources, the BIOS calls in bigger guns: the **bootloader**.

The bootloader is not the OS! It has only one job: to *load* the OS during the *boot* process, and carry out whatever is necessary before that.

Usually, the first thing that needs to be loaded is the filesystem ([Issue 106]({filename}/season09/issue106/issue106.md))). Without that, no program will know how to read in data from the storage disks! At this point, if the bootloader detects disk errors or uncompleted operations in the journal ([Issue 110]({filename}/season09/issue110/issue110.md))), it may attempt to scan for errors or complete those operations before proceeding with the rest of the bootup process.

Some systems may contain multiple OSes: Mac users may want to run Windows using Parallels Desktop, Windows users may want to dabble in Linux, and many Linux users dual-boot Windows as well. The bootloader, with the help of the filesystem, detects other operating systems on the storage disks, and offers the user a choice of which one to boot. If there is only one OS found, this step might be skipped.

Once an operating system is selected, the bootloader loads the OS **kernel**, which contains its core instructions, and hands control over. The bootup sequence is not yet complete, but the bootloader has completed its job.

## The operating system startup

The operating system is not ready to accept user input at this point yet. It still has to mount other storage disks and their subregions, check that other hardware is available and working properly (such as hardware timers, which are very important for an operating system), start up various necessary services, start up programs which asked to be started up when the system boots (like the annoying Adobe Updater, or your sound card drivers and utility), etc.

Finally, when it is ready, it displays the login screen.

**Issue summary:** When a computer is booted up, it runs the BIOS from a chip on the motherboard. The chip checks that core parts are present, checks for a storage disk containing a bootloader, loads it into memory, and hands over control. The bootloader loads the operating system kernel. The operating system kernel then does whatever it needs to do to get the system ready for use.

This a prelude to the next issue, which is where I attempt to explain, as simply as possible, the usual things that go wrong in the bootup process.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 113: A computer’s existential crisis (boot failure)

We’ve all been there. The computer doesn’t get to the login screen. We are shocked that our daily driver, our churner of spreadsheets, can do this to us. Worse, it has left us in an environment we are wholly unfamiliar with: a blinking cursor in a sea of black, cryptic text explaining nothing, and the unbearable pressure of a system silently begging us: fix me.

**Sometime in the future:** What is:

- ~~booting up? [Issue 15]~~
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
