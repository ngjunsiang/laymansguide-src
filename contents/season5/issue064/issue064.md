[**Previously:**](https://buttondown.email/laymansguide/archive/) For Meltdown and Spectre to work, they need two things: (1) Permission to carry out instructions (i.e. run programs) on the OS, and (2) knowledge of where the kernel address space is.

Last week, I explained two key limitations of Meltdown and Spectre that are needed for an attack to be successfully carried out. Hackers getting permission they shouldn’t have is not a security flaw related to Meltdown and Spectre, so that really belongs in a different season of Layman’s Guide.

So we’ll focus on problem 2—protecting access to the kernel address space, which is set aside for the OS’s use. The kernel address space contains key information, such as user privilege tables and OS state, which a hacker can compromise to gain higher-level permissions, or to find out where the memory address space for a certain program is running. Such as the customer information database.

## Protecting the kernel address space

One common way of protecting knowledge of where the kernel address space (i.e. the “HQ”) is located is to keep changing its location. For example, newer versions of Linux randomise the location of the kernel address space at each computer bootup, to make it harder for an attacker to guess.

It is still possible for the attacker to slowly probe which parts of the address space it can access, and which parts it can’t, and make a guess where the kernel address space is; I will not go into detail about these various methods.

But do you see the bigger problem? Programs are **actually allowed** to request an address in the kernel address space. The OS checks its permission tables before it tells the program whether it is allowed to access that space. The only thing preventing program access to that space is an OS permission check.

In contrast, if a program tried to request memory address `-56` or `2^65`, the OS wouldn’t even need to check. Negative memory addresses are obviously invalid, as are memory addresses longer than 64-bit (which wouldn’t even be able to be sent).

## Mitigating Meltdown: Kernel address isolation

One fix that has been merged into the Linux kernel since 2017 is KAISER, which aims to prevent programs from even having access to kernel address space. Similar patches have been released for Windows and macOS as well[^1]. Under this patch, **two** sets of address spaces are maintained.

[^1]: Interestingly, these patches went out shortly before Meltdown and Spectre were announced … I won’t speculate about the timing here, you draw your own conclusions.

The first set is the same as before: it is essentially the entire address space. But now, only the kernel (the “core” of the OS) has access to it. The second set contains the entire address space used by programs, excluding kernel address space. This way, programs running with user permissions will not even be able to get data from the kernel address space. It's like trying to get to a room that doesn’t exist (to the program).

Having to keep switching between two sets of pages when executing instructions from both kernel programs as well as user programs is, of course, going to make things take longer than usual. Up to 20% longer for some instructions.

This primarily mitigates the impact of Meltdown, which attempts to access the kernel address space before it gets caught and an exception is raised in the program. But it does not do anything for Spectre, which speculatively executes two possible outcomes where the code meets a decision point, but later discards the outcome which is not needed.

## Crash course: Translation Lookaside Buffer

One concept to cover before we get to the Spectre mitigation. In [Issue 55](https://buttondown.email/laymansguide/archive/lmg-s5-issue-55-addressing-memory/) I talked about how the virtual address space allows programs to access data from different parts of the computer: USB devices, hard drives, network, sound card, and of course not forgetting the physical memory itself.

How does the CPU know that virtual address 2354476 is actually pointing to physical memory address 3564241? It doesn’t. This mapping is stored in the CPU, within the memory management unit. Like all mappings (remember the CPU cache, and the DNS cache from [Issue 39](https://buttondown.email/laymansguide/archive/lmg-s3-issue-39-caches-and-caching/)?), the lookup process can be greatly speeded up with a cache. The part of the CPU that caches virtual-to-physical memory mappings is called the Translation Lookaside Buffer, or TLB.

A key requirement for Spectre to work is for the Translation Lookaside Buffer to remain unchanged, so that it is getting data from the same part of (kernel address space) memory.

## Mitigating Spectre: TLB flushing

Naturally, one way to mitigate Spectre is to keep flushing the TLB. As can be expected whenever you flush a cache, lookups will cause a cache miss and result in the CPU memory management unit having to figure out the mapping all over again, leading to slowdown.

Some performance/security features that are being worked on for processors include selective TLB flushing (flushing only some parts of it but not all), or learning to identify when it should be flushed.

## Last words on Meltdown and Spectre

I lied in the title of this issue: there is no fix. These are only *mitigations*, which can reduce the impact of these attacks, but not prevent them completely.

The dismal conclusion you might not have drawn is that there is little we can do to protect ourselves against such vulnerabilities, besides keeping your OS patched and up to date, and not leaving your computer running continuously for too long (the location of kernel address space is only randomised upon bootup).

The good news is: Meltdown and Spectre are a lot of work. No cases of them being used in the real world have been reported as of yet, and hackers are unlikely to go to this much effort to attack consumers; targets of their attack will probably be database servers of bigger companies.

Still, the origin of these exploits stemmed from an earlier time when our collective focus was on faster and faster CPUs. In the early ’00s, we didn’t hear CPUs being touted as “safe” or “secure”, just “fast”. Neither did we see a need for secure CPUs.

It was only with the explosion of the mobile internet after 2007 that the market became a lucrative target. By the time the hacking tools became widespread, CPUs had already incorporated so many features to speed up processing at the cost of security.

Perhaps it is time for us to reassess the situation, make the judgement call to ask for greater hardware security, and take the bitter pill of performance tradeoff. and then wait for the CPU manufacturers to get the message, if they haven’t already.

**Issue summary:** Meltdown and Spectre require the programs executing them to have access to kernel memory space. Kernel address isolation attempts to prevent the program from even having access to the kernel address space in the first place. TLB flushing changes the virtual-to-physical memory mapping, disrupting Spectre’s reliance on a consistent virtual-to-physical memory mapping.

Phew, that was quite a bit to type. I am glad to be done talking about Meltdown and Spectre; these are sombre topics, and the more I write about them, the less faith I have in the devices I use.

Funnily enough, I had originally titled this season “Operating Systems and the CPU”. I am obviously far from covering things that I think people should know about their operating system, so that will probably resume in another season.

Since I’ve been talking so much about memory, I think it makes sense to bring in one more topic here to close off the season: how do all those programs share a common memory space?

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 65: Memory Sharing in the Operating System

I have only one issue left and I don’t want to end with a cliffhanger, so I’m going to keep the next issue focused on one question: what is all that memory used for?

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
- What is a password hash? [Issue 63]
