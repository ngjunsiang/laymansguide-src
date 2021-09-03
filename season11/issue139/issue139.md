[**Previously:**](https://buttondown.email/laymansguide/archive/) A system-on-chip (SoC) combines the core functionality of a system—processing, graphics, memory, and control—into a single chip package.

I am eager to dig into the meat of the A14 and M1! But first I must set up a story.

## The hUMA race

Circa 2015 (actually even a couple of years before that), the industry suddenly seemed to wake up and realise that graphics cards could do a lot more than just play video games. The nature of how they work ([Issue 121](https://buttondown.email/laymansguide/archive/lmg-s10-issue-121-in-graphic-detail/) & [122](https://buttondown.email/laymansguide/archive/lmg-s10-issue-122-the-great-flattening/)) makes them very amenable to solving problems in scientific computing, particularly in simulations, which use up computational resources by the petaflop, and energy by the megawatt.

In a nutshell, the problem the industry now faces is this:

1. The GPU is massively powerful ... at doing a small subset of things. You can solve scientific equations but can’t run a computer with *only* a GPU.
2. The CPU is nimble, and much more suited for everyday tasks, like starting up a computer and connecting to multiple peripherals, and basically creating a useable digital environment for humans.
3. It thus makes the best sense to use the CPU to set up the heavy-lifting for the GPU, and have the GPU return the results after computation.

Remember this diagram from [Issue 134]([**Previously:**](https://buttondown.email/laymansguide/archive/) The M1 goes one step further: not only does it make do with fewer chips, it does so with passive cooling.

In [Issue 136](), I showed the miniaturisation of the Macbook mainboard through a series of pictures. While the laptop has remained the same size mostly (apart from getting slimmer), that is not the case with its components. The bigger components, like memory and storage, changed from being separate discrete parts to being another component soldered directly to the mainboard.

But that only gets us so far; even in the M1 Macbook Air, the mainboard is still almost the entire length of a phone. There’s got to be something else.

Today, let’s see how the iPhone has evolved.

## What’s in a smartphone: 2008

Rewind to 2008: one year after the first-generation iPhone was launched, the iPhone 3G was released. These early smartphones let us see every little chip that was required to run a smartphone:

![iPhone 3G mainboard, with parts labelled](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_01.jpg)<br />
<small>iPhone 3G mainboard, with parts labelled<br />There are lots of small, auxiliary processors around the CPU.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+3G+Teardown/600)</small>

In spirit and form, the early smartphones were a lot like the early desktop mainboards ([Issue 132](https://buttondown.email/laymansguide/archive/lmg-s11-issue-132-the-at-form-factor-pre-1995/)): lots of chips performing highly specific functions.

After all, a smartphone has no need (or space) for a peripheral controller hub (PCH) ([Issue 134](https://buttondown.email/laymansguide/archive/lmg-s11-issue-134-part-1-the-intel-core-i-series/)) when it does not have add-on peripherals, and no need for a memory controller hub (MCH) when it can put the memory directly on the same chip as the CPU.

At this point, Apple was still using a CPU based on a design by ARM, and manufactured by Samsung. 2 years later, Apple had its own in-house processor: the Apple A4, their own design.

## What’s in a smartphone: 2010

This time, Apple had switched to an internal layout distinctly different from the iPhone 3G, and the basic layout (mainboard beside battery) would become a pattern for subsequent iPhone generations.

![iPhone 4 and iPhone 12](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_02.jpg)<br />
<small>iPhone 4 on the left, iPhone 12 on the right<br />The basic layout of the iPhone has been preserved over a decade.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+4+Teardown/3130) and [iFixit](https://www.ifixit.com/Teardown/iPhone+12+and+12+Pro+Teardown/137669)</small>

What’s the difference between this and the 3G? Let’s have a look at the iPhone 4’s mainboard:

![iPhone 4 mainboard](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue138/issue138_03.jpg)<br />
<small>iPhone 4 mainboard. I got lazy with the labelling because, well, there’s nothing to label!<br />The CPU is the huge chip labelled “A4”, and there’s memory and the 3G chip on the back.<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPhone+4+Teardown/3130)</small>

Similar to the transition from AT to ATX motherboards ([Issue 132](https://buttondown.email/laymansguide/archive/lmg-s11-issue-132-the-at-form-factor-pre-1995/) and [134](https://buttondown.email/laymansguide/archive/lmg-s11-issue-134-part-1-the-intel-core-i-series/)), the iPhone underwent a great miniaturisation—in a single generation!

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
- rendering graphics ([Issue 123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/))
- managing the flow of information between CPU, GPU, and memory (previously the job of the MCH)
- managing the flow of information between storage, network, and the MCH (previously the job of the PCH)

It is literally an entire system on a chip: a **system-on-chip** (SoC)!

More and more functionality would gradually be migrated into the SoC itself, with fewer auxiliary chips required: sensors, gyroscopes, image processors for the camera, etc. More educational perhaps would be to look at what’s *not* included in the SoC, particularly by the time we get to the the iPhone 12’s SoC, called the A14.

Not on the A14 SoC:

- solid state disk (only part of it is in the SoC)
- power management
- 4G & 5G
- audio

The above functionality is highly specialised, especially in modern[^2] smartphones. It manages the remaining parts of the phone: camera & mic/speakers, wifi & bluetooth, and telecommunications (4G/5G). Telecommunications in particular require a lot of power and would have contributed to unnecessary heating in the small CPU package.

[^2]: I know it’s strange to differentiate older vs newer smartphones when the technology is only 1.5 decades old. But the evolution of smartphone designs over the course has been significant enough that yes, I am going to make this distinction :)

And this is how we shrink a laptop mainboard even further.

**Issue summary:** A system-on-chip (SoC) combines the core functionality of a system—processing, graphics, memory, and control—into a single chip package.

## What I’ll be covering next

The M1’s design shares a lot more in common with the A14 on the iPhone and iPad than it does with the laptop CPUs that came before it. I want to go into a bit more detail about this in the next issue, so that it’s easier to see just how different it is from a typical laptop.

First question: what exactly does “unified memory” mean? Why is Apple making it such a big deal?

**Next issue:** [LMG S10] Issue 139: What’s before this line is mine, what’s after this line is yours

Next issue, we look at a trend that started being reported on in 2015: the high-performance computing industry realised that the CPU and GPU need to have much more integrated memory sharing.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
)?

![Chipset diagram of ATX systems for Intel Core (i-Series)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue134/issue134_02.gif)

Think about how information would flow here:

1. The CPU requests data from the hard disks, which get put *into system memory* (DDR; left-most side).
2. It carries out some pre-processing on that data to set up the task for the GPU, reading from memory, and storing the results back in memory.
3. The data is **copied** *from system memory* to the GPU, which stores that data *in GPU memory* (GDDR; right-most side).
4. The GPU carries out the task, storing the results *in GPU memory*.
5. The CPU requests the data from GPU memory, **copying** it back *into system memory*.

Are you seeing lots of wasted effort there? I bolded it in case you missed it. So much copying of information!

The high-performance computer industry quickly realised that it could be much more efficient if the CPU and GPU could *share the same memory*.

The information flow in this hypothetical memory-sharing system would be simplified to this:

1. The CPU requests data from the hard disks, which get put *into shared memory*.
2. The CPU pre-processes the data, storing it back into shared memory.
3. The CPU sends *the location* of the data to the GPU, which then reads *from shared memory* and carries out the task, storing the results back *into shared memory*
4. The CPU retrieves the results directly *from shared memory*.

We save time, bandwidth, and resources without having to copy data between CPU and GPU, twice! The only drawback is that with so many components (CPU, GPU, and others) accessing memory at the same time, you are going to need memory with really high bandwidth.

The industry gave this dream a name. They called it [heterogeneous system architecture (HSA)](https://en.wikipedia.org/wiki/Heterogeneous_System_Architecture), using a heterogeneous unified memory architecture (hUMA) i.e. shared memory.

![Unified memory diagram from Nvidia](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue139/issue139_01.jpg)<br />
<small>Nvidia’s heterogeneous unified memory architecture (HUMA) dream<br />Source: [WCCFtech](https://wccftech.com/intel-amd-nvidia-future-industry-hsa/2/)</small>

It turns out that this is a pretty difficult task—consider the amount of bandwidth needed to support CPU *and* GPU access. Today no product from any company (besides Apple) fully implements this in its SoCs ([Issue 138]()) yet.

**Issue summary:** Around 2015, the high-performance computer industry quickly realised that this would be much more efficient if the CPU and GPU could *share the same memory*.

I should stop here with this issue, and summarise the struggles of these companies in the next issue. They will make Apple’s success with the A14 & M1 a much more compelling read :)

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 140: The shared memory dream

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
