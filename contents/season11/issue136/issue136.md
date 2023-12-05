Title: Issue 136: The mobile workstation – laptops
Date: 2021-09-04 08:00
Tags: 
Category: Season 11
Slug: lmg-s11-issue-136-the-mobile-workstation-laptops
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) A modern CPU is manufactured through a process called photolithography, by which the CPU components are etched onto the silicon substrate by successive layers of chemicals, masking, and laser exposure. When the CPU components could be made small enough, the MCH and CPU were designed onto the same chip, and this is the design used by the Intel Core i7 (1st-gen).

In the last 4 issues, I walked through the general evolution of desktop computers. Let’s go more mobile, and look at laptops. How does something as big as a desktop shrink down to the size of a laptop? And what are the tradeoffs involved?

I addressed the power part of the formula in [Issue 130]({filename}/season10/issue130/issue130.md), on power limits; laptops are slimmer in part because part of them—the AC adapter—lies outside the system.

Let’s look at the rest of it.

## Laptops use slimmer components

Laptops use slimmer memory than desktops:

![Desktop memory vs Laptop memory]({attach}issue136_01.jpg)<br />
<small>Desktop memory (DIMM) vs laptop memory (SODIMM)<br />Source: [Quora](https://www.quora.com/What-type-of-memory-module-is-used-in-a-desktop-and-laptop-computer)</small>

On a desktop mainboard, desktop memory sticks out perpendicularly from the mainboard, all the better to cram memory sticks together and maximise the use of space.

On a laptop mainboard, laptop memory sticks lie parallel to the mainboard, to reduce the mainboard height and allow a slim laptop profile.

As far as I know ... there aren’t any other significant differences to highlight (besides size). Unless you’re overclocking, just get the kind of memory your computer/laptop needs. These days, small-form-factor desktops use laptop memory (SODIMM) as well!

Laptops use slimmer hard drives compared to desktops as well:

![Desktop hard drive vs Laptop hard drive]({attach}issue136_02.png)<br />
<small>Desktop hard drive (3.5″) vs Laptop hard drive (2.5″)<br />Source: [M2WifiCards](https://www.m2wificards.com/2-5-vs-3-5-hdd/)</small>

Desktop hard drives are larger, use larger platters (3.5″ diameter), and hence draw more power (at both 12V and 5V voltages). Laptop hard drives are smaller, use smaller platters (2.5″ diameter), and draw less power (at 5V voltage only). This is why smaller external hard drives, which use laptop hard drives, can be powered over USB, but larger external hard drives, which use desktop hard drives, need an external AC adapter.

These days, laptops have mostly made the transition to solid state disks, and you are much less likely to see hard drives in laptops.

## The slim laptop in 2010: Macbook Air

Let’s examine how a characteristic slim laptop, the Macbook Air, has changed in the past 10 years.

In 2010, the Macbook Air had its solid state disk and wifi network card on separate (replaceable) cards. But the CPU, GPU, and memory were all soldered directly onto the motherboard.

![Solid state disk in the 2010 Macbook Air]({attach}issue136_03.jpg)<br />
<small>The solid state disk in the 2010 Macbook Air<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+11-Inch+Late+2010+Teardown/3745)</small>

![Wifi network card on a 2010 Macbook Air]({attach}issue136_04.jpg)<br />
<small>The wifi network card on the 2010 Macbook Air<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+11-Inch+Late+2010+Teardown/3745)</small>

![CPU and GPU on a 2010 Macbook Air, exposed without cooler]({attach}issue136_05.jpg)<br />
<small>The CPU (left) and GPU (right) on the 2010 Macbook Air<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+11-Inch+Late+2010+Teardown/3745)</small>

![Mainboard of a 2010 Macbook Air]({attach}issue136_06.jpg)<br />
<small>Another view. CPU (red), GPU (orange), and memory (yellow) are directly soldered onto the mainboard<br />Where is the chipset? I don’t know; the Macbook Air does not seem to use the same chipset as Intel-powered desktops<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+11-Inch+Late+2010+Teardown/3745)</small>

## The slim laptop in 2018: also Macbook Air

By 2018, while the outside of the Macbook Air still looks much the same, the insides are rather different:

![Mainboard of a 2018 Macbook Air (top view)]({attach}issue136_07.jpg)<br />
<small>CPU (red) and solid state disk (yellow) are directly soldered onto the mainboard<br />Where’s the chipset? Notice that the CPU seems to have *2 chips* on it? They are the CPU and chipset; two chips in one CPU package!<br />The next image shows the reverse side. Other chips are ignored here, see the iFixit article for full identification<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+13-Inch+Retina+2018+Teardown/115201)</small>

![Mainboard of a 2018 Macbook Air (bottom view)]({attach}issue136_08.jpg)<br />
<small>Memory (red) and wifi network chip (orange) are *also* directly soldered onto the mainboard<br />This laptop only had integrated graphics; Intel had upped its integrated graphics performance sufficiently by this point<br />Other chips are ignored here, see the iFixit article for full identification<br />Source: [iFixit](https://www.ifixit.com/Teardown/MacBook+Air+13-Inch+Retina+2018+Teardown/115201)</small>

Components which in the 2010 Air were on separate cards are now all soldered directly to the mainboard! On the one hand, this saves space, which can be used for other features, or just for larger batteries. It also reduces the cost of manufacturing; connectors are costly to engineer and manufacture. On the other hand, it means upgradeability goes out the window.

**Issue summary:** Slim laptops have been undergoing a gradual transition: more and more of their chips are no longer available as a replaceable card, but instead soldered directly to the mainboard. Since 2017/2018, most slim laptops pretty much have CPU, memory, storage, and network chips all soldered directly to the mainboard.

Sorry about the image dump, I figured it would still be more convenient than having to click-through to see the images :)

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 137: The M1 Macbook Air

The M1 goes even further than the 2018 Macbook Air, in one pretty significant way. Next issue, we compare how the Intel and M1 Macbooks Air differ!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
