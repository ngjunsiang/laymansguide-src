Title: Issue 116: Hibernation
Date: 2021-04-17 08:00
Tags: operating system
Category: Season 09
Slug: issue116
Author: J S Ng
Summary: 
Modified: 2021-04-17 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) When you shut a computer down, it sends an exit signal to all running programs to get them to do their exit routine. This process can sometimes take a long time. To preserve the data configuration in memory while minimising power draw, a computer can go into standby mode: all hardware except the memory gets powered down, until the computer is woken up from standby.

Okay, so standby/sleep mode lets you keep the data configuration in memory by putting the computer into a sort of low-power mode, where only the memory still has power while the rest of the computer is shut down.

If you’re not just going for a short jaunt; you’re maybe getting on a flight and don’t have the laptop charger with you and want your laptop to still be in the same configuration (windows open, Spotify playing, etc) *without drawing any power* … is that possible?

By now, you know the answer is *yes*! You just put the computer in **hibernation** mode!

## Hibernation

How is it possible to preserve data configuration in memory without any power at all? Any time you notice magic like this happening, you should immediately suspect that data storage is involved somehow.

When you put a computer into hibernate, Windows dumps the contents of computer memory into a hibernation file on your storage disk (check if you have `C:\hiberfil.sys` on your computer disk; that’s the one), then *shuts down* your computer. Yup, it’s a shutdown, except the programs don’t have to exit (because remember, the data configuration is already preserved). So this is much faster than a normal shutdown, but not as fast as standby which involves no shutdown at all.

When you press the power button again to bring the system back, the computer still has to go through the bootup sequence (memory was completely wiped, remember). But at the point where control is handed over to the OS ([Issue 112]({filename}/season09/issue112/issue112.md))), the OS does not carry out its usual preparations. Instead, it reads the contents of the hibernation file into memory, then acts as though the system is already booted up! You just log in, and everything is the way it was just before hibernation (keeping fingers crossed …)

**Issue summary:** Hibernation mode causes the computer to store the data configuration into a hibernation file on disk. When powered up, the OS reads the data configuration from the file back into memory. This lets the system avoid having to do a full shutdown and bootup; it performs a shorter version of these two sequences instead.

Okay, so that’s one more mystery explained.

One thing I didn’t think was critical to explain above, but which eventually crops up for most people, is that the hibernation file takes up a lot of space! It needs to contain all the data in memory, so if you have a laptop with 16GB of memory, your hibernation file will be around that size too. If you’re wondering why Windows is taking up so much space, this is usually one of those reasons.

If you found `C:\hiberfil.sys`, you might have also found `C:\pagefile.sys`, another huge file, though not as huge as the hibernation file. What is this one used for? I’ll explain that in the season finale :)

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 117: Swap space

Sometimes, you get a laptop with 2 or 4 GB of memory, and you wonder how it’s able to run Chrome with 46 tabs open; shouldn’t you have run out of memory by now? In the next issue, I’ll explain this trick that lets computers pretend they have more memory!

I wanted to write this issue earlier in the season, but it just never presented an opportune moment. So let’s wrap up with it.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
