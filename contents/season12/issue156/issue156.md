[**Previously:**](https://buttondown.email/laymansguide/archive/) Translating a set of instructions before executing it will always lead to a slowdown, although sometimes this may not be noticeable to users.

So, just-in-time (JIT) compilation is really cool and mostly works. Feed in enough instructions to fill a buffer, and execute them. Keep your fingers crossed and hope the buffer doesn’t empty. That’s kind of how our global supply chain works too.

But sometimes it doesn’t go smoothly. The program hits a code branch, new instructions have to be unpredictably injected. The emulation layer halts temporarily. The program stutters.

We can’t really avoid that, not without rewriting the program anyway. But we can at least decide *when* to carry out the translation.

## Ahead-of-time translation

What if we translated whatever we could ahead of time, and stored the *native* instructions? Then, whenever we need that chunk, instead of translating the original program chunk, we just load the already-translated instructions?

This is called ahead-of-time (AOT) translation, and is what Apple Rosetta 2 does with MacOS programs compiled for Intel x86-64. While installing those applications, it also carries out translation into native ARM instructions that the M1 later uses for execution.

## Android AOT translation

The Java virtual machine (VM), also called the Java Runtime ([Issue 151](https://buttondown.email/laymansguide/archive/lmg-s12-issue-151-the-java-vm/)), is the interpreter that carries out the Java bytecode that a Java program comprises.

Android apps, though themselves Java programs, are run not by the Java Runtime, but by the Android Runtime[^1].

[^1]: Recall from [Issue 151](https://buttondown.email/laymansguide/archive/lmg-s12-issue-151-the-java-vm/) that one needs a distribution license to distribute the Java runtime environment (JRE); Google would have to pay hefty licensing fees to Oracle to bundle the JRE with each copy of Android. Instead, they decided to write their own compatible runtime: the Android Runtime. Is this legal? They already fought that battle in court ([Google LLC v. Oracle America, Inc](https://en.wikipedia.org/wiki/Google_LLC_v._Oracle_America,_Inc.)), and it seems the answer is “yes” (with a heap of caveats).

Whenever your Android phone finishes installing an Android update, there is always a significant block of time that it takes up “optimising” your apps. What it is doing is actually AOT translation, of the app’s Java bytecode into ARM instructions.

## Compilers vs interpreters

Back in [Issue 54](https://buttondown.email/laymansguide/archive/lmg-s5-issue-54-compiling-programming-code-into/), I mentioned in a footnote that

> Purists will argue with me that Python technically runs through an interpreter, not a compiler. At this point, the distinction between the two terms for layfolks is not critical, and I choose clarity over accuracy at this point until I can delve into more detail in a future issue.

Here is where I can draw the distinction more clearly.

A **compiler** *compiles* a programming language into another language; usually this means translating a programming language into machine instructions, or virtual machine (VM) bytecode ([Issue 150](https://buttondown.email/laymansguide/archive/lmg-s12-issue-150-system-vms-vs-process-vms/)). But it is also not unheard of for compilers to translate one programming language into another, e.g. translating to Javascript for use in a webpage.

An **interpreter** *interprets* a programming language, and executes it to bring about the intended effect (creating/changing/deleting a file, producing a sound, displaying an image, …).

It may be helpful to think of a compiler as carrying out AOT translation, and an interpreter as carrying out JIT translation. But many systems will use a mix of both. The Python interpreter, for instance, actually translates Python code into intermediate Python bytecode, and then executes the bytecode. When you run the same Python script, it executes the bytecode if the Python code has not changed. If it has changed, the interpreter will recompile the bytecode first, then execute it.

**Issue summary:** To speed up execution and avoid translation overhead, some systems employ ahead-of-time translation, storing the translated instructions to be executed in future. But many systems employ a mix of just-in-time (JIT) and ahead-of-time (AOT) techniques.

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 157: NTP and time-syncing

In the season finale, I’ll wrap up with a mishmash of things that are *not* the Internet per-se, but very much a part of the Internet and our lives. First up: how do our phones always know the *actual* time?

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
