[**Previously:**](https://buttondown.email/laymansguide/archive/) Using the same hardware for both smartphones and laptops would make it much easier to write apps for both platforms. The closer they are in features, hardware, and software support, the easier things will be for developers.

So, let’s get some Likely-Asked-Questions (LAQs) out of the way in this last issue.

## If developing for a single chip makes things much easier for developers, can we just decide to develop everything for the M1 chip and somehow force Apple to share the chip design?

You know as well as I do that the answer is no. Besides, Apple doesn’t care about the hardware needs of devices other than its own. You want other features they don’t care about? Too bad.

## So only Apple users get to enjoy unified memory?

Yes, for now. We’ll need to wait a few years for other chipmakers to figure out their own hardware implementations.

## Who’s likely to achieve it first?

This’ll have to be a company that designs its own CPUs and GPUs.

The incentives don’t align for Intel. Their main business has never relied on capable graphics, and they are much more concerned with saving the server market from ARM’s and AMD’s encroachment.

What about AMD? After all, they were one of the earliest companies to push for a similar idea: Heterogeneous System Architecture. And they achieved it to a lesser extent, with their Accelerated Processing Units (see [Issue 142](); a fancy term for CPU+GPU).

AMD has made this possible in software; that means as a programmer, you can command the CPU to store data at a memory address, pass that address to the GPU, and then get the GPU to retrieve data from that address. But in practice, benchmarks show that passing data this way falls short of the actual throughput that would be expected; possibly the hardware support is just not there yet, and not easy enough to use.

But the incentives line up quite well for AMD. If they achieve it, the performance of their APUs, their mid-range product, will see a significant boost. But they will need significant influence with developers to develop software development kits (SDKs) that developers can use to take advantage of unified memory, and that’s a big investment of resources.

Nvidia is putting a lot of effort into catching up on the CPU side of things, and they have been pushing lots of ARM chip designs to complement their strength in graphics cards. They have also recently bought ARM, so they also seem like a strong contender to implement unified memory. My gut sense is that it is not high on their priority list, as their primary business is still parallel compute and related applications, such as machine learning and scientific computing.

The work for this will have to be ongoing, of course, and likely started since 2015 or so; starting in 2021 is way too late!

## What does this mean for Apple?

They are now almost fully in control of their own hardware and software now. The main limitations where their control does not reach is their cloud computing (where iCloud happens), and the manufacturing (likely still TSMC in the near future). Their concerns now will be much more international than before.

## Should we expect to see unified memory on non-Apple chips?

Yes, definitely, it’s something the industry has been working towards, just way too slowly ... and hopefully the M1’s existence will put some pressure on those development timelines.

I suspect the main cause of inertia is all the legacy software that still has to be supported. Because Intel and AMD have a lot of business riding on keeping compatibility with past hardware, they can't make sweeping changes across their entire range of products, unlike Apple. Every change that is made to an existing line of chips has to still keep it working when customers run their existing software.

## How does this affect consumers?

Probably not much effect, beyond the gradual speed gains from generation to generation that we are already seeing.

The more significant effect is, I think, the miniaturisation of mobile systems. Already the mainboard for a laptop like the Macbook has shrunk to a narrow rectangle; most of the space for devices is now taken up by energy storage (i.e. batteries). The limiting factor now seems to be energy density: how many grams of batteries we will need per hour of laptop use. I suspect this is going to keep laptops more or less at the same size; the laptop is a mature form factor at this point and will gradually age.

What’s more exciting is when unified memory architectures can be miniaturised sufficiently for wearables. We are going to need that if we want augmented-reality (AR) systems, e.g. graphics projected directly on a lens in front of our eyes, in a compact form factor. Many virtual reality (VR) and AR systems currently come in bulky designs that sit heavily on the body; there is much room for improvement here.

## Wrapping up

This somehow ended up as a crash course in CPUs and GPUs, all in one season. I didn’t mean to carry out an industry analysis here, and this is definitely not a forecast to be relied on! It’s just a very interesting story to follow and I can’t help but think about what’s happening on multiple levels.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 144: Programs-in-a-vat

How does a program on the computer know if it is in a simulation?

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
