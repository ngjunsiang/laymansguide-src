Title: Issue 141: The Apple A14 and M1
Date: 2021-10-09 08:00
Tags: 
Category: Season 11
Slug: issue141
Author: J S Ng
Summary: The Apple A14 and Apple M1 are essentially the same chip architecture: they use almost the same building blocks, just with different numbers of them. On top of that, the Apple M1 implements unified memory, allowing the CPU and GPU (and other SoC components) to share the same system memory, greatly facilitating intra-chip communication.
Modified: 2021-10-09 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Shared memory is easier to implement when a company has control over the designs of both CPU and GPU.

So, to recap:

Most companies design either CPUs or GPUs, but seldom are well-positioned[^1] to be excellent in both.

[^1]: Companies that achieve both CPU and GPU excellence generally have business incentives that align with that goal (as opposed to, say, making low-power or cheap processors)

Among the companies that design both CPUs and GPUs, almost none of them[^2] make CPUs for both mobile (smartphones + tablets) as well as laptops (including low- to mid-range desktops).[^3]

[^2]: Intel had a short-lived but ultimately doomed attempt at a smartphone chip (it was named Medfield).

[^3]: I‘m going to ignore servers here because I can! And because they’re not really relevant to a discussion on low-power consumer chips.

Which leaves Apple in the (current) position of being the only chip company with a design for both mobile as well as laptop.

## The difficulties of power scaling

It’s not that other companies have not attempted this.

They have tried to scale down laptop chips to achieve smartphone-like power consumption, but found that laptop chips can’t power down the way smartphone chips can, and require more circuitry to achieve that.

They have also tried to scale smartphone chips up to achieve laptop-like computational capacity, but found that simply pushing more electrical power doesn’t help all that much. Beyond a certain frequency limit, you simply need more bandwidth and more units, and designing a chip that easily accommodates more units like this just requires a very different design.

It seems that designing a chip that can go from 4W all the way to 65W (and possibly higher) requires intentional engineering, not simply modifying an existing smartphone/laptop chip design or bolting on/removing features.

## The Apple A14 vs the Apple M1: similarities

Apple has managed to do just this with the Apple A14 and M1. They are, at heart, the same chip design! (In processor parlance, we say they have the same **chip architecture**.)

Let’s see:

![Apple A14 hardware overview]({attach}/season11/issue141/issue141_01.jpg)  
*The Apple A14’s key hardware.<br />Source: [Apparently an online Arabic image gallery site](https://www.electrony.net/350867/%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%84%D8%AC-apple-a14-bionic-%D9%82%D8%AF-%D9%8A%D9%88%D9%81%D8%B1-%D8%A3%D8%AF%D8%A7%D8%A1%D9%8B-%D9%85%D9%85%D8%A7%D8%AB%D9%84%D8%A7%D9%8B-%D9%84%D8%A3%D8%AF%D8%A7/apple-a14/) (I have no idea why this picture is so hard to find!)*    

![Apple M1 hardware overview]({attach}/season11/issue141/issue141_02.jpg)  
*The Apple M1’s key hardware.<br />Source: [TechBuzzPro](https://www.techbuzzpro.com/apple-introduces-m1-5nm-octa-core-soc-for-the-mac.html)*    

We can also compare these features via Wikipedia:

**Apple A14**

- 6-core CPU (4 low-power[^4] cores “Icestorm”, **2** high-performance “Firestorm” cores)
- **4**-core GPU
- **8**-core NPU
- 4GB memory (iPhone 12) / 6GB memory (iPhone 12 Pro)

[^4]: These are the same ones labelled “high-efficiency”, which is marketing speak for “designed to use very little power”

**Apple M1**

- 8-core CPU (4 low-power[^4] cores “Icestorm”, **4** high-performance “Firestorm” cores)
- **8**-core GPU
- **16**-core NPU
- 8GB memory / 16GB memory

Notice that at heart, they are using the same building blocks: ~~low-power~~ high-efficiency cores, high-performance cores, GPU cores, and NPU cores (I suspect these are GPU-like cores but optimised for machine learning, i.e. they probably power Siri and other parts of the OS which lean on AI features); the A14 and M1 just has different numbers of them.

So one really amazing thing about the Apple M1 is that it is actually a boosted Apple A14: almost double the hardware!

It’s like when Magnemites join together and evolve into a Magneton …

## The Apple A14 vs the Apple M1: differences

What’s different between the A14 and M1, besides the number of key chips? Apple isn’t forthcoming with the details, but we can guess about minor details like the image processor (for camera imaging), storage controller (the M1 can use high-power solid-state disks (SSDs) which the A14 can’t).

The major difference announced between the A14 and M1 launch is that the M1 has unified memory.

## Unified memory vs CPU–GPU transfers

Back in [Issue 139]({filename}/season11/issue139/issue139.md)), I mentioned that unified memory needs really high bandwidth to support access by the SoC components.

Today, laptop processors use an interface called PCIe to connect CPUs to GPUs. PCIe has a bandwidth of up to 16 GB/s[^5].

[^5]: Bandwidth of 16 GB/s is for PICe 3.0; PCIe 4.0 will support up to 32 GB/s, but graphics cards won’t use that much bandwidth to communicate with the CPU.

The M1’s unified memory has a bandwidth of up to *58 GB/s* reading from memory, and *36 GB/s* writing to memory. Definitely an improvement.

## Unified memory: what’s yours is also mine

The 8GB/16GB of system memory is used by both CPU and GPU. It is not partitioned at boot; both the CPU and GPU (and other parts of the SoC, such as the NPU) have *full access to all system memory*.

This greatly simplifies intra-chip communication, as all subchips in the SoC can request access to memory! The GPU no longer needs to keep its own (power-guzzling) memory. This reduces the motherboard space that is needed, lowers power consumption, and decreases latency for data transfer between CPU and GPU ([Issue 139]({filename}/season11/issue139/issue139.md))): a triple-compounding win.

**Issue summary:** The Apple A14 and Apple M1 are essentially the same chip architecture: they use almost the same building blocks, just with different numbers of them. On top of that, the Apple M1 implements unified memory, allowing the CPU and GPU (and other SoC components) to share the same system memory, greatly facilitating intra-chip communication.

Some implications of the Apple A14–Apple M1 familial connection: the Apple M1 is truly capable of smartphone-like standby, a feature that Intel’s and AMD’s laptop chips have been striving for but not quite achieved.

It’s a lot to detail here, so instead I will do so—in a separate issue.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 142: Implications (Part 1) - Software

Besides the reported fact that the M1 is really very fast (and yes I will spend a little time explaining just how fast), what else does this herald for expectations in the software on devices? Coming up next issue :)

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
