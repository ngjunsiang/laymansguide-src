In Season 2, I took a detour to introduce some cool things that developers typically work with, and ideas they implement to make their work as smooth as possible.

And now we’re back on track, where I last stopped in Season 1. There, I did a little dive into my app to introduce [HTTP](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/), the protocol that forms the *de facto* means of communication for the internet. And then I showed some [HTTP requests](https://buttondown.email/laymansguide/archive/lmg-issue-9-how-do-i-make-an-http-request/), the basic means of requesting data from servers, served over unsecured HTTP and secured HTTPS, and I hope that illustrated sufficiently why HTTPS is really important.

In Season 3, I’ll continue where I left off. We’ll see where that HTTP request packet goes, and what this Internet thing looks like on the outside.

## The HTTP packet, revisited

<span style="text-align:center">
![An HTTP request captured in Wireshark](https://github.com/ngjunsiang/laymansguide/blob/master/season1/issue012/issue012_01.png?raw=true)<br />
Remember this from [Issue 12](https://buttondown.email/laymansguide/archive/lmg-issue-12-what-is-https-how-is-it-different/)?
</span>

The two columns (Source and Destination) that I censored out contain my IP address, and Hypothes.is’s IP address. Why would I want to censor that? I hope this and the next few issues will make it clear.

When my laptop sends out the HTTP packet, the radio waves containing the data do not have enough energy to reach all the way to wherever Hypothes.is’s servers are based. Instead, before they completely dissipate to undetectable levels, my router has to receive them (just like a radio receives FM waves with its antenna), decode the information, and pass it forward to my ISP’s server, which then forwards it to another server … until it finally reaches the Hypothes.is server.

How does it do that?

## The IP address

Each HTTP packet contains information about the source of the packet (i.e. my router), and the destination of the packet (i.e. Hypothes.is). This information is encoded as a string of four numbers, ranging from 0 to 255 (the smallest possible combination is 0.0.0.0, the largest is 255.255.255.255).

This string of four numbers is known as an IP address.

If you are good at math, you can work out the total number of available combinations: it’s 4,294,967,296 (256^4). It seems like a lot, but we actually have more humans on this planet than we have IP addresses. And if we assign a unique IP address to each device on the Internet, many of us will need multiple IP addresses for our smartphone, laptop, Amazon Echo, smart TV, router, …

IP addresses are a limited resource! They are really precious! If you don’t have one, nobody would be able to send you anything. The HTTP packets that other people send will never reach you. The HTTP packets you send will not have an IP address in the Source column above. You would be cut off from the internet. (Less dramatically, you would be offline.)

When you sign a contract with your ISP for an internet connection, they might give you a free router and other niceties or freebies. But the most important thing they give you is the privilege of using one of the IP addresses they own.

## Wait what?! Why do the ISPs get to hog all the IP addresses?

A long long time ago … well, actually just back in 1987, a bunch of internet pioneers came together and published a list of reserved IP addresses in [RFC1010 (starting on page 16)](https://tools.ietf.org/html/rfc1010). The RFCs (**R**equest **F**or **C**omments) are documents published by the Internet Engineering Task Force (IETF) for interested folks to review. Considering the magnitude of responsibility involved, a committee was drafted … and the [Internet Assigned Numbers Authority](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority) (IANA) was born in 1988.

IANA parcelled out IP addresses to regional Internet registries, which further subassigned them to smaller Internet registries, such as your ISP. Lots of money was involved, unsurprisingly. To own an IP address means to have every registry out there agree that all data packets intended for that IP address should be forwarded to your server. That’s a lot of obedience you own, and it will cost you.

Okay, so how do those packets actually make their way to you if they don’t originate anywhere near you?

## Forwarding Tables and The Gateway

Your smartphone, or laptop, first sends the packet to its gateway (which is typically your router). Your router differs from your handy gadgets in one key way: it is a server, while your gadgets are clients ([I covered clients and servers in Issue 7.](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/)). The router contains a forwarding table, which is a table telling it where to forward data meant for various IP addresses. For example, if you are trying to send a document to your home network printer, that data packet is not meant to go out onto the Internet—it’s meant to be forwarded to the printer! The information in the forwarding table ensures that this happens. Your laptop has no idea what the IP address of the printer is; all it knows is your router’s IP address, and it will forward everything to your router for it to figure out.

<span style="text-align:center">
![Network connection properties window](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue027/issue027_01.png?raw=true)<br />
Network connection properties, a window that one used to see very often when configuring a router. [Source: Help Desk Geek](https://helpdeskgeek.com/networking/change-ip-address-and-dns-servers-using-the-command-prompt/)
</span>

If the destination IP address is not in the forwarding table, the data packet gets forwarded to **your router’s gateway**, which is typically your ISP’s router. The ISP router then checks its forwarding tables to see if the destination address is in there (maybe the data packet is meant for one of your ISP’s customers?), if not it gets forwarded to the next gateway … a few hops and bounces later, it finally reaches its destination. Phew!

**Issue summary:** IP addresses are a string of four numbers. A list of reserved IP addresses is managed by IANA, and all Internet registries agree to forward data packets according to that list. A data packet sent from a client goes to its gateway. At the gateway, the destination IP address is checked against the gateway’s forwarding tables. If the IP address is found in the forwarding table, it gets sent along that route, otherwise it gets forwarded to the next gateway, … until it reaches its destination.

<hr/>

This looked like a good place to stop before I get any deeper. I’ve left out a lot of the history of development of the internet and Internet Protocol (which is where the acronym IP comes from), because it is necessarily messy and not really relevant here. But one important result of these developments is that there isn’t a single master server out there to which **all** data packets must go to be sorted. This makes the Internet more robust (if one gateway fails, your packet can still reach its destination via other routes), but more importantly it prevents server owners from dominating the entire Internet and its development (because whoever owns that master gateway will hold great sway over the flow of information).

## What I’ll be covering next

**Next season:** Domain Names (because who memorises IP addresses anyway?)

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
- compiling code into an application [Issue 26]?
