[**Previously:**](https://buttondown.email/laymansguide/archive/) A system-on-chip (SoC) combines the core functionality of a system—processing, graphics, memory, and control—into a single chip package.

I am eager to get dig into the meat of the A14 and M1! But first I must set up a story.

## The hUMA race

Circa 2015 9actually even a couple of years before that), the industry suddenly seemed to wake up and realise that graphics cards could do a lot more than just play video games. The nature of how they work ([Issue 121]() & [122]) makes them very amenable to solving problems in scientific computing, particularly in simulations, where they use up computational resources by the petaflop, and energy by the megawatt.

In a nutshell, the problem the industry now faces is this:

1. The GPU is massively powerful ... at doing a small subset of things. You can’t run a computer with only a GPU.
2. The CPU is nimble, and much more suited for everyday tasks, like starting up a computer and connecting to multiple peripherals, and basically creating a useable digital environment for humans.
3. It thus makes the best sense to use the CPU to set up the heavy-lifting for the GPU, and have the GPU return the results after computation.

Remember this diagram from [Issue 134]()?

![Chipset diagram of ATX systems for Intel Core (i-Series)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue134/issue134_02.gif)

Think about how information would flow here:

1. The CPU requests data from the hard disks, which get put *into system memory* (DDR; left-most side).
2. It carries out some pre-processing on that data to set up the task for the GPU, reading from memory, and storing the results back in memory.
3. The data is **copied** *from system memory* to the GPU, which stores that data *in GPU memory* (GDDR; right-most side).
4. The GPU carries out the task, storing the results *in GPU memory*.
5. The CPU requests the data from GPU memory, **copying** it back *into system memory*.

Are you seeing lots of wasted effort there? I bolded it in case you missed it. The high-performance computer industry quickly realised that this would be much more efficient if the CPU and GPU could *share the same memory*. This idea was labelled heterogeneous systems architecture (HSA).

The information flow would be simplified to this:

1. The CPU requests data from the hard disks, which get put *into shared memory*.
2. The CPU pre-processes the data, storing it back into shared memory.
3. The CPU sends *the location* of the data to the GPU, which then reads *from shared memory* and carries out the task, storing the results back *into shared memory*
4. The CPU retrieves the results directly *from shared memory*.

We save lots of time, bandwidth, and resources without having to copy data between CPU and GPU, twice!

The industry gave this dream a name. They called it heterogeneous system architecture (HSA), using a heterogeneous unified memory architecture (hUMA) i.e. shared memory.

![Unified memory diagram from Nvidia](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue139/issue139_01.jpg)<br />
<small>Nvidia’s heterogeneous unified memory architecture (HUMA) dream<br />Source: [WCCFtech](https://wccftech.com/intel-amd-nvidia-future-industry-hsa/2/)</small>

It turns out that this is a pretty difficult task, and today no product from any company (besides Apple) implements this in its SoCs yet.

**Issue summary:** Around 2015, the high-performance computer industry quickly realised that this would be much more efficient if the CPU and GPU could *share the same memory*.

I should stop here with this issue, and summarise the struggles of these companies in the next issue. They will make Apple’s success with the A14 & M1 a much more compelling read :)

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 140: The shared memory dream

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
