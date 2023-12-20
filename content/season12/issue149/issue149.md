Title: Issue 149: History of commercial computing - containerisation
Date: 2021-12-04 08:00
Tags: 
Category: Season 12
Slug: issue149
Author: J S Ng
Summary: Containers are one layer of virtualisation above virtual machines: containerisation systems virtualise access to the operating system, presenting a virtual interface that provides software with the resources it needs, without being aware of software running in other containers on the same system.
Modified: 2021-12-04 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Renting out virtual hardware instead of physical hardware meant that instead of having to move hardware around and manage it, you could send the *data* for running an OS to the hosting company and have them be responsible for hardware operations.

## Business concerns

Every business computer you have encountered likely runs an operating system (OS). And yet, what value does managing the OS have for the business? They have business software to run—point-of-sale systems, accounting systems, communication systems e.g. email—but the OS is no big concern for them, as long as it runs the software!

If I have point-of-sale software that only runs in Windows, and I’m paying for a company to provide it as a service, I don’t care if the software actually runs on Windows with direct hardware access, or if it is doing it through a virtual machine, *so long as it works*.

If I am going to help other companies run point-of-sale systems, one way to do it securely (so that data from different terminals/companies do not mix) would be to run a separate virtual machine (VM) for each system. I would do this through a [hypervisor](https://en.wikipedia.org/wiki/Hypervisor), a specialised _thing_ (software/firmware/hardware) meant for running VMs.

## Virtualising OSes

This is kind of wasteful; I am running multiple versions of the same OS to support as many copies of the point-of-sale system, even though they can all run on the same OS. I am just loathe to do so for security reasons.

What if we could apply virtualisation one layer up: instead of just virtualising hardware, we *virtualise the OS*?

To recap: when we virtualise the hardware, we provide virtual drivers that the OS can accept as valid hardware.

But programs don’t need real or virtual hardware; they need OS libraries which provide common resources and services: network, storage, compute, memory, windowing/display. If we can provide *virtual libraries* which respond like the actual OS libraries would, the programs would be able to run as normal.

The technology that enables OSes to let programs think they are running exclusively, protected from other programs, is called OS-level virtualisation, but more widely referred to as **containerisation**.

An OS (with the appropriate software & support) can run multiple **containers**, each container acting like a sandbox ([Issue 92]({filename}/season08/issue092/issue092.md))) for the software within. In each container, software has access to OS features, but are unable to affect software outside of the container. Each container appears to have exclusive access to (a portion of) the system’s network, storage, compute, and memory resources.

## Managing containers

The word **containers** may seem like a misnomer, for what are effectively software wrappers. But these do work almost like shipping containers: set up a container in an OS, install the required software, configure it, and now you have a container ready to meet business needs. You could send this container to any virtualisation service, they drop that container into their hosting system, and it runs like you expect.

**Issue summary:** Containers are one layer of virtualisation above virtual machines: containerisation systems virtualise access to the operating system, presenting a virtual interface that provides software with the resources it needs, without being aware of software running in other containers on the same system.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 150: System vs Process VMs

Up to this point, we have been looking at two different kinds of virtualisation: system virtualisation (virtualising hardware), and containerisation (virtualising operating system environments).

Next issue, we examine a third kind: process virtualisation.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
