Title: Issue 30: Private IP Addresses
Date: 2019-07-20 08:00
Tags: 
Category: Season 03
Slug: issue030
Author: J S Ng
Summary: Private IP addresses are special IP addresses that routers will treat as belonging to devices within the private network, and not outside it. Data packets sent to private IP addresses will never make it past the gateway into the internet. This system allows multiple devices within a private network to share a public IP address.
Modified: 2019-07-20 08:00

Previously: Your web browser resolves a hostname (finds out which IP address a hostname points to) by sending a DNS query to its gateway.

Back in [Issue 27]({filename}/season03/issue027/issue027.md)), I said this:

> If you are good at math, you can work out the total number of available [IP address] combinations: it’s 4,294,967,296 (256^4). It seems like a lot, but we actually have more humans on this planet than we have IP addresses. And if we assign a unique IP address to each device on the Internet, many of us will need multiple IP addresses for our smartphone, laptop, Amazon Echo, smart TV, router, …

> IP addresses are a limited resource! They are really precious!

IP addresses are so precious that your ISP only has a handful, and they will only give you one per subscriber line. Which of your devices are going to receive it?

Fortunately, there is a way for all of them to share this one IP address.

## Private IP addresses

When you send a data packet through the internet, the data packet gets "stamped" with the destination IP address. The first router it reaches checks its internal forwarding tables (covered in Issue 27) to see if the IP address is there; if it is not, the router forwards it to the router’s gateway, and the process repeats.

Some IP addresses don’t get treated this way. Data packets sent to the following IP address ranges will **never** be forwarded past a gateway:
- 10.0.0.0 to 10.255.255.255
- 172.16.0.0 to 172.31.255.255
- 192.168.0.0 to 192.168.255.255

In effect, packets sent to these addresses will never make it out beyond your router, onto the (public) internet. These addresses are known as **private IP addresses**.

Not too long ago, you configured your router through a webpage. That means you need to enter an IP address into your browser to access the router settings, and there’s no way for you to know that IP address in advance. Most routers are configured to have a default gateway IP address of 192.168.1.1 or 192.168.0.1 (check your router’s manual for the correct one), so you set that as your gateway address in network settings. the private IP address system prevents commands you send to your router from making their way out to the Internet, and potentially leaking your information.

Imagine how many devices at home are sending data packets to 192.168.0.1 (or 192.168.1.1), to be forwarded to their destinations through the gateway … private IP addresses allow private networks to be separated from the internet. Every device in the private network has an IP address that only the router has a complete list of. You can't send a data packet to a private address (say, 192.168.1.3) on a different private network, since that data packet will never make it past the gateway. The router will simply attempt to send it to 192.68.1.3 within the same private network.

(A **router** is a _device_ that forwards data packets it receives; a **gateway** is a _destination point_ that a data packet gets sent to as it makes its way across the internet to its destination. I’ll try not to get too philosophical about the difference between them, but I’ll be using them interchangably depending on whether I’m emphasising the device or the network layout.)

## Handling the complexity: DHCP and NAT

It all sounds terribly simple when described this way. And then somebody at the back of the room raises their hand and asks, “so when we want to send a packet to IP address 45.63.153.22, should I send it to 45.63.153.22 (destination) or 192.168.0.1 (gateway)?”

No spoilers, we’ll cover this a couple issues later. The router juggles between the various IP addresses through a process called Network Address Traversal (NAT). NAT goes hand-in-hand with IP addresses to enable this IP-sharing magic. But first it has to have a public IP address …

How do our devices get an IP address from the router? How does our router get an IP address from the ISP? This usually occurs according to a set of rules known as Dynamic Host Configuration Protocol (DHCP)—yep, it’s another protocol.

## An analogy: home addresses and names

When someone sends a physical packet to you, they’ll write a home address _and_ a name (To: ). The mailman doesn’t care that much about the name; they just send the packet to the home address. Once it reaches your home, someone in the house (the early riser, or the stay-home one) looks at the name and figures out where the packet should go. If the packet is addressed to “Peter”, it’s natural to assume that it’s meant for Peter-in-this-house and not Peter-5-blocks-down-the-street.

This system allows multiple people to share one address. That address is like your ISP-given public IP address. The names are like private IP addresses; they are only meaningful within the house, and ambiguous outside of that context.

**Issue summary:** Private IP addresses are special IP addresses that routers will treat as belonging to devices within the private network, and not outside it. Data packets sent to private IP addresses will never make it past the gateway into the internet. This system allows multiple devices within a private network to share a public IP address.

-----

This was a little longer than I expected, but I’m pretty pleased with it. I hope you found the analogy helpful; it just popped to mind as I was nearing the end of the issue.

Private IP addresses were something I started learning when I started playing with my home router to try to optimise its performance (this was back in the slow days of 56k ADSL), and it took me weeks to understand all the different knobs and dials in the web interface. If you ever come across them, now you know what’s going on :)

## What I’ll be covering next

**Next issue:** How do my devices get an IP address? Dynamic IP addresses and DHCP

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
