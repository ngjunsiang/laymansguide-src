[**Previously:**](https://buttondown.email/laymansguide/archive/) To speed up execution and avoid translation overhead, some systems employ ahead-of-time translation, storing the translated instructions to be executed in future. But many systems employ a mix of just-in-time (JIT) and ahead-of-time (AOT) techniques.

This season, I’ll attempt to plug the gaps in the layperson’s working knowledge of Internet-related services. Time, location, wifi and mobile data ... almost all will be covered this season!

## Global time information

Frequent fliers would no doubt be familiar with the existence of timezones: geographical bands stretching from the North to South pole, within which all locations are assumed to be running on the same regional time. These timezones used to be manually synchronised, by phone or telegram, via operators all over the globe.

Today, [timezone information](https://en.wikipedia.org/wiki/Tz_database) and other time information required for global coordination are maintained by the [Internet Corporation for Assigned Names and Numbers](https://en.wikipedia.org/wiki/ICANN) (ICANN), which also maintains IP addresses and other lists of names and numbers owned by the [Internet Assigned Numbers Authority](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority), which we first met back in [Issue 27](https://buttondown.email/laymansguide/archive/lmg-s3-issue-27-what-is-an-ip-address/) when introducing IP addresses. These databases are used by programmers worldwide when writing programs that require time coordination.

## Time synchronisation

What about *syncing* time? Intuitively this process involves communication *between* computers, and anytime computers need to communicate, you can be sure a protocol is involved. We have seen a few protocols mentioned so far:

- HTTP, the Hyptertext Transfer Protocol, for sending web documents (aka webpages) and requests
- DNS, the Domain Name Service protocol, to translate domain names (like google.com) to IP addresses (like 142.250.64.110)
- DHCP, the Dynamic Host Configuration Protocol, used by routers to assign IP addresses to its client devices
- USB, the Universal Serial Bus set of protocols, used for data transfer between a host computer and another device

... I hope that’s enough for an idea of where protocols are involved.

The protocol for time synchronisation is called the [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP), in use since 1985—that makes it as old as me!

## Time sources

In the past, people would look at a common time source—the town square clock tower, Big Ben, church bells, and so on—to get the time. When watches were invented, people who had one would synchronise their watches to these common time sources.

But watches, clock towers, and other sources of time can get out of sync: one second as measured by each device does not accurately match the official definition of a second:

> The second is defined as being equal to the time duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the fundamental unperturbed ground-state of the caesium-133 atom.

That’s from [The International System of Units](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf/fcf090b2-04e6-88cc-1149-c3e029ad8232)[^1], which I am not inclined to argue with in a layman’s newsletter. Needless to say, synchronising to a universal standard is not something the average layperson does. Only select organisations have the need to keep such accurate time on their own, typically using such precise instruments as atomic clocks.

[^1]: If you need a term to google for more of this kind of geekery, it is called [metrology](https://en.wikipedia.org/wiki/Metrology), the scientific study of measurement.

How does the rest of the world get its time from these high-precision devices? It doesn’t; most of the world has no need for the sixteen zeroes of precision provided by an atomic clock. Instead, another cluster of servers synchronise their time to within microseconds of precision of these devices. And *another* cluster of servers synchronise their time to these microsecond-precision servers.

Each “layer of precision” is called a stratum in NTP. Time “trickles down” from higher-precision sources to lower-precision sources, down the stratum. As we descend the stratum, there are more and more devices providing time at that precision. If a time server synchronises to a stratum 1 server, it becomes a stratum 2 server; if it synchronises to a stratum 7 server, it becomes a stratum 8 server. The upper limit for stratum numbers is 15; a stratum 16 device is considered unsynchronised.

It is important to note that the stratum number is not an indication of quality or reliability, it only indicates distance from the reference time source.

## Operating a time server

NTP is an open protocol, which means the protocol is [readily available online](https://www.ntp.org/), and anyone can run their own server implementing this protocol. If you don’t want to write your own software, you can also use the [open-source ntp distribution](https://github.com/ntp-project/ntp), and compile it to make your own time server. Some large companies do this for their own large network, to improve the response time from time servers—public time servers, you can imagine, are under pretty heavy load!

## So is this how our smartphones synchronise their time?

More or less, yes. (They actually use a slightly simpler protocol, in the interest of preserving battery life.)

If you ever find yourself designing your own operating system (why would you do that though?) and having to provide a “set time automatically” feature, you can let your user connect to a public pool of time servers, [pool.ntp.org](https://www.pool.ntp.org/en/) (yes that is the actual name, and also the web address). This pool is further subdivided by continent and region, down to individual countries, since you will probably need specific time for your location. For instance, the specific time server pool for Singapore is sg.pool.ntp.org.

**Issue summary:** Time is synchronised from higher-precision sources through a protocol called Network Time Protocol (NTP). A public pool of time servers is available for synchronisation at pool.ntp.org.

I have been waiting ten seasons to write this, and it is finally out of my system!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 158: GPS

This issue is about time. Next issue is about location. With these two issues I would have explained time and space! 🤭

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
