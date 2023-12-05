Title: Issue 133: the ATX form factor (post-1995)
Date: 2021-08-14 08:00
Tags: 
Category: Season 11
Slug: lmg-s11-issue-133-the-atx-form-factor-post-1995
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Chipsets served as go-betweens in the AT form factor by IBM.

In 1993, Intel launched its Pentium line of processors; barely two years later, in 1995, Intel launched the ATX form factor. This was the beginning of Intel’s dominance in the desktop space, and they could well afford to dictate most of the standards for this form factor.

## Chipset diagram

Mainboards at this point were complicated enough that as part of the marketing, tech publications had taken to staring at diagrams of how the chips were connected. These diagrams are called **chipset diagrams**.

This is the chipset diagram of a typical mainboard for the Pentium 4:

![Chipset diagram of a mainboard for the Pentium 4]({attach}issue133_02.jpg)<br />
<small>I tried to find a chipset diagram that used human terms instead of acronyms.<br />This is the best I could do. Annotations my own.<br />Source: [Hexus](https://www.hexus.net/tech/reviews/mainboard/635-sis655fx-dual-channel-p4-chipset/?page=2)</small>

The **memory controller hub** (MCH) now takes on a much bigger role; it is managing data transfer between the CPU, graphics card, computer memory, *and* the PCH.

The **peripheral controller hub** (PCH), while managing connections to many more devices, actually has less work to do; these are all low-throughput devices that don’t send much data to the CPU.

## ATX mainboard

And this is where the components are found on the motherboard:

![A mainboard for the Pentium 4]({attach}issue133_01.jpg)<br />
<small>A motherboard for the Pentium 4, with key components outlined.<br />Annotations are my own.</small>

The CPU clearly draws the most power and produces the most heat here. But notice now that the MCH is no longer bare; it now produces so much heat ([4–10 W](https://hexus.net/tech/news/mainboard/132515-der8auer-examines-amd-x570-chipset-power-consumption/)) that it needs to be passively cooled with a heatsink ([Issue 129]({filename}/season10/issue129/issue129.md)). the PCH, on the other hand, is still chill enough to get by bare naked (4 W or less).

3D graphics at this point is a rapidly growing industry, especially for videogames. Graphics cards needed much more throughput to the CPU and memory, so the MCH grew to fit into this role as the mediator between these throughput-hungry components

**Issue summary:** The ATX form factor also brought with it a new breed of computers with more specialised chipsets: the memory controller hub (MCH) and peripheral controller hub (PCH). The MCH coordinates high-throughput components, such as computer memory and graphics. The PCH specialises in lower-throughput needs.

Much as I try to avoid using acronyms, here they are really just easier to read.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 134: Part 1 – the Intel Core i-series launches!

I don’t know if you noticed, but there seem to be fewer chips here than on the AT board. That’s misleading though; the components that were on the AT board are also on the ATX board, but greatly shrunk. Some of the functionality that used to require multiple chips on AT have been replaced by a single chip in ATX, hence the appearance of simplicity. In reality, the ATX mainboard is more complex!

Next issue, onward with the integration!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
