Title: Issue 63: Limitations of Meltdown and Spectre
Date: 2020-03-07 08:00
Tags: 
Category: Season 5
Slug: issue063
Author: J S Ng
Summary: 
Modified: 2020-03-07 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) To snoop the cache, we:

1. Flush the cache corresponding to the 256 memory addresses (to get a cache miss when attempting to load the data from memory)
2. Load the secret value using Meltdown or Spectre attacks (the secret value is only one byte, and cannot be greater than 256, so 256 addresses are sufficient)
3. Load the memory address from step 1 that corresponds to the value of the secret - this address is now cached, and the next request for it again will result in a cache hit
4. Request each address and look for the one with a lower request latency

At the heart of the exploit is a cache which, being managed by hardware, is not subject to more fine-grained OS control. This is presumed to be safe by engineers, since you can’t access data directly from hardware easily. But as we have seen in this season, with the right exploit, you can still get to that data, with or without permission.

Just how vulnerable are we to Meltdown and Spectre?

## Getting permission

Every exploit relies on one or more things to work before it can do its things. Meltdown and Spectre require a way to run themselves on the CPU, in the OS. That means a black hat hacker will have to obtain illegal access to the OS, and there are a few common ways to do so:

1. **By cracking a password**  
   If the hash of a password (future season) is leaked, hackers can try to reverse-engineer the original password that led to that hash. This requires A LOT of CPU time, and is often not feasible for properly hashed passwords.

2. **Getting a password from an unsuspecting user**  
   Other people, usually admins and employees, of the OS will already have access to it. A black hat hacker can try to get the password from them through phishing means, or trying to get keystroke-logging malware onto a flash drive they use, or simply posing as a contractor who needs the password for … whatever reason.

3. **Exploiting vulnerabilities**  
   There are many ways to get an OS to carry out instructions it is not supposed to. An improperly secured web app could receive malicious form data from any of its pages that tells the database to return supposedly-secured information. An improperly configured web server could be exploited by sending it more data than it requested. (Just see the number of “buffer overflow” entries [on this page](https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-66/opov-1/Apache-Http-Server.html)). If it is not properly written to know what to do with this excess data, and naïvely stores it into memory or processes it, that leads to Bad Things Happening.

Once the black hat hackers find a way to get permission to run things in the OS, they are in lala-land! Not quite. There are different levels of permissions, and the most restrictive ones might not let you run any programs except from a whitelist. At the other end of the privilege spectrum, **root** accounts let you do pretty much everything and anything. This is why if you are ever asked to be root (or Admin) of a computer (including your router), you should really keep that password in a safe and secure place, such as a password manager.

## Knowing where the loot is

During that tiny window of opportunity, the black hat hackers are trying to read data from parts of virtual memory they are not allowed to access. But which are those parts?

Within the physical memory part of the virtual memory space—

Okay, quick unpacking here. Remember that the virtual memory space is where all our devices get an address? Hard drives, USB devices, network interfaces, … and of course, physical memory (also known as “RAM”—yes, the same RAM you usually see on the specs of computers). Programs request data from and send data to these devices by using their virtual memory addresses. Each cell in physical memory also gets an address in virtual memory space.

Within the physical memory part of the virtual memory space, there are portions which are set aside *for the OS only*. This is the **kernel address space**, which is where critical information such as user privilege tables and OS state get stored. Knowing the addresses in the kernel address space is a big requirement for many exploits, so OS engineers obviously put a lot of work into make sure they are as hard to guess or discover as possible.

**Issue summary:** For Meltdown and Spectre to work, they need two things: (1) Permission to carry out instructions (i.e. run programs) on the OS, and (2) knowledge of where the kernel address space is.

Problem (1) has been with us since the operating system was born. Problem (2) is also not new: it’s basically figuring out where the HQ is. Spies have also been doing that since time immemorial. But we are now dealing with a space where humans cannot tread: the virtual memory space. Hackers are sending preprogrammed chunks of compiled code into the computer to sniff out data-loot and get it out, while we are programming computers to try to detect such attempts and warn us about them or stop them outright.

Meanwhile, the processor manufacturers are trying to make everything happen faster. They are, of course, trying to prevent hackers from doing their thing, but it’s hard to do that while also trying to make things go faster. Next issue, I’ll try to show you how many of these fixes (whether complete or incomplete) inevitably lead to lower CPU performance.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 64: Fixing Meltdown and Spectre

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
