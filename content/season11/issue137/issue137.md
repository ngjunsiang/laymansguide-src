Title: Issue 137: The M1 Macbook Air
Date: 2021-09-11 08:00
Tags: 
Category: Season 11
Slug: issue137
Author: J S Ng
Summary: 
Modified: 2021-09-11 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Slim laptops have been undergoing a gradual transition: more and more of their chips are no longer available as a replaceable card, but instead soldered directly to the mainboard. Since 2017/2018, most slim laptops pretty much have CPU, memory, storage, and network chips all soldered directly to the mainboard.

Let’s get to it: Intel vs M1 Macbook Air!

## The 2020 Macbook Air: passing the torch

Here’s the Macbook Air in 2020. There was one in early 2020 using an Intel Core CPU, and one in late 2020 using the Apple M1 CPU.

![Macbook Air in early 2020 (left), vs late 2020 (right)]({attach}/season11/issue137/issue137_01.jpg)  
*Macbook Air, early-2020 (Intel, left) vs late-2020 (M1, right)<br /><br />Source: [iFixit](https://www.ifixit.com/News/46884/m1-macbook-teardowns-something-old-something-new)*    

They look almost identical, but some parts are noticeably different … can you spot the differences?

1. The cooling fan (upper left) is there in the early 2020 (Intel) model, but gone in the late 2020 (M1) model.
2. Besides the CPU (upper centre in both models, under a heatsink), the Intel model has a mysterious-looking chip (upper right, covered in black shrouding)

You may have spotted other differences in the hardware, but since this issue is focused on the mainboard and CPU, let’s zoom in on those. Let’s have a closer look at their mainboards:

![2020 Intel Macbook Air mainboard, front(left) vs back (right)]({attach}/season11/issue137/issue137_04.jpg)  
*2020 Intel Macbook Air mainboard, front and back<br />The Intel CPU unfortunately sits under the huge heatsink, shown with its 4 securing screws<br />Memory and solid state disk are on separate chips (most likely on the back)<br />Source: [iFixit Store](https://www.ifixit.com/Store/Mac/MacBook-Air-13-Inch-Early-2020-1-1-GHz-Core-i3-Logic-Board-with-Paired-Touch-ID-Sensor/IF188-152?o=1)*    

![2020 M1 Macbook Air mainboard, front (left) vs back (right)]({attach}/season11/issue137/issue137_02.jpg)  
*2020 M1 Macbook Air mainboard, front and back<br />There are fewer big chips, but the single biggest chip there is *much* bigger, and Apple-branded<br />Memory is integrated into the CPU, but the solid state disk sits on a separate pair of chips<br />Source: [iFixit](https://www.ifixit.com/News/46884/m1-macbook-teardowns-something-old-something-new)*    

## The M1 Macbook Air: all aboard

Overall, it looks like the M1 has “swallowed” a number of chips. Compared to the 2020 Intel model, the M1 has brought on-board computer memory (the two black chips on the M1), and Apple’s T2 chip (the back shrouded chip on the 2020 Intel Macbook Air). These are major components for computer operation.

So not only does the M1 incorporate more components, it does so while drawing less power—the lack of a cooling fan implies it is passively cooled. From [Issue 129]({filename}/season10/issue129/issue129.md)), this suggests the M1 Macbook Air also uses less power (8–12W) for its tasks. And reviews for the Macbook M1 Air suggest it is not being thermally throttled except under the heaviest of loads.

How did Apple manage to design a processor like this?

## The Apple M1: evolved from a smartphone chip

To get into that story, I’ll have to go even more mobile, and look at smartphone CPUs. After all, the Apple M1 actually evolved from the Apple A-series CPUs for their iPhone and iPad. That starts next issue.

## What about other Intel Core laptops running Windows?

They are largely undergoing the same transition, just more slowly. This is the Microsoft Surface Laptop in 2017:

![Microsoft Surface Laptop (2017) mainboard]({attach}/season11/issue137/issue137_03.jpg)  
*Microsoft Surface Laptop mainboard<br />CPU(red), memory (orange), solid state disk (yellow), and network card (green) are all soldered on. (Outlined in cyan are the display control chips)<br />Source: [iFixit](https://www.ifixit.com/Teardown/Microsoft+Surface+Laptop+Teardown/92915)*    

Larger-sized laptops that can afford the space may still have solid state storage on a separate card.

**Issue summary:** The M1 goes one step further: not only does it make do with fewer chips, it does so with passive cooling!

The last issue simply went on too long, especially with all the images, so I figured this issue would stand better as a Core-vs-M1 comparison, instead of being the tail of an evolution-of-Air issue. So it’s short.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 138: System-on-Chip (SoC)

If smartphones are even smaller than laptops, how do they do it? Laptops seem to have exhausted all the tricks, and those boards still look pretty big.

Next issue, I’ll talk about the next step in the evolution of shrinking mainboards.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
