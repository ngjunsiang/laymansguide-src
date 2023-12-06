Title: Issue 155: Emulation performance
Date: 2022-01-15 08:00
Tags: 
Category: Season 12
Slug: lmg-s12-issue-155-emulation-performance
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Programs that were not compiled for the instruction set of the host OS have to go through an emulation layer program. This program translates the instructions of that program into compatible instructions that its own processor can execute.

> The Apple M1 is an ARM processor that executes 64-bit ARM instructions. MacOS programs that were compiled for Intel 64-bit x86-64 processors go through the Apple Rosetta 2 emulation layer to run on the M1.

Yes, that’s what I said last issue. But if that were all the Apple Rosetta 2 emulation layer did, The M1 Macbook would not have gotten its rave reviews.

## The act of translation

Think about it: the ARM and x86-64 instruction sets are very different! They have different lengths, different instruction names and bit values, different concepts of operation, … they’re *very* different. While the Intel Core and ARM processor architectures share *some* similarities, translating instructions from one set to another, though possible, is still no simple feat.

Keep in mind that in addition to translating the x86-64 instructions to ARM, the M1 also has to *execute them*—the program must go on. It should not be surprising at all that there is a performance hit compared with executing native ARM instructions.

If you were given a set of execution instructions in your native language, you would have little difficulty carrying out the required task. But if the execution instructions are now in alien language? Suppose you were given translation instructions, in your native language, for understanding the alien language. You would definitely be doing it slower than if the execution instructions were in your native language.

## Just-in-time translation

These days, our processors are fast enough that if they are not too bogged down, they can actually read in instructions slightly ahead of time, translate them, and store the translated instructions for a short period of time before they are executed. This way, the operating system remains ever so slightly ahead of the program being translated, in a way reminiscent of our currently strained global supply chain.

Naturally, it doesn’t make sense to keep doing translation work. As much as possible, we want to minimise it! But how?

**Issue summary:** Translating a set of instructions before executing it will always lead to a slowdown, although sometimes this may not be noticeable to users.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 156: Translation

In the last issue of season 12, we talk about why app installation or system updates can take so long.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
