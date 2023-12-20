Title: Issue 119: Solid-state disks, an upgrade from hard disks
Date: 2021-05-08 08:00
Tags: 
Category: Season 10
Slug: issue119
Author: J S Ng
Summary: Solid-state disks are much faster than hard disks because they have no moving parts, so no time is wasted waiting for parts to get into the right position. However, they are more expensive than hard disk drives.
Modified: 2021-05-08 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) A hard disk consists of a read arm, and a set of magnetic platters which store data. To read or write data, the read arm must move to the appropriate track of the rotating platter, and detect the magnetic field (for reading), or attempt to magnetise the domains on the platter (for writing). Operations that require the read arm to access different parts of the magnetic platters intermittently result in slower read speeds.

Hard disks were, for a long time, the best affordable storage technology we had. But then something better came along: the solid state disk[^1] (SSD).

[^1]: The name has to do with the fact that its working principles are based on [solid state physics](https://en.wikipedia.org/wiki/Solid-state_physics), and not on the solidity of the disk itself.

## What is a solid state disk?

It is, to put it simply, a small circuit board with lots of chips, that plugs into your laptop.

It has multiple storage chips, quite similar to the ones in your thumb drives/flash drives but much faster, and one controller chip to rule em all.

![Solid state disk inserted into laptop slot]({attach}/season10/issue119/issue119_01.jpg)  
*A solid state disk, plugged into a laptop slot (but not secured)*    

## Hmm ... like computer memory?

Computer memory also consists of chips on a circuit board, right? But memory gets wiped after the computer loses power ... but that doesn’t happen with SSDs; why?

![Computer memory inserted into memory slot]({attach}/season10/issue119/issue119_02.png)  
*Computer memory sticks, inserted into the memory slot of a computer motherboard*    

Computer memory uses capacitors, which are like micro-sized batteries. They hold a charge when powered, and store either a 1 or 0 state by being charged or uncharged, respectively.

Solid state storage, on the other hand, uses gated transistors instead of capacitors. They lock a bunch of electrons behind a gate to fill a storage cell (storing a 1), and empty it by forcing the electrons out (strong a 0). This is slower than charging/discharging a capacitor, but hey you don’t lose your data when the power goes out!

## Solid state disks have no moving parts

As you can see, there are no read arms or magnetic platters involved. No waiting for a platter to spin up, no waiting for a read arm to move back and forth ... access is almost instantaneous[^2].

[^2]: Feels almost instantaneous to humans ... but this still takes a few microseconds, which is considered slow for a computer!

This is a big deal when reading data from multiple locations; the response is hundreds of times quicker than a hard disk!

## What’s the drawback?

The biggest drawback for now is of course price. Solid state disks cost much more, per GB, than a hard disk drive (HDD).

Another potential drawback is that SSDs have a limited lifespan. This lifespan is not measured in months or years, but in the amount of data written.

You see, each time electrons are forced through the gate (called a program-erase cycle), the gate gets weaker. Do it tens of thousands of times, and eventually the gate gets too weak to hold electrons. A budget SSD typically has a lifespan of 30,000 program-erase cycles. For a 256GB SSD, that’s 7.68 **million** GBs of data-writing before it fails!

This was a big concern for early SSDs, which had program-erase cycles in the low thousands. Today, with technology improving the program-erase cycle lifespan of SSDs, most users would not come close to reaching the end-of-life of an SSD.

**Issue summary:** Solid-state disks are much faster than hard disks because they have no moving parts, so no time is wasted waiting for parts to get into the right position. However, they are more expensive than hard disk drives.

I managed to write this issue without once mentioning write amplification or NAND, and I consider that a significant personal achievement.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 120: Drivers, the glue between hardware and firmware

So ... hard disk drives and solid state disks work pretty differently under the hood, yet when you plug them into a computer they just ... work? How does that happen?

For that matter, how do devices just work when we plug them into a computer?

This next week, when I finally talk about ... drivers!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
