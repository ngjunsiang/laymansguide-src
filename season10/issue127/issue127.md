[**Previously:**](https://buttondown.email/laymansguide/archive/) USB is a (licensed) technical standard that describes how devices connect to each other through a cable. USB Type-C is a new connector standard that supports USB 3, Displayport, HDMI, and Thunderbolt. It is able to carry multiple types of data simultaneously, in limited combinations. In a USB connection, one device acts as the host while the other acts as the device; the host initiates all communication.

Last week, I differentiated the USB Type-C **cable** specification from the USB3 **data** specification; the former describes how the cable and connector should be, while the latter describes how to transmit USB data over a Type-C cable. Remember that in addition to USB3 data, the Type-C cable can also transmit HDMI or Displayport video data!

What else can a Type-C cable do? Oh, right—provide power to devices. In other words, charge them.

## What’s wrong with USB2 charging?

Absolutely nothing! At this point, it was not expected that USB would be needed for powering anything more than some basic peripherals, like keyboards, mice, and anything less power-consuming than a small external hard disk. 5V of voltage with 0.5A could provide 2.5W of power, and that was considered plenty enough.

The USB Implementers’ Forum (USB-IF) didn’t want to set too high a standard for USB devices and peripherals (*including* USB-certified cables) because original equipment manufacturers (OEMs), who were the ones who actually had to manufacture the goods, would complain about the high cost. Nobody likes being undercut by cheap knockoffs that don’t bother applying for the license and following the specs (do you notice the official USB logo when buying?). So for a long time, we had up to 2.5W of power from USB.

And then tablets came along, drawing 8–12W of power to do whatever they have to. Aside from the iPad, these were charged over USB. So their manufacturers had to come up with *kludges* to work around USB limitations. They had Quick Charge, Dash Charge, and all kinds of other standards which were not approved by the USB-IF, just to allow their cables to provide up to 12W of power (3A of current, more in some cases) to their tablets while charging.

USB 3.0 bumped the limit up to 0.9A (providing 4.5W), which was nice but far from enough. The hard limit was the cable itself though: drawing anything more than 5A over the usual USB cables would cause them to heat up to unsafe levels. Clearly, something more was needed.

## USB Power Delivery

From 2012, the USB-IF finally added a Power Delivery (PD) specification, which allowed power to be delivered over USB cables at *different voltages*.

In addition to 5V, which is used by phones, tablets, and most power banks for these devices, the PD spec also allows charging at 9V (fast charging for some devices), 15V (for higher-power devices like the Nintendo Switch), and 20V (what most laptops use for PD charging). With a current of up to 5A, this technically allows up to 100W of power to be delivered—sufficient for pretty much all laptops!

### Which voltage is used?

The actual voltage to be delivered by the charging host is *negotiated* with the host. When a charging device is connected, it communicates the voltages it can support, the host compares it with the voltages it can supply, and power at a supported voltage is delivered.

### Can any cable be used?

Greater current requires a thicker cable to be used, as thinner cables have more resistance and will heat up to unsafe levels. A cable following the USB-PD specification will negotiate the correct voltage and current in any case, so if your cable is not charging at a level you know is supported by both your devices, do check the cable rating. You may have to buy a higher-rated cable.

## Any advantages from buying a more expensive cable?

Users of external monitor screens and docking bays often have to connect multiple cables from those devices to their laptops for power, (USB) data, and video output. With USB Type-C and USB-PD specifications unifying these three requirements into one cable, we will (eventually) be able to connect a laptop to a Type-C monitor using a Type-C cable, and this cable will supply power plus allow the laptop to use all devices connected to the monitor.

It’s supposed to simplify the physical cable mess, at the cost of having to manage a more complicated specification. Let’s see how that plays out in the next decade.

**Issue summary:** USB Power Delivery is a specification that describes how much voltage and current can be supplied by different categories of USB cables. It allows power delivery at different levels for all kids of connected devices, up to 100W. This should help to simplify cable setups that otherwise require multiple kinds of cables between two closely interconnected devices (such as a laptop and an external monitor).

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 128: Upgradability

Millennials and other older computer users may remember the glory days of the desktop, when almost any component could be removed and swapped out for another. Laptops used to enjoy this upgradability to a lesser extent; the laptop memory and hard disk came as separate slotted cards that could be replaced with upgraded versions for increased performance.

What happened to that trend today? The reason mainly lies in the realm of economics, but I figured I’d use the chance to dig a little deeper and explain what is going on with the hardware that no longer allows this to happen.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
