Title: Issue 34: Firewalls
Date: 2019-08-17 08:00
Tags: 
Category: Season 3
Slug: lmg-s3-issue-34-firewalls
Author: J S Ng
Summary: 

Previously: Data is encapsulated when it goes out from an app onto the internet as a request or response. First, in the TCP layer, the OS tags the request with the pre-assigned port number so that it can forward the response to the correct app later. Next, in the IP layer, the network card adds source and destination IP address information so that the data packet arrives at the correct destination server, and the destination server can send the response back to the correct computer. As the packet goes through the router, the router replaces the (source) private IP address assigned to the device by the router with the public IP address assigned to the router by the ISP.

If the above summary of Issues 30–33 makes sense to you, you are probably ready to proceed :) If not, you might want to review those issues quickly through the links below:

[Issue 30]({filename}/season3/issue030/issue030.md)): Private IP addresses  
[Issue 32]({filename}/season3/issue032/issue032.md)): Sharing a public IP address: Network Address Traversal  
[Issue 33]({filename}/season3/issue033/issue033.md)): Port numbers  
[Read the rest of the archives here.](https://buttondown.email/laymansguide/archive)

Okay, now we understand how the open, unfettered internet of the 1990s worked. But we are still nowhere near understand the modern Internet until we understand how security is applied. Let’s look at one of the earliest features first.

## Firewall: a wall to prevent the spread of fire

A software firewall performs an equivalent function: to prevent the transmission of an identified packet through it.

Of course, that means it must be able to be configured with rules that enable it to check the data packets to see if they should be allowed through. What kind of rules can be written for a firewall? That would depend entirely on what information is available in the data packet.

## IP and port number filtering

Thus far, we know that the outermost layer of the data packet is the IP layer, which contains IP address information. A firewall can simply block out data packets coming from a certain source IP address, or being sent to a certain destination IP address. This lets a router administrator block certain devices on the network, by blocking data packets with source IP address matching the private IP address of the device. It also allows an ISP to filter out certain servers from receiving data packets from its customers, by blocking data packets with destination IP address matching the public IP address of the server.

Do this with a sufficiently comprehensive list of IP addresses, and you can completely block out an entire region’s or even country’s servers. And it would take a VPN to circumvent this, if the VPN server’s IP address is not in the firewall’s block list.

At the next level, the TCP layer contains port information. A firewall can block out all web browser traffic by restricting data packets with port number 80, or prevent the use of HTTPS by block port 443. It could also theoretically restrict WhatsApp messages, or Apple Messages, just about anything with a well-known or registered port number. This involves more processing power, since the router would have to process the IP layer first to get to the TCP layer.

## Hostname filtering

At higher levels of filtering (involving yet more processing power), the router might even block certain hostnames. Remember that the public IP address of the server is needed before a request can be sent, and this IP address is obtained through a DNS query ([Issue 29]({filename}/season3/issue029/issue029.md))). If a firewall intercepts and processes the DNS query and blocks the DNS query to resolve that hostname, the device never obtains the public IP address of the server and won’t be able to send the request.

## Advanced filtering

Advanced routers might also come with built-in patterns that detect different types of traffic, e.g. streaming video, videoconferencing, bittorrent, and more. Anything with a predictable pattern can be blocked by a firewall that the data packet passes through, some requiring more processing power than others.

**Issue summary:** Firewalls block data packets that match certain rules. They decrypt the data packet layer by layer, dropping those that match its programmed rules without allowing them to be forwarded to the next point in its journey. The type of filtering that can be applied depends on the processing power available to the router, since some information is hidden more deeply in the data packet than others. Such filtering is typically circumvented by the use of VPNs, or other means of encrypting the data that is required.

-----

Short issue, entirely by design. Firewall blocking and circumvention methods are an arms race between two sides, one side building better software and hardware that detects packets more quickly and accurately (requiring massive computational power), and the other side seeking ways to hide such metadata or enable it to get to its destination via other paths, often with the use of encryption (also requiring computational power). The details of how each method works can fill tomes. So I’ve decided to just introduce the basic idea, which is really quite simple: detect and block.

Today, most basic routers have ways to block data packets using hardware (MAC) address, IP address and port number information. Hostname blocking may be enabled on more advanced (i.e. expensive) routers, or on custom router _firmware_ (I’ll unpack this many issues in the future). You can use this to block ads from certain providers, to restrict access to certain sites (whether to protect your kids or to improve your productivity, I won’t guess), or even to only allow known devices to use your network (in case your neighbour is really good at hacking wifi networks).

I mentioned VPNs a lot, and didn’t elaborate on that. That’s because I’ll be covering that in the next issue :)

## What I’ll be covering next

**Next issue:** VPNs: Virtual Private Networks

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n’s in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
