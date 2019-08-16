Previously: Private IP addresses are special IP addresses that routers will treat as belonging to devices within the private network, and not outside it. Data packets sent to private IP addresses will never make it past the gateway into the internet. This system allows multiple devices within a private network to share a public IP address.

Last week, I tried to answer the question "how do all my devices manage to share the one precious IP address assigned to me by my ISP?", and in the process introduced two more acronyms: DHCP and NAT. I don’t intend to spam this newsletter with acronyms, but to use them as neat little terms that conveniently capture ideas about how different parts of the complete Internet experience works. So if you never remember what DHCP is, don’t fret over it; you won’t see it often unless you configure routers or servers often.

In a nutshell, DHCP is how you get a (private) IP address when you connect to your router. Before that, here’s one of those niggly little problems that the early Internet pioneers ran into in trying to write awesome services:

## MAC address: Media Access Control address

When your phone/laptop/device first connects to the router, it needs to know what its private IP address is, so it can begin stamping data packets to be sent. It doesn’t have a private IP address yet, so it has to ask the router for one. But if it sends the IP address request, how would the router know who to reply to?

The answer is that each device (or more specifically, the networking chip of the device) has a unique hardware code, known as the **MAC address**. It will stamp the request with its MAC address first, so the router knows who to offer the IP address to.

The MAC address can also be used to do many other things, like block devices on a network; we’ll get to those other things in future issues ;)

## DHCP: Dynamic Host Configuration Protocol

So what happens after that? your device asks for an IP address, and the router reserves one from its pool of private IP addresses and offers it to the device. the device accepts the request, and the router adds the device IP address to its forwarding table. Done.

It’s called a dynamic process because the router assigns private IP addresses only upon request, so a device may not always end up with the same IP address.

## Static vs Dynamic IP addresses

One potential drawback of this dynamic process is that if you are trying to set up a network printer the Old Way, it will ask you to input the address of the printer. And unless you have figured out internal DNS on your router and properly hostnamed all your printers, you will be providing this address not as a hostname (like printer.home.com) but as an IP address (192.168.1.5).

<span style="text-align:center">
![Add Printer dialog asking for an IP address](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue031/issue031_01.gif?raw=true)<br />
An old printer management dialog window for adding printers. [Source: UC Davis Coastal And Marine Science Institute](https://marinescience.ucdavis.edu/bml/facilities/it/instructions/mac-how-add-network-printer-ip-address)
</span>

But when you reboot your network printer and it requests an IP address from the router again, will it get a different one? Will you have to re-add the printer again?

Not if you get the router to assign it as a static IP address. The router can store a list of MAC addresses and their associated static (private) IP addresses, so that the device will always get the same IP address.

## DHCP and your ISP

One more thing you need to know about DHCP: when a device requests an IP address, it’s not going to get that IP address forever. IP addresses have a lease (5 days by default), after which the IP address will expire and the device will have to request a new IP address.

It’s the same thing with your ISP. Your home router, even if it is left on 24/7, will have to renew its (public) IP address with your ISP every few days, as and when it expires. So your ISP also (most likely) assigns you IP addresses by DHCP; you are not going to enjoy the privilege of a static IP address unless you pay gobs more money!

## Wait: why are static IP addresses such a privilege?

Remember what a public IP address is? It’s a way for data packets to get to you wherever they are sent from. And that is possible because of the forwarding tables stored in Internet registries everywhere (including your ISP). All over the world, anyone who knows your IP address can send your router data.

But often they won’t do so. They will use a URL instead, because they are easier to remember.  The sender finds out what IP address the domain name is assigned to by querying its DNS servers ([Issue 28](https://buttondown.email/laymansguide/archive/lmg-s3-issue-28-domain-names-and-dns/)).

If you want your own domain name, you have to buy one at a domain name provider. This lets you add your unique domain name to the WHOIS database ([Issue 28](https://buttondown.email/laymansguide/archive/lmg-s3-issue-28-domain-names-and-dns/)) … but you need an IP address to map to your domain name. And you can’t use your ISP-assigned IP address, because it’s dynamic and changes when the lease expires … can you?

## Dynamic DNS

Some domain name providers offer a service known as Dynamic DNS (**DDNS**). This service lets you run software on your computer or a sufficiently advanced router that will update the provider whenever your public IP address has changed. So if you want to be able to stream videos from your own home server for your own viewing, without going through a cloud service, that is possible! But we won’t go into the details here ;)

**Issue summary:** DHCP is a protocol by which a router assigns IP addresses to devices that connect to it. Static IP addresses are IP addresses that are reserved for a device, so that the device always gets the same IP address when it connects.

<hr/>

I had almost forgotten about DDNS, and decided to include it at the last minute, making this a bit longer than I had aimed for. But I hope this fleshes out your model of the Internet a little more, so that you understand how it is possible for you to have your own domain name too.

I usually introduce new terms and acronyms in bold, but I didn’t bold DHCP here. You won’t ever need that acronym again and you will probably forget it if you don’t do router configuration, and that’s just how things should be.

## What I’ll be covering next

**Next issue:** How do packets from my device get out onto the internet, and how do they come back to me? Network Address Traversal (NAT)

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
