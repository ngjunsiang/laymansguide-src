Title: Issue 140: The shared memory dream
Date: 2021-10-02 08:00
Tags: 
Category: Season 11
Slug: lmg-s11-issue-140-the-shared-memory-dream
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Around 2015, the high-performance computer industry quickly realised that this would be much more efficient if the CPU and GPU could *share the same memory*. This idea was labelled heterogeneous systems architecture (HSA).

Let’s rewind a bit further from last issue. That was in 2015.

Circa 2009, changes were happening on the desktop motherboard, as the memory controller hub (MCH) came on-board the CPU to reduce latency when communicating with memory ([Issues 134]({filename}/season11/issue134/issue134.md))–[135]({filename}/season11/issue135/issue135.md))). But the memory chips themselves remained on the motherboard, and this was the case even in 2018, in Apple’s Macbook Air ([Issue 136]({filename}/season11/issue136/issue136.md))).

## Bringing memory on-board

Smartphones can’t afford to do that; every bit of mainboard space is precious! The Apple A-series processors have been gradually moving more and more memory into the CPU, where it enjoys lower latency communicating with the CPU.

In 2013, Apple released the iPhone 5S, using the Apple A7 SoC. This was Apple’s first 64-bit SoC ([Issue 55]({filename}/season5/issue055/issue055.md))), and by this point Apple had managed to bring 1GB of memory onto the SoC package. By 2018, With the Apple A12 SoC, the on-board memory had increased up to 4GB on high-end iPhone X models.

So in 2015, the high-performance folks (working with workstations and servers) were dreaming of the CPU and GPU sharing memory, while from 2013, in smartphones, the CPU, GPU, and system memory were already cohabiting in the same chip package! CPU, GPU, and memory all living in the same space … how does this work?

## Memory: yours or mine?

Remember this diagram?

![Chipset diagram of ATX systems for Intel Core (i-Series)]({attach}/season11/issue134/issue134_02.gif)<br />
<small>An Intel Core i-series ATX system chipset diagram.<br />The MCH is merged into the CPU, but still a discrete unit.<br />DDR refers to computer memory, while GDDR refers to graphics card memory ([Issue123]({filename}/season10/issue123/issue123.md)))<br />Source: [Ars](https://arstechnica.com/gadgets/2009/09/intel-launches-all-new-pc-architecture-with-core-i5i7-cpus/)</small>

Apple is pretty tight-lipped about the technical details of its products, but if the industry standard is anything to go by, the GPU will usually have its own memory, separate from the CPU.

After all, CPUs and GPUs don’t do the same work, or even work the same way ([Issue 123]({filename}/season10/issue123/issue123.md))). They use different memory, they use memory differently, they store data differently, and if they accidentally overwrote each other’s data … well, your device would just crash.

So … that on-board memory, whose is it? CPU’s, or GPU’s?

## Successful sharing looks like ...

One thing that makes it difficult to share memory is that the CPU and GPU have to “speak the same language”; they need a common shared understanding of the workflow involved in passing data through shared memory.

This is easier to develop when a single company has control over both CPU and GPU designs. This is not always the case; many smartphones have CPU designs from one company and GPU designs from another!

For instance, the Apple A-series processors initially used GPUs from a graphics company called Imagination Technologies, designed by their PowerVR division. With a CPU and GPU from different teams, working in different ways, shared memory is not likely to happen[^1].

[^1]: What about other companies that had control over the CPU and GPU designs? Such as AMD, Samsung, Qualcomm, ...? It’s a long story, and not really suitable for a layman newsletter. Sorry.

But in the A10 SoC, released in 2016, Apple had subtly started to replace parts of the GPU with their own in-house designs. The A10 would be the last in the line of the “Fusion” SoC series.

When the A11 SoC was released in late 2017—first in the “Bionic” series of SoCs—PowerVR’s GPU had been replaced by Apple’s own design[^2].

[^2]: The design is technically Apple’s, but they had been learning from many generations of working with PowerVR’s GPU, so the early initial designs are very likely heavily influenced by it.

Apple is finally in the position of working towards shared memory with their Bionic-series SoCs, with the A14 being the fourth “Bionic” SoC.

**Issue summary:** Shared memory is easier to implement when a company has control over the designs of both CPU and GPU.

The story which began in [Issue 138]({filename}/season11/issue138/issue138.md)) is coming to a close soon! Next issue, the curtain falls, the A14 and M1 are released, and Apple (probably) pulls the chip industry in a new direction again.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 141: The Apple A14 and M1

And finally I can geek out over the A14 and M1 😎 don't worry, I’ll keep it on-topic.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
