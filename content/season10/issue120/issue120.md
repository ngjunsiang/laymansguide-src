Title: Issue 120: Drivers, the glue between hardware and firmware
Date: 2021-05-15 08:00
Tags: 
Category: Season 10
Slug: issue120
Author: J S Ng
Summary: Driver files provide information about the driver, and instructions on how to receive information from the device, and encode information to be passed to the device. The operating system may come with generic driver files for the device, but custom driver files might provide better performance or additional features.
Modified: 2021-05-15 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Solid-state disks are much faster than hard disks because they have no moving parts, so no time is wasted waiting for parts to get into the right position. However, they are more expensive than hard disk drives.

So this issue, we finally get to a question that most folks would have asked at some point after buying a new device:

“What is a (device) driver and why do I need one?”

This issue is going to focus on USB devices, since that is by far the largest category of devices that people use. But driver files are needed for all hardware, including disks, monitors, hardware timers, controller chips, …

## USB Devices

The USB specification was first released in 1996, and today it contains 21 categories of devices, each containing even more subcategories.

Each category of device has its own protocol for sending information to the computer, and receiving information from the computer.

I don’t think I am over-exaggerating things to say that there are an uncountable number of USB devices in the world today. For this reason, it makes no sense to complain to the [USB Implementers’ Forum](https://en.wikipedia.org/wiki/USB_Implementers_Forum) (USB-IF), which is responsible for designing the USB specification. Device manufacturers themselves have to be the one responsible for making their device work with our computers.

They do so by providing driver files with their devices. In a not-so-distant past, every device you bought came with drivers on a CD-ROM or DVD-ROM, which you had to install before use. Today, it is more likely that you’ll download these drivers from the manufacturer’s website. If this is a widely used device (e.g. monitors or input devices like keyboards or mice), it might even make its drivers (and updates to those drivers) available through Windows Update.

## What is a driver file?

Simply put, a driver file tells the computer:

- information about the device (its name, category, and available features)
- how to interpret signals coming from the device (through the USB cable),
- how to encode signals to be sent to the device so that it can understand them.

The USB-IF maintains a database of vendors and their products. Companies that wish to have their products recognised should [get a vendor ID](https://www.usb.org/getting-vendor-id) through the USB-IF; this also allows them to use the USB-IF logo (for USB-certified™) on their product packaging if the product passes certification.

When a device is inserted, it passes information including its vendor ID and product ID to the computer. Each driver file also includes the vendor ID and product ID it is meant for use with. This allows the computer to verify that the correct driver is installed for the device.

If you insert a device and Windows says it does not recognise it, you can be sure the problem has something to do with the device file (if the device is otherwise working properly).

On your computer, you can view a list of your devices and inspect their driver details using Device Manager.

![Device Manager in Windows 10]({attach}/season10/issue120/issue120_01.png)  
*Device Manager in Windows 10*    

## Generic drivers

When you first set up your computer, it is not going to have driver files for devices that are already connected. How are you supposed to use your keyboard, mouse, and monitor, among other things?

The major operating systems come with **generic driver files** pre-packaged. These generic driver files support a class of devices (e.g. input devices, pointing devices, display devices, …) for *basic features only*. Manufacturers that wish their devices to work upon plugging in (this capability is also known as **Plug-and-Play**) should aim to support these basic features through the use of generic drivers.

They can then encourage the customer to install custom drivers which may improve the device performance (e.g. for wifi or LAN networking devices), or provide additional features (e.g. storing mouse button configuration settings, or programmable mouse/keyboard buttons).

**Issue summary:** Driver files provide information about the driver, and instructions on how to receive information from the device, and encode information to be passed to the device. The operating system may come with generic driver files for the device, but custom driver files might provide better performance or additional features.

Driver files were one of those mysterious things that made perfect sense once I took the time to think about why they are needed. I hope this issue does that for you too.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 121: In graphic detail

One part I’ve always wanted to tackle with this season is explaining the process of getting graphics onto your monitor screen. The explanations I’ve found online are either too vague, trying to paper over the details with metaphors, or far too technical, going into exhaustive detail about the graphics rendering pipeline.

I want to strike more of a middle ground, to help those who have read the former and are trying to bridge the gap to the latter. The next two issues are going to talk about the processes involved in going from model (the computer’s view of things) to graphics (the final rendered display).

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- ~~a driver file and why do I need one? [Issue 98]~~
- a video card? [Issue 113]
