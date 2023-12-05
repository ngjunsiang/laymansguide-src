Title: Issue 146: Virtual hardware
Date: 2021-11-13 08:00
Tags: 
Category: Season 12
Slug: lmg-s12-issue-146-virtual-hardware
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Programs do not usually deal with the gnarly details of hardware, but instead access it through an interface. They access storage devices through a filesystem, and access hardware through drivers.

How does one trick an operating system (OS) into coexisting with other operating systems on a single machine? By _virtualising_ hardware into virtual drivers!

## Virtual network hardware

Let’s take an example. Take a look at your network devices: there's one for your LAN port, there’s one for your wifi card, and these days there may be one each for your Bluetooth chip and 4G/5G modem too.

If your workplace requires a VPN, you may have noticed that it adds a new network device. How is this possible if you don’t actually have any new network hardware?

Remember that in an operating system, access to hardware is mediated through drivers. A driver decides how to present its interfaces to the operating system. In essence, nothing prevents a driver from presenting multiple interfaces to the OS, provided the driver is able to receive requests and respond to them.

A VPN uses its own driver to present an additional interface to the OS, and that is how we end up with “virtual hardware”.

## Virtual storage

We are used to thinking of storage as referring to a hard disk, or solid state disk. But technically anything that is capable of representing bits can be used as storage—with an appropriate driver.

Some operating systems/programs provide drivers for RAM disks—a storage disk that uses computer memory. These appear as a normal disk drive (in Windows) or mountpoint (in Linux). Managing files in a RAM disk is speedy, because computer memory is much faster than a storage device.

## Virtual memory

In [Issue 55]({filename}/season5/issue055/issue055.md), I explained how the operating system offers and controls access to computer memory, the pagefile ([Issue 117]({filename}/season9/issue117/issue117.md)), as well as hardware devices through a single addressing interface: virtual memory.

When a program requests access to the printer and the OS responds with “here, you can send your request to memory address 0x35a4b2ff”, how is it to know if the data is going to a physical printer, or to a virtual one[^1]?

[^1]: These virtual printers do, in fact, exist. It is why some OSes offer a “Print to PDF” printer device: the program effectively sends print commands to another program, which interprets the commands to produce a PDF file. This is possible because both printers and the PDF format share a common language: Postscript (see [Issue 51]({filename}/season4/issue051/issue051.md)).

## Virtual hardware

Take a look at your Device Manager in Control Panel. What do you see?

![screenshot of Device Manager in Windows 10]({attach}issue146_01.jpg)  
<small>Device Manager in Windows 10  
Note that what you are seeing are not the actual hardware (which the OS cannot possibly know).  
These are interfaces to the hardware.</small>

A whole set of drivers and interfaces which the OS uses to carry out its work.

Many of these were initialised during bootup ([Issue 112]({filename}/season9/issue112/issue112.md)), when the OS kernel (the core of the OS) enumerates the available hardware by sending out signals and seeing what hardware responds.

So a bunch of engineers at VMware thought: what if we ... made drivers to present virtual hardware emulating the CPU, memory, storage devices, ... and even the chipset? What if we then we booted the BIOS (the bootup program loaded on a computer’s mainboard; see [Issue 112]({filename}/season9/issue112/issue112.md)), got the virtual hardware to respond when the BIOS enumerates hardware, and then basically simulated all the signals that hardware would actually send?

We end up with a virtual machine—one that you can actually install an OS on!

**Issue summary:** Virtual hardware can be created in the form of drivers that respond to a program’s requests for hardware resources. If a bootup program enumerates hardware devices and receives a response, then as long as it continues to receive valid and correct responses, it can work with the virtual hardware to run an operating system.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 147: Operating systems on virtual hardware

So ... what is it like to run an operating system on virtual hardware? Screenshots incoming!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
