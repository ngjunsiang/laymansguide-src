Title: Issue 148: History of commercial computing - cohosting
Date: 2021-11-27 08:00
Tags: 
Category: Season 12
Slug: issue148
Author: J S Ng
Summary: 
Modified: 2021-11-27 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Running a virtual machine is like running a physical machine, but within a window in your OS.

## Co-located hosting

A not-so-long time ago, to run a website, you literally just ran a webserver on your desktop, connected it to the internet, and gave your IP address to other people. This is a pretty unreliable way to host a business website though. A big company would make business arrangements to procure a reliable internet connection, set up the infrastructure (power, cooling, mounting hardware) required to run multiple computers, and then manage their multiple systems with a full IT management team (hardware & software).

Not every company can afford this. Smaller companies would therefore **co-locate** their computers (called colo boxes) with bigger companies, enjoying service support and infrastructure for a monthly/yearly fee. Some companies decided to just provide these services as their full-time business, and the hosting business was born.

## The difficulties of troubleshooting remotely

Running your computer on someone else’s premises is no joke. If something went wrong, there was no way to do troubleshooting remotely. You had to drive down and do the troubleshooting onsite, usually wasting at least half a day in the process. Unsurprisingly, this was a problem many companies were happy to abstract away by paying more money. Soon, hosting companies offered to rent your _their_ computers, configured to standard specs, _and_ provide basic onsite troubleshooting. You would email/send them the software you wanted to run on those computers, with instructions, and they would do it for you. A huge timesaver; most hardware issues are now out of mind for business owners.

You still had to worry about OS issues though. If you need to have multiple pieces of software set up and configured, this was something a hosting company could not do for you. And this was where virtual machines (VMs) came in handy. What if you could set up a virtual machine, with virtual CPU and virtual memory, install your OS on a virtual disk, install all your required software in that OS, and then send that virtual disk (as data) to a hosting company? They would then run that disk through their hypervisor, a piece of software that manages virtual machines.

## The promise of virtualisation

This was the promise that virtualisation companies offered to businesses. You could manage your virtual machines remotely, choosing when to boot them up or shut them off, paying only for virtual hardware you requested, without affecting the virtual machines of other companies. Hosting companies could “collect rent” for multiple VMs running on a single computer.

After all, as long as you have an interface to manage it, and you are able to set up your software on it, does it really matter whether it is a physical or virtual machine?

**Issue summary:** Renting out virtual hardware instead of physical hardware meant that instead of having to move hardware around and manage it, you could send the *data* for running an OS to the hosting company and have them be responsible for hardware operations.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 149: History of commercial computing - containerisation

Can we push this further? Could we get hosting companies to not only help us run the hardware, but the operating system as well? Yes, yes we can!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
