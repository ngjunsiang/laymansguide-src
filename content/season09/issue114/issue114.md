Title: Issue 114: In the beginning (firmware)
Date: 2021-04-03 08:00
Tags: operating system
Category: Season 09
Slug: issue114
Author: J S Ng
Summary: 
Modified: 2021-04-03 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) If you can’t get to a BIOS screen, it is likely a hardware problem and has to be solved by a technician. If you can’t get the the OS loading screen, it’s a bootloader problem and needs to be solved with more geekery. If something goes wrong with OS loading, and fails to fix itself on subsequent reboots, it’s probably time for a system refresh or reinstall.

In [Issue 111]({filename}/season09/issue111/issue111.md)), I described the bootup process. These days, anything more complex than a calculator typically has an operating system (OS) running it. Your TV set-top box, your router, even your (high-end) printer and your car have an operating system running them these days!

## Embedded operating systems

That OS is quite different from the one running on your laptop. It’s not meant for users to interact with directly. It primarily runs services which the appliance provides; you’re not allowed to install your own apps on it unless it has a manufacturer-approved app store or you are hacking it.

We call these **embedded OS**es.

## Hardware and Software

We often see the term “hardware” used to refer to physical tools and implements that are needed for a job; they’re “hard” in the sense that they often come fixed into a certain configuration, are not easily changeable, and remain that way for the rest of their lifetime.

“Software”, on the other hand, is … fuzzier, more malleable, less clearly defined. Almost anything goes for software! This is usually the user-facing side of a system.

## Firmware

We usually consider laptop OSes to be software, because it has an installation process, you get small regular updates on it, you can add and remove features … if it looks like software, talks like software, and behaves like software, you might as well call it software.

Embedded OSes are kinda different. They come preinstalled; if they don’t, you won’t know how to install it yourself on a brand new, unprogrammed appliance. You don’t get small hotfixes and updates, only big version changes. And you can’t control what features it has.

If *soft*ware sits at the layer nearest the user, and *hard*ware sits at the layer nearest the machine, then I guess we’ll call the middle layer *firm*ware.

So when you see the word **firmware** used in an interface, I guess you can just think of it as the “OS of the device” :)

**Issue summary:** Embedded operating systems are unlike user operating systems. They are designed to run the software needed for an appliance’s operation, and are not meant to be used by users directly. Since they are considered somewhere between software and hardware, they are usually referred to as firmware.

Okay, that’s one thing out of the way. Now we can move on to shutdowns, sleeps, and hibernates!

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 115: Shutdown & standby

I often hear a lot of confusion about this in my workplaces, and from folks too. This is often the cause of many problems-that-happen-when-I-press-the-power-button. Let’s see what we can uncover.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- ~~firmware? [Issue 34]~~
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
