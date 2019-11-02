Previously: An IP address is a string of four numbers that looks like 255.255.128.1. IP addresses are a list managed by the IANA, and all Internet registries agree to route data packets through their servers according to that list, so that you can send your data to anyone whose IP address you know. If you don't know their IP address, but you know their domain name, you can look up the domain name in a WHOIS database through a Domain Name Server to get their IP address.


![Resolving host message in a Chrome browser](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue029/issue029_01.png?raw=true)<br />
<small>A really old screenshot of Chrome, showing the resolving host message. [Source: Webnots](https://www.webnots.com/what-is-resolving-host-or-domain-name/)</small>


I think it’s basically impossible to be living in the age of the Internet and not have encountered one of those absolutely annoying times when your web browser just seems to be stuck on “resolving host …” for what seems like *forever*. What *is* it doing? And what does resolving host mean?!

Let’s address the second part first:

## What is a host?

In the early days of the internet, before blogging happened, if you wanted your own webpage you had to write the content and code yourself and put it up somewhere that people can access. the one place almost everybody in my generation knew could do this was Yahoo! GeoCities, a **web hosting service**. They are called hosting services because they act like a host to your content, serving them biscuits and water, making sure they know the wifi password to the place, and the way to the bathroom.

This is why the part of the domain name after the subdomain, i.e. facebook.com or google.com without the www in front, is also known as the **hostname**; on the internet, that is literally the name of the host(ing server) that holds your content.

## What does resolving mean?

[Merriam-Webster online:](https://www.merriam-webster.com/dictionary/resolve)
> **resolve** *verb*
>
> re·​solve | \ ri-ˈzälv
>
> 4 b : to find an answer to

To resolve a hostname is to seek an answer to the question “which IP address does this hostname point to?”

Your web browser, bless its poor soul, has to ask this question every time you type a URL into the address bar. It does not keep a list of domain names (and the addresses they map to), so someone else has to seek the answer for it.

This someone, or rather something, is a Domain Name Service.

## DNS: Domain Name Service


![Network connection properties window](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue029/issue029_02.png?raw=true)<br />
<small>Network connection properties, a window that one used to see very often when configuring a router. [Source: Help Desk Geek](https://helpdeskgeek.com/networking/change-ip-address-and-dns-servers-using-the-command-prompt/)</small>


In the days when you had to set up your router through a LAN cable connected to your internet-less laptop, this was a screen you would see regularly. You had to do this because you had to set your gateway address to point to the router’s default IP address in order to access its internal admin page.

But I talked about gateways back in ([Issue 27](https://buttondown.email/laymansguide/archive/lmg-s3-issue-27-what-is-an-ip-address/)), so we’re here to talk about DNS servers instead.

Just like other data request packets, the request to resolve a host (known as a **DNS query**) first goes to the gateway (usually your router). If it can’t be resolved there, it gets forwarded to the next gateway (your ISP), and it keeps getting forwarded until it reaches a server that is able to answer that query and return the long-desired IP Address (hey, a few seconds is already lifetime for an HTTP session!)

Usually, this request would be resolved by your ISP’s DNS servers. But sometimes the ISP gets a little swamped, or their DNS server decided to call in sick, or didn’t update its WHOIS databases properly and gave you a wrong answer, or … anyway, if you wanted to bypass that DNS server and try another one, you could input its IP address in the Preferred DNS Server field above.

Short question for you, dear reader: Why does the Preferred DNS Server field require an IP address and not a hostname?

Advice on the Internet these days suggests that if you find your browser is taking a little too long to resolve a hostname, you can try configuring your network interface to use [Google Public DNS](https://developers.google.com/speed/public-dns/) instead. Since this is a newsletter and not a helpdesk, I won’t go into the details here but you can always drop me a message if you need help.

**Issue summary:** Resolving a hostname means answering the question “which IP address does this hostname point to?”. Your web browser seeks this answer by sending a DNS query to the gateway. If the gateway is unable to provide a satisfactory answer, you can configure your network interface to send the DNS query to a different DNS server.

<hr/>

This a is a nice, sweet, and short issue, though it took almost as long to write as Issue 28. Crazy, I know.

I have more to say about DNS, but I don’t think it belongs in this issue. I’ll figure out where to slot that info, whenever it becomes more relevant :)

I hope a picture of how your browser gets its data is gradually forming in your head: registries looking up databases of addresses, requests getting forwarded to higher and higher gateways, and now hostnames resolving into IP addresses.

Yeah I really should have introduced hostnames last issue, but couldn't find a place to put them without making the issue more unwieldy than it needs to be. I think it made perfect sense here.

Did you answer the question above? It’s meant to make you think a little; that helps a lot for remembering what you read. You have to input the DNS Server as an IP address because if you used a hostname, your laptop would have to resolve that hostname *before* knowing where to send the DNS query. For this reason, Google Public DNS makes its DNS Server IP addresses easy to remember: 8.8.8.8 and 8.8.4.4.

## What I’ll be covering next

**Next issue:** Private IP addresses – how do I use one IP address for all my devices?

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
