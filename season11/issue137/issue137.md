[**Previously:**](https://buttondown.email/laymansguide/archive/) Slim laptops have been undergoing a gradual transition: more and more of their chips are no longer available as a replaceable card, but instead soldered directly to the mainboard. Since 2017/2018, most slim laptops pretty much have CPU, memory, storage, and network chips all soldered directly to the mainboard.

Let’s get to it: Intel vs M1 Macbook Air!

## The M1 Macbook Air: all aboard

Here’s the Macbook Air in 2020. There was one in early 2020 using an Intel Core CPU, and one in late 2020  using the Apple M1 CPU.

![Macbook Air in early 2020 (left), vs late 2020 (right)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue137/issue137_01.jpg)<br />
<small>Macbook Air, early-2020 (Intel, left) vs late-2020 (M1, right)<br />The cooling fan is noticeably missing in the late-2020 model.<br />Source: [iFixit](https://www.ifixit.com/News/46884/m1-macbook-teardowns-something-old-something-new)</small>

The M1 not only performs better, it does so while passively cooled! From [Issue 129](https://buttondown.email/laymansguide/archive/lmg-s10-issue-129-cooling/), this suggests the M1 Macbook Air also uses less power (8–12W) for its tasks.

![2020 M1 Macbook Air mainboard, front (left) vs back (right)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue137/issue137_02.jpg)<br />
<small>2020 M1 Macbook Air mainboard, front and back<br />There are fewer big chips, but the single biggest chip there is *much* bigger, and Apple-branded<br />Memory is integrated into the SoC, but the solid state disk sits on a separate pair of chips<br />Source: [iFixit](https://www.ifixit.com/News/46884/m1-macbook-teardowns-something-old-something-new)</small>

It looks like the M1 has “swallowed” a number of chips! Here’s the 2020 Intel Macbook Air mainboard for comparison:

![2020 Intel Macbook Air mainboard, front](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue137/issue137_04.jpg)<br />
<small>2020 Intel Macbook Air mainboard, front<br />The Intel SoC unfortunately sits under the huge heatsink, shown with its 4 securing screws<br />Not visible here are the memory and solid state disk, on separate chips<br />Source: [iFixit Store](https://www.ifixit.com/Store/Mac/MacBook-Air-13-Inch-Early-2020-1-1-GHz-Core-i3-Logic-Board-with-Paired-Touch-ID-Sensor/IF188-152?o=1)</small>

Compared to earlier Macbook Air mainboards, there are fewer chips in both the Intel and M1 Macbook Air, and the CPU is much larger. What does this mean?

## The Apple M1: evolved from a smartphone chip

To get into that story, I’ll have to go even more mobile, and look at smartphone CPUs. After all, the Apple M1 actually evolved from the Apple A-series CPUs for their iPhone and iPad. That starts next issue.

## What about other Intel Core laptops running Windows?

They are largely undergoing the same transition, just more slowly. This is the Microsoft Surface Laptop in 2017:

![Microsoft Surface Laptop (2017) mainboard](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue137/issue137_03.jpg)<br />
<small>Microsoft Surface Laptop mainboard<br />CPU(red), memory (orange), solid state disk (yellow), and network card (green) are all soldered on. (Outlined in cyan are the display control chips)<br />Source: [iFixit](https://www.ifixit.com/Teardown/Microsoft+Surface+Laptop+Teardown/92915)</small>

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
