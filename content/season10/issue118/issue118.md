Title: Issue 118: When I run two file-copy processes at the same time, why are they much slower?
Date: 2021-05-01 08:00
Tags: 
Category: Season 10
Slug: issue118
Author: J S Ng
Summary: 
Modified: 2021-05-01 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Operating systems use a page file on the storage disk as a complement to physical memory. This allows OSes to behave more performantly than they would if they did not have a page file. Data that is rarely accessed is moved to the pagefile (“paged out”), and can be paged in when it is needed later, albeit with a performance hit.

It’s kind of funny the moment you realise how much of what an operating system (OS) does is try to mitigate the slowness of hard disks. But why are they so *slow*? There’s an actual explanation for that, and along the way it will help us understand a few things about why OSes sometimes behave funny.

## What is a hard disk?

A hard disk is a magnetic platter that stores data. This platter contains trillions of magnetic atoms; yep, they’re atom-sized magnets! These atoms are grouped into clusters called magnetic domains; they are so tiny that 500 of these placed in a straight line would stretch the diameter of a human hair! These domains can align themselves in one of two different ways: let’s call them “up” and “down”. Each bit (as in, 8 bits = 1 byte) is stored as the alignment of a magnetic domain: up represents 1, and down represents 0.

To read data, all you need to do is move a tiny electromagnet over each domain, and use it to see which way the domain is aligned. This can be done by measuring the current flowing through the electromagnet, a detailed explanation of which is beyond the scope of this newsletter (perhaps in a future newsletter titled “Layman’s Guide to Physics” or something).

To write data, you pass a current through the electromagnet to magnetise the domain below it whichever way you want; just spin the platter and keep changing the current to write a series of 1s or 0s.

Put 3-5 platters together, attach the electromagnet to a moving arm (called the read arm), control the whole thing with some microchips, and you have a hard disk.

<figure>
    ![Open hard disk]({attach}/season10/issue118/issue118_01.gif)
    <figcaption>A picture of an opened hard disk, showing the read arms and magnetic platters</figcaption>    
</figure>

## Characteristics of a hard disk

A hard disk spins at a constant speed, because it is much more complicated to figure out how to read/write stuff when the speed can vary. The larger hard disks, which go into desktops and use 3.5-inch platters, spin at 7200rpm, while the smaller hard disks, which go into laptops and use 2.5-inch platters, spin at 5400rpm.

Data stored near the circumference of a magnetic platter is faster to read than data stored near its centre. For this reason, OSes that are installed on hard disks usually attempt to partition the storage space so that the operating system is stored on domains closer to the circumference.

The read arm moves really close to the platters during disk operation! The gap between them (called the head gap or flying height) is half the thickness of a human hair. This is why you do not want to drop hard disks while they are in operation; the slightest movement of the read arm towards the magnetic platter causes it to gouge the platter surface and damage it permanently: this is called a head crash.

## Read and write operations

The hard disk is ultimately a mechanical device; each operation involves moving parts.

Reading from or writing to a domain involves:

1. Spinning up the platter (if it isn’t already spinning)
2. Moving the read arm to the correct position
3. Measuring or inducing a current

This means that each time the hard disk needs to access data from a different region of the disk, there is significant lag time (~5ms; see [Issue 57]({filename}/season05/issue057/issue057.md))). This is the time needed for all those movement described above. It is thus advantageous to try to put all the data you need in contiguous domains[^1], to minimise read arm movement.

[^1]: This process is what millennials might remember as **defragmentation**, or defragging.

So when an OS tries to perform two data operations at the same time (instead of sequentially), the read arm has to move a lot more to access data from different regions. And this is why, if you have multiple data operations to perform on a hard disk, you should try to do them sequentially instead of simultaneously!

**Issue summary:** A hard disk consists of a read arm, and a set of magnetic platters which store data. To read or write data, the read arm must move to the appropriate track of the rotating platter, and detect the magnetic field (for reading), or attempt to magnetise the domains on the platter (for writing). Operations that require the read arm to access different parts of the magnetic platters intermittently result in slower read speeds.

This was something that took me a while to figure out; first, to notice that it was actually happening, and second, to read up enough about hard drives and take some (nonworking) ones apart to understand. And now I can explain it to you :)

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 119: Solid-state disks, an upgrade from hard disks

Next, we look at the technology that has been steadily replacing hard disks as system disks in most desktops and laptops. These have managed to eliminate the latency due to moving parts, and enable much higher read and write speeds.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
