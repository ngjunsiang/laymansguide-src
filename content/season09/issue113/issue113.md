Title: Issue 113: A computer’s existential crisis (boot failure)
Date: 2021-03-27 08:00
Tags: operating system
Category: Season 09
Slug: issue113
Author: J S Ng
Summary: 
Modified: 2021-03-27 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) When a computer is booted up, it runs the BIOS from a chip on the motherboard. The chip checks that core parts are present, checks for a storage disk containing a bootloader, loads it into memory, and hands over control. The bootloader loads the operating system kernel. The operating system kernel then does whatever it needs to do to get the system ready for use.

In this issue, doom and gloom.

## Nothing happens

Sometimes, you press the power button and nothing happens. Absolute stillness.

This is not a software problem; something is wrong with the computer’s power source (the power supply unit of a desktop, or the battery/charging system of a laptop), and you have to bring it to a technician.

## Something happens, and then nothing happens

If you hear fans spinning, the power source works. But if nothing appears on screen after that, and then the system seems to reboot again, it may mean the BIOS has failed; if you attempted to upgrade the BIOS recently, that might be a possible cause. A friendly geek might be able to fix this for you.

If you hear fans spinning for a long time, and things *seem* to be happening, but nothing is showing on screen, your video card (future issue, I promise) may be borked. Can’t do anything other than sending it in to a technician.

If you have attempted a driver upgrade recently (again, future issue), that might be a possible cause.

When the BIOS works, you should see the startup screen—always a comforting sight.

## Bootloader issues

Bootloaders are reliable as anything, so seldom anything goes wrong here.

The most common bootloader problem is that it does not detect any OSes to boot—may be the case the first time you attempt dual-boot, or get advanced enough to start playing with bootloaders (Windows and Mac don’t let you do that, so these are almost always Linux users). This is … something that can only be solved with more geekery, and is beyond the scope of this newsletter. Sorry 😬

## OS booting problems

The OS, being the most complex part of the bootup process, is often where things go wrong.

If nothing has changed in the system since the last bootup, usually things go smoothly. So it’s almost always changes to the system that cause this.

Sometimes you installed a program that dabbles in the system innards—a system-optimising program maybe—and it attempts to change some settings but without propagating them to all the required places. This leaves the system in an inconsistent state.

Sometimes you attempted a Windows Upgrade[^1], possibly a major one, and it did not go as hoped. Windows usually will attempt to undo the damage it wrought, and may or may not succeed in leaving your system in a bootable state.

[^1]: These days it’s more like you attempted to stop a Windows Upgrade, but did not manage to do so or it is unskippable.

Sometimes some system files get corrupted—remember that this can happen if you force a computer to power off before it has finished its shutdown properly. If the OS can’t find that file, it sometimes initiates a search for it in the system disk, which can take … really long.

In my opinion, the best way to resolve these issues, especially if they are recurring, is with a system refresh or reinstall.

**Issue summary:** If you can’t get to a BIOS screen, it is likely a hardware problem and has to be solved by a technician. If you can’t get the OS loading screen, it’s a bootloader problem and needs to be solved with more geekery. If something goes wrong with OS loading, and fails to fix itself on subsequent reboots, it’s probably time for a system refresh or reinstall.

I told you, gloom and doom. Modern OSes are getting more sensible at not requiring human intervention, so when they fail to resolve their own issues, there is often little a layperson can do on their own.

The best thing you can do for yourself and your data is to ensure you have a copy of your critical data elsewhere. Always have backups of things you are working on.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 114: In the beginning (firmware)

I tried to find a place to talk about firmware in this and the previous issue, but couldn’t do so without taking the story in weird directions. So we’ll take a short detour to do that next issue, before I talk about shutdowns, sleeps, and hibernates.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
