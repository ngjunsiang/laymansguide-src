**Previously:** The operating system is responsible for listing and managing the computers resources, making them available to programs running on the computer, and making sure they only use what they are allowed to.

Those who have been following Layman’s Guide since Season 3 will remember this term, **caching**. I first introduced it at the end of Season 3, in [Issue 39](https://buttondown.email/laymansguide/archive/lmg-s3-issue-39-caches-and-caching/):

> Searching for anything takes time. Need to fill out a form? You need to search for a pen first. Need to call someone? Before speed dial and contacts apps existed, You used to need to look up a number in order to dial it. If you do it often enough, you would make sure you always had a pen with you, or you would write the number somewhere convenient for you to see so you don’t need to hunt for it.

> Computers use the same trick, and it is called **caching**. Any information it needs repeatedly which is unchanging is stored in a **cache**.

The DNS cache, which I introduced in that issue, is a place where hostnames (such as facebook.com) and their associated IP addresses are stored, so that we don’t need to keep looking up the IP address for facebook.com.

We use caches to reduce latency and speed up processing: the full DNS querying process takes a few hundred milliseconds, but looking up a DNS entry in the cache only takes a few milliseconds — that’s a speedup by a factor of 100!

## How long does it take to transfer data?

Let’s look at the transfer speeds and latencies for a few places where data can be stored:

- Hard disk drive (HDD): ≈5 ms response latency, 100 MB/s transfer speed
- Solid state disk (SSD): up to 0.1 ms response latency, 0.5–1+ GB/s transfer speed
- Physical memory (RAM): 0.1 µs (0.0001 ms) response latency, 20GB/s transfer speed
- CPU register: <1 ns (<0.000001 ms) response latency[^1]

[1]: We seldom talk about the transfer speed of CPU registers, because each register only holds one byte and the transfer is near-instantaneous.

A CPU register is a slot within the CPU (the same slots from [Issue 53](https://buttondown.email/laymansguide/archive/lmg-s5-issue-53-the-cpu-is-an-instruction-obeying/)) which it uses to hold the data it is processing.

Notice that the speed difference between each layer is more than 10×? If a computer did not have physical memory to store temporary data in, and had to transfer data to/from disk, it would be responding a thousand times more slowly!

A CPU can carry out operations very quickly on data loaded into its registers; it generally takes only a few nanoseconds for complex calculations to be done. Simple instructions (such as ADD) can even be done in less than 1 ns!

This means that the limiting factor for CPU speed is actually loading and storing data. In the time it takes to load data from physical memory or store data to physical memory, it can perform 100 simple operations. That’s *damn slow* in CPU time!

## CPU and cache performance

So CPU designers included some cache on the CPU:

- CPU cache: 0.001–0.040 µs response latency, 175 GB/s transfer speed

Great, now we have some storage space that sits between physical memory and the CPU’s registers. It is only slightly slower that a CPU register, and much faster than physical memory.

Imagine working in an office that gave you a cubicle but no desk. When you need a piece of information, you have to go down the hallway to the filing cabinet, retrieve it, and return to your cubicle (no desk!). When you were done processing it (1 second), you had to put the results back in the filing cabinet, down the hallway … a process that takes about 100 seconds. SLOWWWWW!

If you had a desk, you could put some papers on it, and retrieve them much more quickly (a few seconds). You would be 10× more efficient!

By simply including a cache on the CPU, its designers sped up its performance by a factor of more than 10.

## Cache is not managed by the OS

Just as an organisation would not control what information you should have on your desk, an operating system does not control the CPU cache. This feature is managed entirely by the CPU itself. The operating system is unable to see what is in the CPU cache, and has no access to it.

Like other caches, when the CPU needs data from a memory address, it looks in the cache first. If the data is not there (a **cache miss**), it will load the data from the memory address, and store a copy in the cache for faster reference in future.

Like other caches, this process has its own issues. the cache can fill up, requiring the CPU to eject old data so as to make way for fresher data. The cached data on the CPU cache can also become outdated when other programs and instructions update the data in memory. Programs that absolutely need to ensure they get the freshest data from memory can issue special instructions to perform a **cache flush** and **cache reload**.

A cache flush empties out the cached data while preserving the memory address it is linked to. A cache reload, well, reloads the data from those memory addresses. These two terms, jargon for very technical operations that take place in the CPU, are being introduced because they are the linchpin of Meltdown and Spectre. We will get there in the next two issues.

**Issue summary:** The CPU stores data for ready access in the CPU cache. Accessing data from the CPU cache is much faster than accessing data from memory. When the CPU needs data from a memory address, it looks in the cache first. If the data is not there (a **cache miss**), it will load the data from the memory address, and store a copy in the cache for faster reference in future. The CPU cache is managed by the CPU and is invisible to the OS. Programs that need to ensure the data in the cache is “fresh” can perform a cache flush and reload.

If CPU development had stopped at this point, Meltdown and Spectre would not have been possible … and we would have been stuck in the ’90s, somewhat. It is in human nature to try to exploit every last bit of available optimisation, and this is what happened with the design of CPUs.

As new manufacturing processes allowed computer engineers to cram more transistors into a CPU, the question arose: what should we do with more transistors? Just add more calculation units? Build new features into the CPU?

Adding more calculation units made the design of CPUs much more complex (as anyone who has had to work alongside other team members doing the same job can attest). The most popular optimisations thus hinged on adding CPU features to ensure that it is fully utilised as much as possible.

In the next two issues, I will do a shallow dive into two of these features: out-of-order processing, and speculative execution. These will not be technical issues, because there are ready human analogues for such optimisations. You probably already do some of this at work, or even at home!

## What I’ll be covering next

**Next issue:** CPU Optimisation Part 1 – Out-of-Order Execution

Out-of-order execution is a solution that we have all discovered at one point or other in our lives. When we have to manage multiple tasks and carry each one out as quickly as possible, we don’t always carry out the steps in a logical order, but in a manner that makes sense and lets us work as quickly as possible.

CPUs do this as well, to perform calculations much more quickly. More in the next issue of Layman’s Guide.

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
