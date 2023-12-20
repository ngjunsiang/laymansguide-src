Title: Issue 55: Addressing memory
Date: 2020-01-11 08:00
Tags: cpu, memory
Category: Season 05
Slug: issue055
Author: J S Ng
Summary: 
Modified: 2020-01-11 08:00

**Previously:** To get useful output from a CPU, we must translate the operations we want it to perform into CPU instructions, in a process known as **compiling**. Most compilers convert programming code into CPU instructions.

A CPU executes instructions, which loads data from memory, store data to memory, or carries out operations on loaded data. Where exactly does this data go, and how is it organised?

## Memory is a collection of bytes organised by address

In Season 4, I mentioned the byte as a convenient collection of 8 bits. Part of the reason is that memory is organised by bytes. Each byte of memory has its own address. Naturally, in a CPU, this memory address will be encoded in binary.

Working out the numbers, a CPU will need 10-bit memory addresses to use 1 KiB of memory (2^10 = 1,024). 20-bit addresses will let it use 1 MiB of memory (2^20 = 1,048,576). 30-bit addresses will let it use 1 GiB of memory (2^30 = 1,073,741,824). And 32-bit addresses will let a CPU use 4 GiB of memory.

Are those numbers ringing a bell?

## The 32-bit to 64-bit transition in the ’00s

A little history, for those who remember: Around the turn of the century, in the ’00s, there was some hoo-ha about 32-bit CPUs not being able to use more than 4 GiB of memory; this was a time when 2 GiB of memory on a laptop was considered beefy, Google Chrome hadn’t appeared on the scene yet, and browsers did not use up gobs of memory.

This was also a time when 64-bit CPUs started coming onto the scene, and there was much confusion in the software world about which software would work on 32-bit CPUs, which ones would work on 64-bit CPUs, and which ones would work on both.

So this is what it boils down to: a 32-bit CPU, without any hacky workarounds, can only work with about 4 billion memory addresses. and this became insufficient around the turn of the century. We needed to use CPUs that could work with more than 4 billion addresses. 64-bit CPUs were the solution that the computing industry settled on. 64-bit memory addresses would extend the addressable memory capacity to 16 TiB for the foreseeable future.

## 16 TiB?! Why do we need so much memory?

Hold your horses — I want to be clear here. I’m not just talking about memory here, but about **memory addresses**. What’s the difference? Consider for a moment how the CPU would transfer data to the hard drive. Or send data to a printer. Or even send it out onto the network. How would those virtual “locations” be represented in a CPU instruction that can only handle memory addresses?

The most straightforward answer, which you may have some difficulty accepting, is that they are simply represented as memory addresses. Yep, in the entire space of memory addresses, most of it is used to address physical memory (what is known as **R**andom **A**ccess **M**emory, or **RAM**), while some of it is used to address hard drive devices, USB devices, network devices, and various other connected peripherals.

## Of instructions and addresses

Let’s summarise the picture so far.

**Issue summary:** The life of the unconscious CPU is just executing instruction after instruction after instruction. Each instruction may consist of loading data from a memory location, sending data to a memory location, or performing operations on the data it is holding.

Not a very interesting life, but it forms the bedrock which supports everything we use a computer for. And things are about to get more complex once we throw programs into the picture. Each program is its own long list of CPU instructions, meant to produce different results. Excel carries out our spreadsheet processing, while Word helps us to format our documents. Yet the instructions from both programs are carried out in the same CPU! How does the CPU avoid mixing up data from different programs? How does it prevent Word from accidentally screwing up Excel’s data, and vice-versa?

## What I’ll be covering next

**Next issue:** Operating Systems and resource management

Okay, I think I’ve laid out the basics of CPU operation in sufficient detail for now. I have yet to mention one key component—the CPU cache. And I have yet to explain how CPUs speed up processing. These two explanations will make more sense after I make a side trip about how operating systems prevent everything from becoming one gigantic mess.

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
