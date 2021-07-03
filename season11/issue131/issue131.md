[**Previously:**](https://buttondown.email/laymansguide/archive/) AC power from the wall uses electric current that alternates directions, while DC power from batteries uses electric current that flows in one direction only. All electronics are DC-only, and require an AC-DC adapter to be powered from the wall. The AC-DC conversion produces a significant amount of heat; AC-DC adapters are usually external unless the device has sufficient space or cooling capacity for it.

This season, let’s open up that computer case and see what’s inside. Where does everything fit, and how does all that information get around? More importantly, how are computers able to cover such a large range of sizes, from towering desktops to tiny smartphones?

## What a computer wants, what a computer needs

The common model of a computer is that it … computes. It calculates. It takes in numbers, and spits out more numbers.

That’s not quite right.

While a computer does carry out compute operations, these are far outnumbered by load/store operations ([Issue 58](https://buttondown.email/laymansguide/archive/lmg-s5-issue-58-cpu-optimisation-part-1-out-of/)). Why so much loading and storing of data?

## Moving data

The CPU itself has precious little storage (<20 MB of cache storage); it is only a wee little chip! Most of the data in a computer is stored in a hard drive or solid state drive; let’s just call them storage drives for now.

So CPUs have to read data from a storage drive. This is a slow operation, because storage drives are slow; writing to storage drives is even slower than reading from them.

In the meantime, the CPU needs a place to dump working data; this is computer memory (2–32GB). Memory is slower than the CPU’s cache, but much faster than a storage drive.

That’s 3 places to stash data so far: storage drives, CPU cache, and computer memory. You with me so far?

## Pipelines

The next place that often requires lots of data is the graphics card ([Issue 123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/)). For you to play a video game, the computer has to:

1. Load game data from the storage disk,
2. Store most of it in memory while it’s doing some number crunching in its cache,
3. Get the crunched numbers to the graphics card for rendering graphics ([Issue 122](https://buttondown.email/laymansguide/archive/lmg-s10-issue-122-the-great-flattening/)),
4. Load more data from memory while crunching more numbers, and passing them to the graphics card.

This involves far more loading and storing than computation. And there are limitations to how quickly data can be transferred.

## Throughput

How does data get transferred? Through very fine wires usually. One side (e.g. the CPU) applies a voltage to the wire, the other side (e.g. memory) checks the voltage on the wire. No applied voltage = a 0, applied voltage = a 1.

How does the CPU know when to apply the voltage, and the memory know when to check it? These operations are synchronised through cycles, like a highly coordinated factory. A CPU operates on a frequency of up to billions of cycles per second, each cycle potentially transferring one bit of data ([Issue 40](https://buttondown.email/laymansguide/archive/lmg-s4-issue-40-bits-and-bytes/)) if there are no delays.

Typically, the transfer rate is somewhat slower; how do we transfer more data per second? By adding more wires! With two wires, we can transfer two bits per cycle; four wires = four bits per second, eight wires = 8 bits per second … at some point, we run into a different problem. The CPU is a small chip, and there is only so much surface area for us to connect wires to.

![An Intel Skylake CPU, showing the pins underneath](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue131/issue131_01.jpg)<br />
<small>An Intel Skylake desktop CPU.<br />Each gold contact on the under-surface connects to a pin on the motherboard when the CPU is seated properly in its socket<br />Source: [Wikipedia](https://en.wikipedia.org/wiki/Skylake_(microarchitecture))</small>

Well, that just sucks.

## The limits of one chip

Come to think of it, humans are much the same; we only have two hands and two legs, there are limits to how fast we can do things, and limits to how long we can stay awake working. We mostly get around these limitations by learning to delegate.

In the same way, computer designs evolved to delegate more work to secondary chips, leaving the CPU to focus on computation. We’ll explore the gradual evolution of these architectures, so you can better appreciate the elegance of the Apple M1’s design ;)

**Issue summary:** CPUs have limited throughput, since there is a max frequency they can operate at, and a limit to the number of wires they can be connected to (throughput = no. of wires × frequency). Later designs of early computers increased the capability of computers by delegating more work to secondary chips.

The more I learned about computer architecture, the more I see parallels to startups and organisational culture in general. I was really looking at ways of organising information flows, and observing how the computational limitations of different parts influence the design of the whole chip! This is a constant work in progress, which is why we keep seeing new CPU designs emerge each year.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 132: the AT form factor (pre-1995)

Let’s start from—nah, I wont go all the way back to the beginning, just to the point where computer architecture was already recognisable in its early modern form. Next issue, a big welcome for the AT form factor!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
