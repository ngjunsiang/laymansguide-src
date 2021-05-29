[**Previously:**](https://buttondown.email/laymansguide/archive/) Analog formats such as VGA mostly contain the control signals that the CRT needs to operate, while digital formats such as HDMI and Displayport contain image data that the device must convert to control signals. Analog signals need a digital-analog-conversion (DAC) chip to be converted to digital signals, hence VGA-HDMI adapters tend to be more costly than Displayport-HDMI adapters. Dedicated graphics cards generally support more simultaneous output video streams than integrated graphics cards.

This week, I attempt to untangle the confusion around **USB Type-C**, informally also referred to as USB-C.

## What is USB Type-C?

It is a connector standard. It sets standards for *this* connector:

![Picture of a USB-C plug](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue126/issue126_01.jpg)<br />
<small>USB-C plug<br />Image via [Wikipedia](https://en.wikipedia.org/wiki/USB-C)</small>

What does a connector standard do? It determines how many pins the connector should have, and what each of the pins should be used for, how the connector should be shaped, how the docking port (where the cable gets plugged into) should be designed, and other similar details. It’s all about the docking.

![Pinout diagram of a USB-C plug](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue126/issue126_02.png)<br />
<small>Pinout diagram of a USB-C plug<br />Image via [Wikipedia](https://en.wikipedia.org/wiki/USB-C)</small>

## But won’t somebody think about the data?!

Ah, now we’re going back in history …

Universal Serial Bus (**USB**) is a (set of) industry standards that sets requirements and protocols for—well, how data is transferred from one device to another. It is maintained by the USB Implementers Forum (USB-IF). The first version of the standard was released in 1996, second version (USB 2.0) in 2000, and third version (USB 3.0) in 2008.

While USB 2.0 (or Hi-Speed USB) supported a transfer rate of *up to* 60 MB/s, USB 3.0 supports *up to* 625 MB/s, allowing for much faster transfers from external disks and other devices.

We don’t have to worry so much about these versions, because USB is designed to be backward-compatible. That means all devices that support USB2 also support USB1, and all devices supporting USB3 also support USB2. The primary advantage that each successive USB version has over previous versions is higher throughput, more supported features, and more connectors to confuse (okay, that last isn’t an advantage 😛).

![Connector shapes for different USB versions](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue126/issue126_03.png)<br />
<small>Comparison of USB connector plugs, excluding USB Type-C plugs<br />Image via [Wikipedia](https://en.wikipedia.org/wiki/USB_hardware)</small>

As you can see, this makes for a lot of confusion, especially when compatibility is mixed: USB2 ‘A’ connectors are meant to go into USB3 ‘A’ receptacles, but USB2 ‘B’ connectors aren’t meant to go into USB3 ‘B’ receptacles …!

So USB Type-C is meant to be the one connector standard to rule them all. It even has rotational symmetry, so it shouldn’t matter which way you plug it in!

## So what is a USB device?

Technically speaking, it is a device whose manufacturer has paid for a USB license, sent their device for certification, and passed the USB-IF’s certification requirements, allowing the manufacturer to put the USB logo on the packaging.

Practically speaking, it is any device that has a USB port, allows USB devices to be connected to it, or allows itself to be connected to other USB devices, and basically behaves like a USB device. (If it walks like a duck and talks like a duck …)

Furthermore, it is important to differentiate between a **USB host** and a **USB device**. The host acts as the controller of the device, and initiates all communication between the two. For instance, if you attempt to connect two Android phones to each other with a USB cable, one must act as the host and the other as a device, even if both are capable of acting as hosts. The host decides what can be done through the connection.

This helps to explain why a USB-charging battery pack cannot also be an external storage device *at the same time*, i.e. you cannot combine a phone battery pack with an external hard disk and hope to charge your phone + access the external hard disk at the same time. When your phone charges from the battery pack, it acts as the USB device (in charging mode); when it accesses a hard disk, it is acting as the USB host. It cannot do both simultaneously!

## Data supported over USB Type-C cables

In addition to USB3.0 data (and later versions of USB 3), the USB Type-C specification also allows the Type-C connector to carry other kinds of data, if supported by the device:

- DisplayPort video data for monitors and computer display devices ([Issue 124]())
- HDMI video data for monitors and consumer electronics devices (also covered in Issue 124)
- Thunderbolt 3 data, for high-data-transfer devices

The Type-C specification even supports modes that allow a Type-C cable to carry multiple types of data simultaneously. For instance, a Type-C connector that connects a laptop to a monitor can:

- carry DisplayPort video data, enabling the laptop to use the monitor as an external display,
- carry USB 3 data, enabling the laptop to use USB ports and other features (such as audio inputs/outputs) on the monitor

… All this comes with the caveat that one must read the manufacturers’ fine print to see if these features are supported on the respective devices. Just because the USB spec *allows* it, doesn’t mean that a particular device *implements* it!

For example, some laptops may have two Type-C ports, but *only one* of those ports will support Thunderbolt and DisplayPort; the other port sometimes only supports USB3 data.

**Issue summary:** USB is a (licensed) technical standard that describes how devices connect to each other through a cable. USB Type-C is a new connector standard that supports USB 3, DisplayPort, HDMI, and Thunderbolt. It is able to carry multiple types of data simultaneously, in limited combinations. In a USB connection, one device acts as the host while the other acts as the device; the host initiates all communication.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 127: USB Type-C Power Delivery

This issue was about how data is handled over USB Type-C. Next issue, how *power* is handled over USB Type-C. After all, every day, millions of devices are getting powered over Type-C: from smartphones, to Internet-of-Things (IoT) devices, to full-size laptops. How is a single type of cable able to cover such a wide range, when earlier cable types could not?

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
