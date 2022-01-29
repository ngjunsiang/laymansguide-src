[**Previously:**](https://buttondown.email/laymansguide/archive/) To get your location using GPS, your phone requests information from four overhead GPS satellites: their location, and the distance between them and your phone. With this information, your phone can calculate its location.

Okay, so what happens when you are in a tunnel or building and can’t get GPS? How are you still able to use Google Maps to navigate that new sprawl of a mall?

## Wifi Positioning System (WPS)

The principles of triangulation still work within a building, thank math 🙏 but now we need other landmarks to replace GPS satellites.

What is something with a known (and ideally fixed) location, is electrically powered to receive and respond to signals, and there are enough of them to provide a sufficient number of landmarks for triangulation? If you are in a building with wifi, the wifi access points scattered throughout the building can probably provide this.

No protocol is involved in [wifi positioning](https://en.wikipedia.org/wiki/Wi-Fi_positioning_system), largely because most routers do not carry a precise hardware clock and do not have any way to know their location precisely, and therefore cannot communicate this information meaningfully. Instead, wifi positioning is a collection of techniques for *guessing* your location. Your smartphone uses these techniques (usually through its operating system) in conjunction with available wifi networks around you to determine its own location.

## Wifi positioning techniques

One way to figure out your location to proximal wifi points is to use the signal strength as a weak analogue for your distance from them. You can do a very rough position estimate with this.

Another common technique is to look up the hardware address, or even IP address of the wifi point you are connected to, and just use it directly (with the assumption that wifi signals get too weak outside of a 10 m radius, so you have your location accurate to within ±10 m).

## Wifi location databases

One way to keep track of wifi access points and their locations is through a global, public database. [A number of these](https://en.wikipedia.org/wiki/Wi-Fi_positioning_system#Public_Wi-Fi_location_databases) are available, such as the [Mozilla Location Service](https://location.services.mozilla.com/).

## Cell tower triangulation

What happens when you are outdoors, far from any wifi point? As long as you have mobile data enabled and are not in airplane mode, you are still going to be getting your cell signal from a cell tower ... which also meet the three basic criteria for device-based triangulation 😉

Your smartphone can thus triangulate its location from cell towers that it is able to reach. Again, there is no protocol for this, since your smartphone does not communicate with the towers for the express purpose of obtaining location; it is a set of similar techniques, often implemented in the operating system.

## Power savings

Because wifi points and cell towers are much nearer to your smartphone than GPS satellites are, much less power is needed for transmitting to them. For this reason, smartphone OSes often ask you to allow the use of wifi for determining position even if you have decided to switch wifi off.

**Issue summary:** Instead of GPS satellites, smartphones can also use wifi points and cell towers to determine their position (if enabled in the OS).

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 160: CDNs and content distribution

Coincidentally, starting with time turned out to be a good idea: time information is sort of like content. It has an origin, and it gets distributed to “consumers” who want that information. As with all distribution systems, you have cascades of product that flow outward from this origin.

We have covered time and space (I mean, location). Let’s move on to data: how does data get around the world from a few central sources?

Back in [Issue 73](https://buttondown.email/laymansguide/archive/lmg-s6-issue-73-the-heart-of-darkness-header/), when I explained how online advertising works, I mentioned that advertising content is served from a content delivery network (CDN). What is this and how does it work?

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
