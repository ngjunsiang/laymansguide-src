Title: Issue 154: Emulation
Date: 2022-01-08 08:00
Tags: 
Category: Season 12
Slug: lmg-s12-issue-154-emulation
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) The cloud offers standard digital business services, accessible through a web interface and API, which any developer (with a credit card) can use. Developers don’t have to reinvent the wheel, so long as they know how to use web APIs.

Virtualisation, particularly system virtualization, is a real game-changer for those of us who like to have our apps all running in the same operating system, instead of switching operating systems all the time through dual-booting (or Apple Parallels).

But what is stopping us from allowing them to run near-natively in the desktop, their windows directly showing up in the taskbar, without the distracting abstraction of the virtual machine?

## Introduction to Emulation

What you are seeking is a feature known as **emulation**, in which your operating system (OS), which we shall again call the **host**, *emulates* the instruction set ([Issue 53]({filename}/season5/issue053/issue053.md))) that the application is compiled for. In other words, the host OS:

1. presents itself as the “correct” machine type to the application (“hello program, I listen to x86 instructions and respond to x86 instructions, so please treat me like an x86 processor”),
2. transparently interprets its machine code into its instruction set’s machine code (through a program called an **emulation layer**),
3. executes the interpreted version, producing its intended effects, and returning any intended output back to the application.

Depending on how different the two instruction sets are, the complexity of this task differs greatly. Not much point going into detail here in a layman’s newsletter, so instead I’ll briefly illustrate some instances of emulation in the wild.

The three main instruction sets discussed here are x86 (32-bit), x86-64 (64-bit), and ARM[^1] ([Issue 53]({filename}/season5/issue053/issue053.md))).

[^1]: ARM actually has a 32-bit instruction set—AArch32 and a 64-bit instruction set—AArch64, which are incompatible. But since Apple switched to AArch64 starting from the iPhone 5S (2013), other mobile device manufacturers have followed suit, and AArch64 is now the main instruction set used on mobile. In this issue, I use ARM to refer to AArch64.

## Windows-to-Windows emulation (WOW64)

Do you remember the great 32-to-64-bit schism of the late 2000s ([Issue 55]({filename}/season5/issue055/issue055.md)))? There was a period of time when people got confused whether a Windows program they had could run on a 32-bit x86 processor or a 64-bit x86-64 processor: programs compiled for the latter could not run on the former, but programs compiled for the former could run on the latter.

![screenshot of download options for WinRAR, showing 32-bit and 64-bit options]({attach}/season12/issue154/issue154_01.png)  
<small>Some download sites still ask you to make this choice between downloading the 32-bit or 64-bit version, usually for users who for whatever reason have opted not to upgrade to 64-bit processors.</small>

That was a lie. Programs compiled for Windows on x86 cannot run *natively* on x86-64, and vice-versa. x86 and x86-64, while looking similar, are different instruction sets. x86 instructions have to be translated into x86-64 instructions to run on a 64-bit processor.

What happened was Microsoft developed the WOW64 subsystem, an emulation layer that translated 32-bit x86 instructions into 64-bit x86-64 instructions. When users tried to run a 32-bit application, Windows plugged the instruction stream into WOW64, executing the interpreted instructions and allowing it to run near-natively[^2].

[^2]: You can still see this happening with some old programs; this is usually indicated in the title bar as compatibility mode.

And so the 32-to-64-bit transition took place more smoothly than it would otherwise have.

## Windows ARM emulation for x86

In 2019, Microsoft released the Surface Pro X, its second[^3] ARM-powered laptop. That’s right, it’s Windows not running on an Intel chip. Microsoft does actually have a version of Windows, called Windows ARM, which runs on ARM chips. But what about all the programs you know and love?

[^3]: Their first was the ill-fated [Surface RT](https://www.techradar.com/reviews/pc-mac/tablets/microsoft-surface-rt-1085839/review), which these days is only whispered about.

WOW64 to the rescue again! This emulation layer *also* translates 64-bit x86-64 instructions to 64-bit ARM instructions, allowing them to run on Windows ARM (with a performance penalty due to the translation required).

## Game console emulation

If you find any “reborn” retro gaming products floating around, these are guaranteed to be emulators in disguise: the original hardware that the consoles used are no longer in production. (If you don’t find any, you can also just google “console emulation” to find a whole collection of them.)

These emulators are usually hobby projects by skilled amateurs, who attempt to reverse-engineer the workings of the original hardware. They then write programs to *emulate* these processors on modern hardware, allowing you to “boot” a digital copy of the games that worked on those platforms.

## Apple Rosetta

The Apple M1 is an ARM processor that executes 64-bit ARM instructions. MacOS programs compiled for Intel 64-bit x86-64 processors must go through the Apple Rosetta 2 emulation layer to run on the M1. This works like WOW64 but in the reverse direction: it takes in an x86-64 instruction stream, and produces interpreted instructions for Apple ARM processors.

**Issue summary:** Programs that were not compiled for the instruction set of the host OS have to go through an emulation layer program. This program translates the instructions of that program into compatible instructions that its own processor can execute.

Simple to describe, much more difficult to execute … 😩

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 155: Emulation performance

Is this how emulation actually works? I wish! Don’t want to go too deep, but I think it is instructive to briefly discuss performance issues, and why it leads to some things you might have observed.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
