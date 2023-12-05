[**Previously:**](https://buttondown.email/laymansguide/archive/) In 1999, VMware launched VMware Workstation, which allowed multiple operating systems to run off a single machine.

In Season 5 ([Issue 53]({filename}/season5/issue054/issue054.md

But the program does not handle everything on its own. In fact, it does not usually have direct access to hardware (unless requested from and provided by the operating system (OS)). All such access is abstracted and mediated through the operating system. The program requests and receives memory space, reads and writes files, and processes keyboard/mouse input—through the operating system.

How does the program know it is not living in a simulation? If the environment it operates in responds to its requests, the program continues running without a care. A keypress event is a keypress event, and the program can respond to it, whether it really came from a keyboard or not. A file that has data to read can be treated like a file, whether it is really stored on the hard disk or actually streamed from cloud storage.

## Computing interfaces

This paradigm is really powerful, because it enables us to pipe data from place to place. It enables us to build **interfaces**: instead of writing a program that has to grapple with the gnarly details of files in binary format, I can write a program that deals with a *file interface* instead. The interface lets me read and write data, while the gnarly details are handled one layer down, by the filesystem.

And this is how we can open documents from a flash drive without even realising that the flash drive uses a different filesystem from our system disk.

The OS is just another special set of programs that mediate access to the hardware. Yet, it is easy to forget that even the OS’s many programs do not actually deal with the gnarly details of hardware, but with an *interface* to the hardware. This interface are the drivers ([Issue 120]({filename}/season10/issue120/issue120.md

As long as the “drivers” respond in the right way, the operating system continues to carry out its instructions as programmed.

How does one trick an operating system into coexisting with other operating systems on a single machine?

**Issue summary:** Programs do not usually deal with the gnarly details of hardware, but instead access it through an interface. They access storage devices through a filesystem, and access hardware through drivers.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 146: Virtual hardware

Examples incoming!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
