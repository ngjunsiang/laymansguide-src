Title: Issue 105: Operating Systems
Date: 2021-01-30 08:00
Tags: 
Category: Season 9
Slug: issue105
Author: J S Ng
Summary: 
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Shared secrets allow secured access to resources, such as databases or other services. These shared secrets are typically kept on a server controlled by the app developer. For mobile apps, they are usually stored with the operating system, inaccessible to other apps.

Last season, I explained the differences between web apps, mobile apps, and laptop apps. Web apps operate in a browser environment, mobile apps operate in a mobile operating system (OS) environment, and laptop apps operate in a desktop OS environment.

The OS is that complex piece of software between the apps and the hardware that runs it all. The hardware speaks its own special code, while apps are run in machine code written for the CPU. The OS makes sure that everything runs smoothly.

What does **everything** entail?

## What an operating system does

### 1. Boot-up

When the machine is powered on, how does it know what hardware is available? This hardware discovery is done by the bootloader (which for the purposes of explanation we can consider as part of the OS). It checks for the available hardware resources, and compiles a list of them for the operating system. Added some memory? Added a new hard drive? The bootloader should detect it.

### 2. Login and user management

While a personal computer (PC) might have only one user, many PCs are used by more than one person. Multiple login accounts allow each user to have their own space on the computer for their files.

In addition to the user accounts, an operating system also creates multiple system accounts to manage services on the OS.

### 3. Window management

Ever wondered how apps on a PC can have their windows styled so similarly? That’s because the OS provides a standardised window style for apps, with standardised actions that can be performed (maximise, minimise, close, resize, …). Apps can choose not to use this standardised window style, but then they are on their own when it comes to window styling, and they will have to write their own code for all of these actions.

### 4. Memory allocation and deallocation

Applications primarily run off computer memory, which is a hundred times faster than the hard disk (I’ll explain more in a future season). When an application is first launched, it is allocated a small amount of memory space for its data. If it wants more, it can’t just reach for the memory space and grab more chunks as needed; other apps are using memory as well, and it might inadvertently overwrite data stored by other apps.

So instead, access to memory is mediated by the OS. All requests for more memory are sent to the OS, which will return addresses for available chunks of memory. And any memory that the app frees up is released back into the common pool, for use by other apps.

### 5. Storage interfaces

Applications do not need to know how the user has their computer set up: what kind of disks they have, or which disk they put the OS on. But what if they need to allow the user to save a file, or load an existing file? The OS provides standard interfaces for doing so—you would likely have seen the “Select A File” interface on any OS. The OS takes care of file reading and writing, sparing the application developers from having to worry about the details.

### 6. Background services

Applications run by the user typically expect input only from one user; if you are running Microsoft Word at the same time as your sister, each instance of Microsoft Word expects to interact with either you or sister. However, there are special system applications that often have to deal with input from multiple users. For example, antivirus software or Windows Printer Management need to run for all users at the same time, and should not be terminated like a typical program.

These applications thus run differently: they run as background services, which are special applications which do not interact with the desktop. Background services are managed differently from applications, and typically can only be terminated by the system administrator.

### 7. Peripheral management

Do you use Bluetooth wireless headphones? USB devices of any sort? Did you just buy a new gamepad? The OS detects them and takes care of driver installation (usually). You can see all detected devices and installed drivers in the Device Manager, under Control Panel, in Windows 10.

I’ve just covered the main ones that most users would use on a regular basis. The OS manages much more stuff, including OS updates, per-user settings, etc—remember the Registry Editor? ([Issue 100]({filename}/season8/issue100/issue100.md))) For a look at what else the OS manages, take a peek in the Control Panel or System Preferences of your OS.

These form a supporting network of services that applications can draw on. Instead of having to work out the full details of implementation for each of these features, they can use the OS’s provided functions to do the work for them. These functions are typically bundled in a standard library ([Issue 17]({filename}/season2/issue017/issue017.md))) provided by the OS manufacturer. For example, [.NET](https://dotnet.microsoft.com/) is a collection of libraries for Windows applications that developers can use to simplify their work.

**Issue summary:** The OS takes care of booting up, login and user management, window management, memory allocation, storage interfaces, background services, peripheral management, and much more. Access to these services, where allowed, is provided in the form of software libraries that developers can use.

I’ve touched on per-user data storage in Season 8, and on memory allocation in Season 5, so I will skip those for the rest of this season. Window management and background services isn’t going to be interesting for a layman’s guide, so let’s skip those too. Instead, I will try to set the stage for a next season about hardware, by explaining more about how storage and computer peripherals work, and how the operating system simplifies access to them. and then I’ll get to booting up—how a computer gets ready from the moment you press the power button.

If I still have issues left after that, I might geek out a bit and talk about fonts ;)

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 106: Organising storage

First up: How exactly is data organised in the hard disk? How does an operating system manage it all?

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- How do apps know where a file starts and ends? [Issue 49]
- a driver file and why do I need one? [Issue 98]
- why does computer memory exist when apps can read directly from the hard disk? [Issue 105]
