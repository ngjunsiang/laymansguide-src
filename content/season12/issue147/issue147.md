Title: Issue 147: Operating systems on virtual hardware
Date: 2021-11-20 08:00
Tags: 
Category: Season 12
Slug: issue147
Author: J S Ng
Summary: 
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Virtual hardware can be created in the form of drivers that respond to a program’s requests for hardware resources. If a bootup program enumerates hardware devices and receives a response, then as long as it continues to receive valid and correct responses, it can work with the virtual hardware to run an operating system.

So ... what is it like to run an operating system (OS) on virtual hardware? I promised screenshots, but they probably won’t be as exciting as you expect—it looks quite normal!

## Creating a virtual machine

I don’t want to purchase a VMware license, so I will be using an alternative virtual machine product instead: Oracle’s free Virtualbox. This is what it looks like, running on Arch Linux on my laptop:

![screenshot of Virtualbox in Arch Linux]({attach}/season12/issue147/issue147_01.png)  
<small>Virtualbox main interface</small>

Let’s create a new virtual machine. It asks which OS I intend to use, presumably so it can pick the right virtual hardware to use (MacOS virtual machines may be more picky? I’m not too sure here either). I don’t have a valid Windows license to use, so I’m just going to demo with Arch Linux instead.

Whichever OS you pick, you are going to have to find a way to install that OS into your virtual machine—whether you are using actual boot media (such as a DVD drive), or virtual media.

![Creating a virtual machine in Virtualbox]({attach}/season12/issue147/issue147_02.png)  
<small>Creating a virtual machine</small>

Cool, you actually get to configure how much of your computer’s memory the virtual machine will get to use.

![Configuring memory size in Virtualbox]({attach}/season12/issue147/issue147_03.png)  
<small>Configuring memory size</small>

Without a storage disk, a computer isn’t much. Virtualbox needs *something* it can use as a disk; the usual way is to create a file on your system that Virtualbox uses as a virtual disk. The space occupied by this virtual disk can be preallocated up front (so that your virtual machine doesn’t accidentally “run out of storage space” before the disk is full), or it can be dynamically allocated, only taking up as much space as is actually used.

I don’t have an existing virtual disk file, so I will ahead and create one here (not shown). If I have one from a previous installation, I can use it here instead.

![Configuring virtual hard disk in Virtualbox]({attach}/season12/issue147/issue147_04.png)  
<small>Configuring hard disk</small>

The machine is created; the main interface now looks like this. Note that all the “hardware” you see there is virtual!

![Virtualbox main interface, with one virtual machine]({attach}/season12/issue147/issue147_05.png)  
<small>Virtualbox main interface, with one virtual machine</small>

If you are doing this on your own computer, at this point you might want to go into Settings and see what else you can toy around with: number of (virtual) CPUs, sharing some folders on your system with the virtual machine (they show up as shared network folders), adding more disks or even a virtual optical drive, etc.

----------

## Setting up boot media

I could try to boot it now, but I already know it won’t work; there is nothing in the hard disk to boot from. With a physical computer, at this point we will attempt to install the OS from a DVD drive or flash drive. You could allow your virtual machine to access the DVD drive or flash drive in order to do this, or you can do it virtually. Most operating systems (including Windows) provide virtual boot media for installation: an ISO file is a virtual optical disk.

I can download the ISO boot file for Arch Linux, but it seems they have gotten savvier lately and actually provide virtual boot media in the form of *virtual hard disks*! Let’s use that instead. I add it as a second virtual disk in Virtualbox:

![Virtualbox hard disk configuration]({attach}/season12/issue147/issue147_06.png)  
<small>Virtualbox hard disk configuration. packer-virtualbox.vmdk is the virtual boot media for Arch Linux</small>

Once I start the virtual machine, it begins its boot sequence, and I interrupt it by pressing F12 to go to the boot menu (otherwise it will attempt to boot from the main virtual hard disk, and fail to detect any OS). Interesting to see here that it isn’t actually connected to a monitor: virtualbox presents a virtual display device, to which the virtual machine sends its video signal. Virtualbox captures these signals and displays them within the window instead. So you can flexibly configure the window size, and the virtual machine just thinks the display device it is connected to has been resized.

![Virtualbox boot menu]({attach}/season12/issue147/issue147_07.png)  
<small>Virtualbox boot menu. Through the virtual (AHCI) disk controller, the virtual machine detects two (virtual) disks: the new disk I created, and the Arch Linux boot media that I loaded.</small>

## Running a virtual machine

I select the second disk to boot up Arch Linux for installation, and the login prompt appears:

![Virtualbox login prompt]({attach}/season12/issue147/issue147_08.png)  
<small>The Arch Linux login prompt, in Virtualbox. Yes, this is how Arch Linux gets installed the first time.</small>

I wont go any further at this point, because then I’d just be showing you how to set up Arch Linux. But I trust this is enough to give you an idea: running a virtual machine feels just like running a physical machine, but in a window!

Okay hold on, how do we shut this thing down? It is not recommended for a computer to be unplugged without a proper shutdown, so ... how do we do that with a virtual machine?

Even the powerdown and reset buttons on a computer are actually hardware signals which the OS receives and uses to trigger a series of actions. We can send these signals virtually too, through Virtualbox’s Machine menu:

![Virtualbox Machine menu]({attach}/season12/issue147/issue147_09.png)  
<small>The Virtualbox Machine menu.</small>

And with that, let’s shut it down.

**Issue summary:** Running a virtual machine is like running a physical machine, but within a window in your OS.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 148: History of commercial computing - cohosting

Right, so this has been really cool and all, but not something a layperson would use on a daily basis usually. And the setup still seems ... rather technical? So why does this deserve its own season?

Remember that this happened before the turn of the century, so the tech industry has had two decades to figure out how to make money out of this. And two decades is the equivalent of a whole lifetime in this industry. How did virtualisation change the landscape of commercial computing? Time to take another walk in recent history.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
