[**Previously:**](https://buttondown.email/laymansguide/archive/) The ATX form factor also brought with it a new breed of computers with more specialised chipsets: the memory controller hub (MCH) and peripheral controller hub (PCH). The MCH specialises in high-throughput requirements, such as computer memory and graphics. The PCH specialises in lower-throughput needs.

Last issue, we looked at the ATX form factor by Intel, which replaced the AT form factor by IBM. While the AT could get by with a smattering of chips, which worked fine for mostly text-only computers, the ATX has much higher throughput requirements. To help the CPU focus on serving the user’s applications, two chipsets—the memory controller hub (MCH) and peripheral controller hub (PCH), take charge of managing the data throughput. The MCH manages data between CPU, computer memory, the graphics processor unit (GPU), and the PCH, while the PCH manages data between the peripherals (audio, storage, network, USB, ...) and the MCH.

![Chipset diagram of ATX systems, up to early Intel Core (i-Series)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue134/issue134_01.gif)<br />
<small>An Intel pre-Core i-series ATX system chipset diagram.<br />The MCH and PCH support the CPU in its data operations<br />DDR refers to computer memory, while GDDR refers to graphics card memory ([Issue123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/))<br />Source: [Ars](https://arstechnica.com/gadgets/2009/09/intel-launches-all-new-pc-architecture-with-core-i5i7-cpus/)</small>

There are terms for each of the connections between chips, which I won’t get into because it largely won’t concern us until we have to design performant systems.

## The evolution of Intel ATX

The technical geeks are probably fuming at this point because ATX is a motherboard standard, while I’m talking about the evolution of processors which have little to do with the motherboards, at least not directly ... but that’s of little importance at this point. Because we first need to talk about CPU pins.

From [Issue 131](), I gave a simple model of the limitations of data transfer:

> There is a max frequency they can operate at, and a limit to the number of wires they can be connected to (throughput = no. of wires × frequency)

The number of pins on processors have been steadily increasing up to this point, and so have the frequencies of processors. The Pentium 4 was succeeded by the Pentium D, then the Pentium Dual Core, then the Core 2. This Core processor preceded the Core i3/i5/i7 processors we know today; I’ll refer to this family of processors as the pre-i Core (rather than the more technical LGA775 series).

Pentium 4: 478 pins
Core, Core 2 (pre-i Core): 775 pins
Core (i7, first-gen): **1155 pins**

Yup, the number of pins have *almost tripled* since the Pentium 4! Remember that more pins does not make the CPU *itself* calculate faster, it just helps it to *transfer data* faster. What are all those pins for if there is the MCH to manage data flow?

Let’s talk about the limitations of the pre-i Core setup.

## Communication at a distance

Wait … don’t electrical signals travel at the speed of light? How would disappearing the MCH improve latency?

Consider some numbers:

The typical distance between the CPU and the MCH is about 5 cm (2 in). Since the wires between them are not straight, let’s approximately double that to 10 cm (4 in). Light would take 0.3 ns to travel that distance. Which is roughly one clock cycle on a 3 GHz processor—at 3 billion cycles per second, each cycle takes a third of a billionth of a second![^1]

[^1]: I want to just make a note here that while I believe my choice of analogy is justified, the numbers are wildly off: [RealWorldTech here puts the 1st-gen Core at approx 30 ns](https://www.realworldtech.com/nehalem/3/), for technical reasons that will take at least half a season to unpack (definitely not layman content!). But he also notes that latency for remote memory (i.e. memory not on the CPU, but on the motherboard) is “roughly 30 ns slower than local [memory]” (i.e. memory residing directly on the CPU). So the remote-vs-local latency gap is real and significant!

Remember that everything in a computer needs to happen like clockwork: for data to sync up, when the CPU sets a bit to one, the other party has to detect the bit signal before the clock cycle is up. If not, it will have to wait for the next clock cycle, causing the operation to slow down and take two clock cycles instead of one. It’s like when you don’t manage to post the mail by 5pm, the postman has emptied the mailbox, and now you have to wait for 5pm the next day to post mail instead.

## It’s all about throughput ... but also latency

If light is taking one clock cycle to get out of the CPU, you have a problem. Raise the frequency higher than 3GHz, and you can cause a one-cycle lag just waiting for data to come in from the MCH, and to go out again to the MCH.

Solution: move the MCH into the CPU!

![Chipset diagram of ATX systems for Intel Core (i-Series)](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season11/issue134/issue134_02.gif)<br />
<small>An Intel Core i-series ATX system chipset diagram.<br />The MCH is merged into the CPU, but still a discrete unit.<br />DDR refers to computer memory, while GDDR refers to graphics card memory ([Issue123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/))<br />Source: [Ars](https://arstechnica.com/gadgets/2009/09/intel-launches-all-new-pc-architecture-with-core-i5i7-cpus/)</small>

## Squeezing more tenants into the building

Wait ... you can just do that?

I will need many more issues to lay out the mechanics of this, so I won’t—I think it’s way beyond the scope of a layman’s guide at that point!—but let’s see what I can come up with in the next issue.

**Issue summary:** Light takes 0.3 ns to travel 10 cm, approximately the distance by wire between the CPU and the MCH. This potentially causes operations between the CPU and MCH to slow down by one cycle, at frequencies above 3 GHz. One way the Intel Core i-series resolves this conundrum is to move the memory controller *into* the CPU.

This is what I spent years reading and thinking about to explain, and I finally get to lay it out in text. Incredibly excited to get to the next few issues!

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 135: Part 2 – Unifying the CPU and MCH (post-2008)

Next issue: how the ATX form factor evolved to eliminate the MCH. Sorry to end on a cliffhanger!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
