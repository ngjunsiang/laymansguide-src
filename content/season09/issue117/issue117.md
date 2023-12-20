Title: Issue 117: Swap space
Date: 2021-04-24 08:00
Tags: cpu, memory, operating system
Category: Season 09
Slug: issue117
Author: J S Ng
Summary: 
Modified: 2021-04-24 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Hibernation mode causes the computer to store the data configuration into a hibernation file on disk. When powered up, the OS reads the data configuration from the file back into memory. This lets the system avoid having to do a full shutdown and bootup; it performs a shorter version of these two sequences instead.

In [Issue 57]({filename}/season05/issue057/issue057.md)), I laid out the transfer speeds and latencies for a few places in the computer where data can be stored:

- Hard disk drive (HDD): ≈5 ms response latency, 100 MB/s transfer speed
- Solid state disk (SSD): up to 0.1 ms response latency, 0.5–1+ GB/s transfer speed
- Physical memory (RAM): 0.1 µs (0.0001 ms) response latency, 20GB/s transfer speed
- CPU register: <1 ns (<0.000001 ms) response latency

Apart from the CPU itself, physical memory is one of the fastest places to store and retrieve data. It’s just such a pity that there’s a limited amount of it, and you really can’t get more than 32GB of it in a single computer (for future readers, this is written in early 2021). If you bought a cheaper computer that only has 8GB or only 4GB, this quickly limits the number of apps you can have open at any single moment.

What happens when you run out of memory?

## Running out of memory

When a program needs more memory, it requests it from the operating system (OS), and waits for the OS to give that memory. After all, it can’t do anything else until the memory is available.

The OS, on the other hand, will give that memory if it is available. If not, it will wait for other programs to free up memory before passing that memory to the waiting program. If no program is willing to release memory …

I guess the computer just hangs 🤷

## Mitigating out-of-memory problems

If memory is limited, what can we do to increase it?

As it turns out, not all parts of memory are constantly being written to or read from. Lots of it is just sitting there, waiting for that one moment when the data is needed. Kind of wasteful if out of 8GB of memory, only 2GB is actively changing in any hour.

The OS could write that mostly-static 6GB to disk and free it up for other programs, maybe? Then when the data is needed, the OS reads it back from disk before passing it to the program. Yes, this would mean a slower response time for programs that have been idle for a while, but surely better than hanging because it ran out of memory?

This is what all modern OSes do. They write unused in-memory data to a file known as the **page file**. In Windows, the page file is `C:\pagefile.sys`. When data is moved from physical memory to the page file, it is said to be *paged out*, and when moved from page file to physical memory, it is *paged in*.

In older systems or software, you may also see this page file referred to as a *swap file*, or *swap space*. On Linux, a subregion of storage space can be set aside as a *swap partition*.

## Why is it called the page file?

Computer memory is organised into pages, each page typically being 4 KiB (notice that disk sectors are also typically 4 KiB ([Issue 106]({filename}/season09/issue106/issue106.md))) …). The computer may have only 8GB of physical memory, but present 16GB of virtual memory ([Issue 56]({filename}/season05/issue056/issue056.md))) to programs. Kind of like how banks only hold some liquidity but present their assets as being much more …

So the 8GB “shortfall” is actually in the pagefile, not in memory. The pagefile essentially acts like (much slower) memory! The OS reads pages from it and writes pages to it, through virtual memory accesses.

## This sounds like a waste of space, can I choose not to use it?

Though most OSes are configured to use a page file by default, you can configure it to not do so, although this is ill-advised (and I won’t explain why here; this is a newsletter aimed at layfolks). Modern OSes are pretty smart at managing page files, understanding that it is much slower than physical computer memory. They have their own algorithms to decide when to move data to a pagefile, and these days they even forecast when data that was paged out will soon be needed by the program.

OSes need page space for all kinds of reasons: as a kind of “emergency space” when physical memory is full, as working space for optimising data layout in memory, etc. So that disk space is definitely not going to waste!

**Issue summary:** Operating systems use a page file on the storage disk as a complement to physical memory. This allows OSes to behave more performantly than they would if they did not have a page file. Data that is rarely accessed is moved to the pagefile (“paged out”), and can be paged in when it is needed later, albeit with a performance hit.

Pagefiles are pretty amazing, even though they used to be a huge pain in older systems, when they were stored on *slowwww* hard disks. These days, page files stored on solid state disks are pretty fast! While the performance hit of a page miss is still noticeable (like when you switch to a Chrome tab that you haven’t touched in a while), it is far from the groan-inducing wait it used to be.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 118: When I run two file-copy processes at the same time, why are they much slower?

Next week, a new season! With operating systems much more fleshed out for you (I hope), I can finally delve into the nuts and bolts of the machine itself: the hardware.

Since this *is* a layman’s guide, I’m going to focus on the interesting bits, the parts that actually answer long-standing questions :)

Let’s start with a bang: sometimes you are copying a file from one flash drive to your external hard disk. And you need to copy another file from your external hard disk to the same flash drive (or even a different one). You’re scared; can the computer handle it? But this is taking so long; let’s just try it anyway.

And you notice the speed suddenly plummets. Why does that happen? Even with 117 issues of Layman’s Guide written, I don’t have enough background laid down to explain this. So let’s delve into the hard disk in the first issue of Season 10.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
- a video card? [Issue 113]
