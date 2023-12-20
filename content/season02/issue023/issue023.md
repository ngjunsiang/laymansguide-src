Title: Issue 23: Specifications in software
Date: 2019-05-18 08:00
Tags: 
Category: Season 02
Slug: issue023
Author: J S Ng
Summary: 
Modified: 2019-05-18 08:00

Last week, we took a look at part of the (heavily simplified) software development pipeline:

`fork a repository → make changes → commit changes (and do automated testing) → merge changes when the branch is ready and all tests pass.`

At this point, it is time to ask a stupid question: how do developers know what they need to do?

## Software requirements

When a project is first accepted, the customer will usually have at least a vague idea of what they want the software to do. Hopefully, they will also have a clearer idea of what they want. For example, if they want an online shopping website, they might have some idea of they want shopping categories, a shopping cart, a search bar (with or without advanced search?), the ability to add or customise promotions, guest checkout, and so on.

Fine decisions, such as the checkout page—the order in which the text fields are arranged, the kind of date/time picker to use for the delivery schedule page, how users should be alerted if there’s an error in the input (alert below the text field or in a warning box at the top), also need to be made. And very often, the customer doesn’t want to make these decisions (which is why they hired a firm like yours to make the website), and so it falls to you (or your designers) to make these decisions instead.

What your customer wants—those are requirements. How the designers (or project lead, or whoever makes the decisions) decide to meet those requirements—those are called **specifications**.

## Specifications

There are more kinds of specifications than I can cover in detail, but let’s talk about some of the ones you are already familiar with.

### USB Specification (Hardware)

Did you know that USB was a specification? A group of engineers known as the [USB Implementers Forum](https://www.usb.org/) decides the specifications that USB devices must meet before they can be certified as USB-compatible.

The specification covers a few categories:

1. [Hardware requirements](https://en.wikipedia.org/wiki/USB_hardware#Connectors): Shape and dimensions of connectors, which pins (those gold contacts on the USB connector) are for power and which are for data, how to implement backward compatibility with older USB sockets, etc.

2. [Performance requirements](https://en.wikipedia.org/wiki/USB#Release_versions): Maximum data transfer rates, maximum charging power, etc.

3. [Operational requirements](https://en.wikipedia.org/wiki/USB#System_design): How transfers are to be implemented and carried out, supported types of devices and the type of transfer modes to use, how different features are to be implemented (e.g. audio streaming), etc.

### HTTP Specification

The [HTTP specifications](https://www.w3.org/Protocols/Specs.html) are maintained by the [Internet Engineering Task Force (IETF)](https://www.ietf.org/), an open community of people who collectively make the technical decisions about what the Internet should be able to do, and how it is going to do them.

[Take a look at some well-known specifications](https://www.rfc-editor.org/standards) that they have produced (click the links that say “ASCII”—yeah we’ll talk about ASCII sometime). It’s going to be way over your head, but don’t worry about that. Here’s an example from TCP, the Transmission Control Protocol that describes how packets should be sent over the internet:

```
3.1.  Header Format

  TCP segments are sent as internet datagrams.  The Internet Protocol
  header carries several information fields, including the source and
  destination host addresses [2].  A TCP header follows the internet
  header, supplying information specific to the TCP protocol.  This
  division allows for the existence of host level protocols other than
  TCP.

  TCP Header Format

    0                   1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                            TCP Header Format

          Note that one tick mark represents one bit position.

                               Figure 3.

  Source Port:  16 bits
    The source port number.

  Destination Port:  16 bits
    The destination port number.
```

Look at how specific these documents are about how data should be transmitted and received! These documents are how developers and programmers resolve arguments about who is writing their code correctly and who is responsible for a bug. The requirements have to be specific enough that the expected behaviour for a scenario is clear, yet leave enough room for better implementations to replace old ones.

### API Specifications

We [discussed APIs in an earlier issue](https://buttondown.email/laymansguide/archive/fe8b59fc-c5fd-49f2-9d01-9f21fa3df95c): an API describes how apps/programms should send and request information from each other. They are how web developers of online services know how to get you to use your Facebook account to log in, or how to access your phone contacts. APIs are another type of software specification: your app must communicate in a manner that fits the API specification, or it would not receive the desired response from the server.

### Time Specifications

We don’t think about it very often, but when someone writes 02/03/19, how do we know if they mean March second or February third of 2019? Such ambiguity is often disastrous in software applications, so there are clear specifications about how apps should standardise the commmunication of time between apps and across the Internet (for internet applications, the standard is [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)). Because computers and humans do not process time the same way ([see Wikipedia’s System time page](https://en.wikipedia.org/wiki/System_time)), there are specifications for how to do the conversion of machine representations to human-readable representations as well. And because this is applicable across many areas and not just in software, some of these specifications are called **standards**: specifications which should be followed by everyone who wishes to communicate clearly.

Think there are only 24 time zones? Or that time zones are always 1 hour apart? Or that the current timezones are exactly the same as they were 20 years ago? Think a leap second is always one second? That calendar time always moves forwards? That February never has more than 29 days?

I used to think these things too, until I read [Zach Holman’s detailed tract on UTC](https://zachholman.com/talk/utc-is-enough-for-everyone-right). Fascinating, and ever so slightly disturbing.

## Why are there so many specifications?!

Because they are useful!

When a developer first learns about specifications, it can be really alarming to find out that they haven’t been following many of them. They may even start feeling oppressed by the number of specifications that must be followed.

And then the developer advances. They tackle more finicky problems. They tackle problems that require more precision: time to the nearest nanosecond, synchronisation within a fraction of a second, lag time of no more than 200 milliseconds, etc. When they run into sufficiently difficult problems and find that they need help (such as the aforementioned time representations), that is where they will welcome the specification overlords into their life.

Many specifications were written because similarly talented developers ran into the same issue. And if there is no need to reinvent the wheel, those specifications save you many hours hashing out a suitable specification and implementation (since other developers would have offered sample implementations online), and enable your app to communicate with others who follow the same specification.

Specifications are part of an engineer’s toolbox in the struggle to create order from chaos, and a well-written specification is a thing of beauty.

**Issue summary:** Specifications describe the details of how a piece of hardware/software should work in order to meet a set of requirements. When well written and well implemented, they aid the coordination of the multitude of devices across the world, enabling them to communicate seamlessly, unambiguously, and unnoticeably with each other. Your devices work because they follow specifications.

-----

Yay, I finally cleared one item from the "sometime in the future" list! When I first started reading implementations, I found them really intimidating and impossible to get into. It was only when I started programming and having to do things like getting my data from an online service through an API, that specifications started making sense. Hardware specifications were useful too, in trying to understand whether a USB charger will be able to do quick charging or support higher rates of data transfer before I buy it.

Because making an app from scratch can be so stressful and annoying, developers usually separate the design work from the programming. Creating a specification and design for an app is both a science and an art, and when done well, can make programming a breeze. A developer just needs to read the relevant part of the specification, think about how to implement that section, and get it done.

Next week, we’ll look at something else that is part of a developer’s life as well: debugging.

## What I’ll be covering next

**Next issue:** Debugging

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n's in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
