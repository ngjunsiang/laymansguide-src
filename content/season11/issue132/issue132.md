Title: Issue 132: the AT form factor (pre-1995)
Date: 2021-08-07 08:00
Tags: 
Category: Season 11
Slug: issue132
Author: J S Ng
Summary: 
Modified: 2021-08-07 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) CPUs have limited throughput, since there is a max frequency they can operate at, and a limit to the number of wires they can be connected to (throughput = no. of wires × frequency). Later designs of early computers increased the capability of computers by delegating more work to secondary chips.

When computers began hitting the mainstream market, they were designed to be able to use interchangeable parts so as to reduce cost and inventory. To support this effort, manufacturers came up with standards for how to lay out computer components on a mainboard; the different patterns came to be known as **form factors**.

The AT form factor, by IBM, is one of the early ones. An AT motherboard looks something like this:

## The AT mainboard

<figure>
    ![An AT motherboard]({attach}/season11/issue132/issue132_01.jpg)
    <figcaption>An AT motherboard, with key components outlined.<br />Annotations are my own.<br />Original: [Wikipedia](https://en.wikipedia.org/wiki/Skylake_(microarchitecture))</figcaption>    
</figure>

Graphics cards, usually added as an expansion card, communicated with the CPU (under the heatsink) through a chipset, while the CPU communicated with memory through another chipset.

At this point, graphics were still barely powerful enough to run 3D graphics (this was before Windows 95!), and the chipsets mainly served as go-betweens between memory, expansion slots (called buses), and the CPU.

After 1995, this would change.

**Issue summary:** Chipsets served as go-betweens in the AT form factor by IBM.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 133: the ATX form factor (post-1995)

Short issue here, just to introduce the idea of chipsets! You can see the chips on the AT board look very similar. On the ATX form factor, they will begin to differentiate and specialise.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
