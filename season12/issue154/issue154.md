[**Previously:**](https://buttondown.email/laymansguide/archive/) The cloud offers standard digital business services, accessible through a web interface and API, which any developer (with a credit card) can use. Developers don’t have to reinvent the wheel, so long as they know how to use web APIs.

Virtualisation, particularly system virtualization, is a real game-changer for those of us who like to have our apps all running in the same operating system, instead of switching operating systems all the time through dual-booting (or Apple Parallels).

But what is stopping us from allowing them to run near-natively in the desktop, without the distracting abstraction of the virtual machine?

## Introduction to Emulation

What you are seeking is a feature known as **emulation**, in which your operating system (OS), which we shall again call the **host**, *emulates* the instruction set ([Issue 53](https://buttondown.email/laymansguide/archive/lmg-s5-issue-53-the-cpu-is-an-instruction-obeying/)) that the application is compiled for. In other words, the host OS:

1. presents itself as the “correct” machine type to the application,
2. transparently interprets its machine code into its instruction set’s machine code (through a program called an **emulation layer**),
3. executes the interpreted version, producing its intended effects, and returning any intended output back to the application.

Depending on how different the two instruction sets are, the complexity of this task differs greatly. Not much point going into detail here, so instead I’ll briefly illustrate some instances of emulation in the wild.

## Windows-to-Windows emulation (WOW64)

Do you remember the great 32-to-64-bit schism of the late 2000s? There was a period of time when people got confused whether a Windows program they had could run on a 32-bit x86 processor or a 64-bit x86-64 processor: programs compiled for the latter could not run on the former, but programs compiled for the former could run on the latter.

That was a lie. Programs compiled for Windows on x86 cannot run on x86-64, and vice-versa.

What happened was Microsoft developed the WOW64 subsystem, an emulation layer that translated 32-bit x86 instructions into 64-bit x86-64 instructions. When users tried to run a 32-bit application, Windows plugged it in to WOW64, allowing it to run near-natively (this is usually indicated in the title bar as compatibility mode).

And so the 32-to-64-bit transition took place more smoothly than it would otherwise have.

## Windows ARM emulation for x86

In 2019, Microsoft released the Surface Pro X, its second(?) ARM-powered laptop. That’s right, it’s Windows not running on an Intel chip. Microsoft does actually have a version of Windows, called Windows ARM, which runs on ARM chips. But what about all the programs you know and love?

WOW64 to the rescue again! This emulation layer *also* translates 32-bit x86 instructions to 64-bit ARM instructions, allowing them to run on Windows ARM. 64-bit ARM instructions are still a work in progress.

## Game console emulation

If you find any “reborn” retro gaming products floating around, these are guaranteed to be emulators in disguise, given that the original hardware that the consoles used are no longer in production. (If you don’t, you can also just google “console emulation” to find a whole collection of them.)

These emulators are usually hobby projects by skilled amateurs, who attempt to reverse-engineer the workings of the original hardware. They then write programs to *emulate* these processors on modern hardware, allowing you to “boot” a digital copy of the games that worked on those platforms.

## Apple Rosetta

The Apple M1 is an ARM processor that executes 64-bit ARM instructions. MacOS programs that were compiled for Intel 64-bit x86-64 processors go through the Apple Rosetta 2 emulation layer to run on the M1.

**Issue summary:** Programs that were not compiled for the instruction set of the host OS have to go through an emulation layer program. This program translates the instructions of that program into compatible instructions that its own processor can execute.

Simple to describe, much more difficult to execute … 😩

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 155: Emulation performance

Is this how emulation actually works? I wish! Don’t want to go too deep, but I think it is instructive to briefly discuss performance issues, and why it leads to some things you might have observed.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
