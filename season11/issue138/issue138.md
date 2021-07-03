[**Previously:**](https://buttondown.email/laymansguide/archive/) The M1 goes one step further: not only does it make do with fewer chips, it does so with passive cooling!

In Issue 136, I showed the miniaturisation of the Macbook mainboard through a series of pictures. While the laptop has remained the same size mostly (apart from getting slimmer), that is not the case with its components. The bigger components, like memory and storage, changed from being separate discrete parts to being another component soldered directly to the mainboard.

But that only gets us so far; even in the M1 Macbook Air, the mainboard is still almost the entire length of a phone. There’s got to be something else.

Today, let’s see how the iPhone has evolved.

## What’s in a smartphone: 2008

Rewind to 2008: one year after the first-generation iPhone was launched, the iPhone 3G was released. These early smartphones let us see every little chip that was required to run a smartphone:

![iPhone 3G mainboard, with parts labelled](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_01.jpg)<br />
<small>iPhone 3G mainboard, with parts labelled<br />There are lots of small, auxiliary processors around the CPU.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+3G+Teardown/600)</small>

In spirit and form, the early smartphone were a lot like the early desktop mainboards ([Issue 132]()): lots of chips performing highly specific functions. A smartphone has no need (or space) for a peripheral controller hub (PCH) ([Issue 134]()) when it does not have add-on peripherals, and no need for a memory controller hub (MCH) when it can put the memory directly on the same chip as the CPU.

At this point, Apple was still using a CPU based on a design by ARM, and manufactured by Samsung. 2 years later, Apple had its own in-house processor: the Apple A4, their own design.

## What’s in a smartphone: 2010

This time round, Apple had switched to an internal layout distinctly different from the iPhone 3G, and the basic layout (mainboard beside battery) would become a pattern for subsequent iPhone generations.

![iPhone 4 and iPhone 12](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_02.jpg)<br />
<small>iPhone 4 on the left, iPhone 12 on the right<br />The basic layout of hte iPhone has been preserved over a decade.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+4+Teardown/3130) and [iFixit](https://www.ifixit.com/Teardown/iPhone+12+and+12+Pro+Teardown/137669)</small>

What’s the difference between this and the 3G? Let’s have a look at the iPhone 4’s mainboard:

![iPhone 4 mainboard](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_01.png)<br />
<small>iPhone 4 mainboard. I got lazy with the labelling because, well, there’s nothing to label!<br />The CPU is the huge chip labelled “A4”, and there’s memory and the 3G chip on the back.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+3G+Teardown/600)</small>

Similar to the transition from AT to ATX motherboards ([Issue 132]() and [134]()), the iPhone underwent a great miniaturisation—in a single generation!

## System-on-Chip

What happened to all those separate chips? They all got moved *onboard*, into the A4 chip, or other auxiliary chips. The great consolidating brought all their functionality under one roof.

The A4 chip carries:

- CPU[^1]
- GPU
- MCH
- PCH

[^1]: The CPU carries (some) onboard memory for itself, but the main bulk of memory is still on the mainboard.

This chip is responsible for:

- performing calculations
- rendering graphics ([Issue 123]())
- managing the flow of information between CPU, GPU, and memory (previously the job of the MCH)
- managing the flow of information between storage, network, and the MCH (previously the job of the PCH)

It is literally an entire system on a chip: a **system-on-chip** (SoC)!

More educational perhaps would be to look at what’s *not* included in the SoC, particularly when we get the the iPhone 12’s SoC, called the A14.

Not on the A14 SoC:

- solid state disk (in a single chip)
- power management
- 4G & 5G
- audio

The above functionality is highly specialised, especially in modern[^2] smartphones. It manages the remaining parts of the phone: camera & mic/speakers, wifi & bluetooth, and telecommunications (4G/5G). Telecommunications in particular require a lot of power and would have contributed to unnecessary heating in the small CPU package.

[^2]: I know it’s strange to differentiate older vs newer smartphones when the technology is barely more than a decade old. But the evolution of smartphone designs over the course has been significant enough that yes, I am going to make this distinction :)

And this is how we shrink a laptop mainboard even further.

**Issue summary:** A system-on-chip (SoC) combines the core functionality of a system—processing, graphics, memory, and control—into a single chip package.

## What I’ll be covering next

The M1’s design shares a lot more in common with the A14 on the iPhone and iPad than it does with the laptop CPUs that came before it. I want to go into a bit more detail about this in the next issue, so that it’s easier to see just how different it is from a typical laptop.

First thing to talk about: what exactly does “unified memory” mean? Why is it a big deal?

**Next issue:** [LMG S10] Issue 139: What’s before this line is mine, what’s after this line is yours

Next issue, we look at a trend that started being reported on in 2015: the high-performance computing industry realised that the CPU and GPU need to have much more integrated memory sharing.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
