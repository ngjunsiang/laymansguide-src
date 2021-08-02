[**Previously:**](https://buttondown.email/laymansguide/archive/) Light takes 0.3 ns to travel 10 cm, approximately the distance by wire between the CPU and the MCH. This potentially causes operations between the CPU and MCH to slow down by one cycle, at frequencies above 3 GHz. One way the Intel Core i-series resolves this conundrum is to move the MCH *into* the CPU.

![Chipset diagram of ATX systems for Intel Core (i-Series)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue134/issue134_02.gif)<br />
<small>An Intel Core i-series ATX system chipset diagram.<br />The MCH is merged into the CPU, but still a discrete unit.<br />DDR refers to computer memory, while GDDR refers to graphics card memory ([Issue123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/))<br />Source: [Ars](https://arstechnica.com/gadgets/2009/09/intel-launches-all-new-pc-architecture-with-core-i5i7-cpus/)</small>

Time to close up some open plot points from last issue:

1. The number of pins on 1st-gen Core i7 is almost triple that of the Pentium 4; what are all those pins for?
2. The MCH has been moved into the CPU to improve latencies, but how is it possible to make it small enough to do that?
3. Are there any disadvantages?

I’ll answer the second question first. It’s quite simple really.

You see, for circuit components, size doesn’t always benefit performance. A large transistor does essentially the same thing as a smaller transistor. So making them smaller is advantageous really; you can fit more into a single chip!

## Making a modern CPU

Modern CPUs are manufactured through a process called **photolithography**—literally it means “etching with light” (Greek; _photo-_ “light” + _litho-_ “stone” + _-graphie_ “to draw”). By layering chemicals over the silicon base, putting a mask over them, and exposing them to light, a series of chemical reactions are induced to create the circuit pattern on the CPU.

Multiple CPUs are created on a single die this way, then individually cut and processed, in multiple steps spanning several months[^1]. The precision and fineness of the etching laser determine how small we can create components on this substrate. As the manufacturing process improves, semiconductor manufacturing companies are able to create CPUs that can cram more and more transistors into each square mm (or inch) of silicon die.

[^1]: See https://www.washingtonpost.com/technology/2021/07/07/making-semiconductors-is-hard/ for a more comprehensive description of the process

Besides being able to cram more transistors into the same space, it turns out that smaller components also use much less power! So we not only get performance gains, we get power efficiency gains as well—two birds with one stone.

![CPU diagram of the Intel Core i7 (1st-gen)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue135/issue135_01.jpg)<br />
<small>CPU diagram of the Intel Core i7 (1st-gen)<br />The memory controller, misc. IO, and QPI areas perform the role that the MCH used to take up<br />Source: [AnandTech](https://www.anandtech.com/print/2658/)</small>

## Moving in

Over multiple generations of process improvements, the MCH and the CPU could finally be made small enough that they could both reasonably fit into the same die. There are, of course, *implications*.

While the CPU and MCH no longer need to communicate with each other over wires, the CPU+MCH chip still needs wires to communicate with the computer memory, graphics processing unit (GPU), and PCH. Overall, it needs more pins than before.

So that answers the first question of what the pins are for.

## Working as one unit

Which leaves the third question: besides latency improvements, are there any other advantages?

Mainboard manufacturers save on the cost of the MCH chipset, [which works out to about $40](https://www.anandtech.com/show/2824). Pretty significant when a mid-range mainboard costs $80–$160.

With the MCH and its requisite wires gone, the mainboard can be shrunk further; motherboards gradually shrank from ATX and microATX form factor sizes, to smaller form factors, such as ITX and the current popular NUC form factors.

**Mainboard form factors**

- ATX: 30×24cm (12×9.6 in)
- microATX: 24×24cm (9.6×9.6 in)
- ITX: 17×17cm (7×7 in)
- NUC: 10×10cm (4×4 in)

And the disadvantages ... well, none on the consumer side actually. It seems to be positive all around!

Well actually, complexity rears its ugly head in power-saving features.

Previously, when the computer is in standby ([Issue 115](https://buttondown.email/laymansguide/archive/lmg-s9-issue-115-shutdown-standby/)), the CPU could be safely shut down (i.e. cut power to CPU), leaving only the MCH minimally powered so the computer memory retains its information.

With the MCH and the CPU now sharing the same chip, they have to be put in separate power zones so that the MCH portion remains powered while in standby, while the CPU can be shut down safely, making the chip more complicated than its predecessors.

But that is of little concern for us layfolks.

**Issue summary:** A modern CPU is manufactured through a process called photolithography, by which the CPU components are etched onto the silicon substrate by successive layers of chemicals, masking, and laser exposure. When the CPU components could be made small enough, the MCH and CPU were designed onto the same chip, and this is the design used by the Intel Core i7 (1st-gen).

This is where the story stops with Intel for this season; their current-gen Core series still uses much the same chipset diagram, and a similar basic architecture, so there’s little new info of relevance for me to add here.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 136: The mobile workstation – laptops

To continue the story towards the Apple M1, it’s time to switch our lens to the mobile world: tablets, smartphones, and things smaller than a laptop. How are these things designed? What are their CPUs like? We’ll examine the evolution of the iconic Macbook Air, from 2010 to 2020 (warning: image-heavy!)

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
