Title: Issue 54: Compiling programming code into CPU instructions
Date: 2020-01-04 08:00
Tags: 
Category: Season 5
Slug: issue054
Author: J S Ng
Summary: 
Modified: 2020-01-04 08:00

**Previously:** CPUs are unconscious slaves that simply execute instruction after instruction, at a very fast rate.

Last issue, I introduced the idea of the CPU has an unconscious instruction-executing machine. It cannot process programming code directly; that code must first be compiled into CPU instructions.

## The compiler converts programming code to CPU instructions

Last issue, I showed you a short snippet of CPU instructions:

```
1 LOAD 1   R1
2 ADD  2   R1, R2
3 MOV  R2, MEM1011
```

But that’s not the kind of code we usually see in movies, on the screens of geeks, and in stock images. What gives?

Most code we see looks something like (example from Python):

```
num1 = 1
num2 = 2
sum = num1 + num2
print(f'The sum of {num1} and {num2} is {sum}')
```

How does that get turned into CPU instructions? That job is performed by a piece of software known as the **compiler**.[^1] The compiler compiles programming code into an **executable file** (sometimes shortened to executable), which contains the actual instructions executed by the CPU. This is why, in Windows, some files have a `.exe` file extension — those are **exe**cutable files!

[1]: Purists will argue with me that Python technically runs through an interpreter, not a compiler. At this point, the distinction between the two terms for layfolks is not critical, and I choose clarity over accuracy at this point until I can delve into more detail in a future issue.

The compiler itself is also a piece of software that reads in programming code (a process known as **parsing**), and follows its own instructions to break it down into CPU instructions.[^2]

[2]: If you find yourself wondering “how was the first compiler written? Which came first: the compiler code, or the compiler executable? How would a compiler compile its own code into its executable?”, you might be a prime candidate for a Computer Science degree programme :)

Okay, I think I am done talking about CPU instructions for now. On to the next piece of the puzzle: memory.

## Computer memory: addressable bytes

In the CPU instruction snippet above, there was a line that involved storing data into memory:

```
3 MOV  R2, MEM1011
```

This line means “store the value in slot R2 into the memory location 1011”. Next issue, I will delve into what these memory locations are, and build out our mental model of how a CPU works.

**Issue summary:** To get useful output from a CPU, we must translate the operations we want it to perform into CPU instructions, in a process known as **compiling**. Most compilers convert programming code into CPU instructions.

A very short issue, just as I like it :) There’s something philosophical about the process of a CPU beginning with no knowledge of what to do, and slowly bootstrapping a library of code-to-instruction conversions through a compiler. These and other puzzles about information manipulation are what computer scientists love studying! And this is one good reason to differentiate Computer Science from general Computing: if you take up a degree in Computer Science and expect to learn more about general Computing, you might end up being disappointed.

## What I’ll be covering next

**Next issue:** Addressing memory

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- ~~compiling code into an application [Issue 26]?~~
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
