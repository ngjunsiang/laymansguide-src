[**Previously:**](https://buttondown.email/laymansguide/archive/) Computers are general-purpose machines that usually process integer calculations. The graphics pipeline requires more specialised hardware that can process decimal number calculations. This is why high-performance graphics usually requires a graphics card.

So why are gamers so agog over **graphics cards** (also known as video cards)? That’s because they do one thing really well! Unlike CPUs which often have to process an unpredictable workload, the graphics pipeline involves performing the same categories of calculations over and over again.

## Graphics compute units

These calculations, which I gave an overview of in [Issue 122](), take in tables of numbers, crunch them mathematically, and spit out another table of numbers. Since the calculations are predictable, we don't need very complicated hardware that enables switching instructions based on the input. We can used specialised cores—clusters of transistors that are custom-fit for the purpose, cram lots of them into a circuit board, and end up with much better performance for the graphics pipeline compared to the CPU.

These cores are organised into groups known as **compute units**, and graphics card companies often differentiate the lower-end and higher-end cards by the number of compute units they have, which indicate the computation rate (measured in **flops**, which stand for **fl**oating-point[^1] **o**perations **p**er **s**econd). Better graphics require more computation, so more flops correlate with better graphics.

[^1]: “Floating-point” is a fancy term for decimal, so-called because the way they are represented allows the decimal point to be placed differently, unlike with integers.

## Graphics memory

Graphics cards often come with their own memory chips, based on a different technology (**GDDR**, standing for “graphics double data rate”, vs **DDR** for CPUs). Graphics memory chips (GDDR) are optimised for higher bandwidth (more gigabytes transferred per second), while CPU memory chips (DDR) are optimised for lower latency (lower time to response). These are soldered directly onto the graphics card to keep memory readily accessible by the compute units.

## Power and heat

Unlike CPUs, which (for desktops) seldom draw more than 100W by themselves, graphics cards (for desktops) can draw up to 300W. Correspondingly, more of the space on graphics cards are taken up by components that try to keep this immense power under control. Regular modules help to adjust input voltages to what the compute units and memory requires.

![Graphics card without its shroud and cooler](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue123/issue123_01.jpg)<br />
<small>A graphics card, here exposed without its shroud and cooler.<br />The graphics chip is in the middle, surrounded by graphics memory chips (smaller, black squares) close to the edges of the board. The larger protruding gray rectangles are voltage regulation modules.<br />Image from [Gamersnexus](https://www.gamersnexus.net/guides/2826-differences-between-ddr4-and-gddr5)</small>

## Other uses

The graphics card excels at carrying out predictable decimal calculations in a pipeline. Besides graphics, what else can it be used for?

In research, they have been purposed to perform calculations for simulations, which often involve processing the same calculation in bulk.

For consumer purposes, they have also been used for video decoding (decompressing videos for playback), and lately even video encoding (compressing videos to a smaller size). These also involve performing the same types of calculations in a predictable pipeline.

Most recently, they are being used for machine learning (also known as “artificial intelligence”) models, again because those involve predictable pipelines (Do you are see a pattern here?)

## Integrated graphics

Not all computers need a full-size GPU to render graphics on screen. Intel processors, and some of the newer AMD ones, contain what is known as **integrated graphics**. That means that these CPUs have a graphics processor unit (GPU) integrated into the same chip. This integrated GPU provides basic capabilities which allow typical users to use a computer, and even run low-end graphics programs, without needing to buy a higher-end graphics card.

Integrated GPUs do not have their own memory. They share computer memory with the CPU. That means that they reserve a (configurable) amount of computer memory for graphics use (typically up to 128 MB), and video card drivers ([Issue 120](https://buttondown.email/laymansguide/archive/lmg-s10-issue-120-drivers-the-glue-between/)) enable the GPU to use more system memory ([up to 50% for Intel integrated graphics](https://www.intel.sg/content/www/xa/en/support/articles/000020962/graphics.html)). This means that integrated graphics use slower memory compared to dedicated graphics cards that have their own memory.

**Issue summary:** Graphics cards contain lots of tiny cores that are much better at performing the same calculation for lots of decimal numbers. These cores are organised into compute units; a graphics card with more compute units can perform more calculations every second. Graphics cards have their own onboard memory, separate from the CPU. GPU memory is different from computer memory; it is configured for much higher data throughput. Integrated graphics are GPUs that are integrated into a CPU chip; these do not have their own onboard memory, and share memory with the CPU.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 124: Video formats

I haven’t talked about the last part, because this issue is long enough already, and because the next part can fill a whole issue by itself. Next up, the last stage: actually displaying pixels on a screen.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- ~~a video card? [Issue 113]~~
