[**Previously:**](https://buttondown.email/laymansguide/archive/) Embedded operating systems are unlike user operating systems. They are designed to run the software needed for an appliance’s operation, and are not meant to be used by users directly. Since they are considered somewhere between software and hardware, they are usually referred to as firmware.

In [Issue 112](), I described the bootup process, and what a process it is! We have sayings in the English language that talk about things taking years to build up, but only seconds to destroy, and that’s certainly the case here. It takes so many steps to get data into computer memory in a way that makes it useable for us humans, and the mere press of a power switch wipes that data configuration once computer memory loses power.

This is obviously undesirable; your work in progress might not have been saved, data that is being transferred to disks might not be written properly and end up getting corrupted ([Issue 109](https://buttondown.email/laymansguide/archive/lmg-s9-issue-109-speeding-up-data-operations/)), and you should never switch off a computer at the power socket this way!

## Forced shutdowns

But sometimes, the computer gets itself so stuck that there’s just no other way to do it. On a laptop or smartphone, which has a built-in battery and cant be shut off immediately at the power socket, this is usually done by holding the power button for more than 10 seconds. This will literally cut off power to the mainboard immediately.

What does a proper shutdown do differently?

## Shutdown

To avoid the Problems described above, we need to give the computer time to wind down. Most programs have a proper exit routine (y’know, the red dot on macOS or the red cross in Windows). This gets the program to write any last bits of data, release any file or database locks ([Issue 82](https://buttondown.email/laymansguide/archive/lmg-s7-issue-82-multiplayer-databases/)), quit, and then release its resources back to the OS. When shutting down, all running programs and services have this exit routine invoked, and they usually quit pretty quickly.

The exceptions to this usually have to do with disk operations, the slowest of operations on a computer. If a program has lots of data to save to disk, or is waiting for a disk operation to complete, it will remain open while attempting to exit, and prevent the computer from shutting down. If you’re wondering why a folder seems to be stopping the computer from shutting down, this is usually the reason!

“Wait, I’m not copying anything …” Yep, but File Explorer in Windows does more than just let you copy, paste, and delete. It also generates image and video thumbnails for you, create file indexes to speed up searching, and so on. And these are disk operations too!

On rare occasions, these disk operations can mean your computer takes up to an hour to shutdown! My best advice, if you’re not in a hurry, is to just leave it alone and let it do its thing. Much safer than having to scan for errors later.

## Standby/Sleep

On older computers, shutting down and booting up took more than 10 seconds, which is quite a killjoy when you are getting ready for a presentation and just need to stuff your laptop into a bag, get up to the conference room, and switch it on again. That feeling when you’re looking at a room full of people looking back at you, waiting for your laptop to boot up … *awkwardddddd*

Some of us just keep our laptops open (because closing the lid causes it to shut down, but you can change that in the settings by the way), and hold it that way while running around. And the purpose of that is just to keep the computer memory powered so we don’t lose the precious data configuration of the computer memory!

What if there was a way to keep power going to computer memory, but have the rest of the computer system powered off, to save on power? That would be perfect for hopping from coffee joint to coffee joint!

This is exactly what happens when you put a computer into **standby** (some systems also refer to this as **sleep**). The computer processor goes into a power state where only the computer memory remains powered ([Issue 112]()). Everything else is powered off—screen, network hardware, storage disks, … until you power the system on again. The memory configuration remains intact, and everything is exactly the way you left it at the moment you put the laptop into standby. Best of all, you didn’t have to go through the long and tedious shutdown-bootup sequence again!

**Issue summary:** When you shut a computer down, it sends an exit signal to all running programs to get them to do their exit routine. This process can sometimes take a long time. To preserve the data configuration in memory while minimising power draw, a computer can go into standby mode: all hardware except the memory gets powered down, until the computer is woken up from standby.

Lots of people don’t know about computer sleep, and resort to workarounds to keep their computer running while they have to move around. But now you know.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 116: Hibernation

Sleep and hibernate; what’s the difference? As it turns out, a lot!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
