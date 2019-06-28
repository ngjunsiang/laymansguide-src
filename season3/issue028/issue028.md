Last issue, I introduced IP addresses: a string of four numbers that tells routers where to send the data packet. These IP addresses are managed by the Internet Assigned Numbers Authority (IANA), and Internet registries everywhere agree to configure their routers to abide by this agreement. Without this coordination, our data won’t be able to make it across the Internet so easily.

## Domain names

When was the last time you remembered entering an IP address into the address bar in your browser? (If you’re a tinkerer, maybe the last time you tried to configure your router through a web browser.) Almost all the time, we enter web addresses that use **domain names**, not IP addresses. Here are some domain names you probably know: www.facebook.com, www.google.com, www.instagram.com.

The `https` part in front of addresses like https://www.facebook.com is not part of the domain name; it is the protocol: a web browser would use that to determine which set of rules to use in processing the data received. I first introduced the idea of a protocol in [Issue 7](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/).

Here’s something that might be new to some of you: www.facebook.com is still not the domain name. facebook.com is the domain name. That’s how it was conceptualised in the 1980s, where people already realised that memorising names is much easier than memorising IP addresses. The original specifications for the Domain Name System were published in 1983, making this system less than 40 years old.

The right to use a domain name is governed by **domain name registrars** (basically any service you see selling and managing domain names), which have to be accredited by the Internet Corporation for Assigned Names and Numbers (ICANN).

## Subdomains

Some domains are a huge place. Just look at the number of services Google offers. Each of these services might be residing on a different server, under a different IP address. It would be mightily inconvenient if each domain name could only be mapped to a single IP address: we would have to use multiple domain names to access them, perhaps gmail.com, googledrive.com, googleslides.com, and so on.

**Subdomains** are a way for a router to consolidate multiple locations under a single domain name. A data packet with the address www.google.com would be routed to the www server, drive.google.com would be routed to the drive server, mail.google.com would be routed to the mail server … and Google can strengthen its identity under this single domain name, and save on registering additional domain names.

Subdomains make it easier for a business or organisation to organise their web presence and identity. Once you have registered myorganisation.com as your domain name, you can configure your hosting server (the server that holds your webpages and files) with multiple subdomains (up to 100 per domain).

## … and Top-level domains

What about international organisations? Some of them may have different branch offices, with webpages hosted on different servers with different IP addresses. Subdomains are a clunky way to deal with this: what if each office needed those subdomains to further divide sections of their website?

The Domain Name System originally specified two main groups of **top-level domains** (TLD):

1. The country code top-level domain, based on two-character territory codes. Example: `.sg`, `.my`, `.us`, `.ru`
2. The seven generic top-level domains – `.gov`, `.edu`, `.com`, `.mil`, `.org`, `.net`, `.int`

A web address *must* have a generic top-level domain describing its category, and optionally may also have a country code top-level domain to signify its associated territory. This helps people to identify the category/purpose and origin of the website.

Each top-level domain is managed by an administrative registry which takes care of the database of names under that TLD. Registration requests from the domain name registrars (mentioned above under domain names) are forwarded to the respective registries. This enables some TLDs to be protected. For instance, .edu domains may only be registered by accredited organisations on a the U.S. Department of Education’s list ([Wikipedia link](https://en.wikipedia.org/wiki/.edu#Eligibility)).

## WHOIS

What do these organisations do with their huge list of domain names? They put them in databases, of course. If you want to find out who registered `mydomainname.net`, you would send a request to a WHOIS server (that is not an acronym, it just means “who is”!) and it would give you the registrant’s information. Here, [give it a try](https://whois.icann.org/en). Just key in any domain name you know. I’ll wait.

When you register a domain name with a domain name registrar, you are putting your name on the WHOIS database, so that people know who the domain belongs to when they query the WHOIS database. The domain name registrar lets you configure the domain name to associate it with your IP address. This information then propagates through the registrar’s Domain Name System (DNS) servers, so that within a day or two, data packets will start to arrive at your server.

How does that happen? That’s a story for the next issue.

**Issue summary:** Domain names consist of an optional subdomain, the domain name, and the top-level domain. The top-level domains are managed by a registry, which receives registration requests from domain name registrars, and maintains registrant information for each domain under their TLD in a WHOIS database. The domain name registrars let you configure which IP address to forward data packets to, and propagate that information through their DNS servers so that data packets will be routed accordingly.

<hr/>

This was wayyy longer than I thought it would be—there are a lot of things I needed to look up and confirm. That’s part of the reason I started this newsletter: to help me clarify what I know and ensure it’s not just “something I heard”. Domain names, something that looks so simple, has a really huge backend system maintaining its existence!

If you really try to imagine how all this happens, one thing starts to become clear: the backbone of the Internet is lists and lists and lists and lists … and the hardware that looks up these lists for you are really carrying a heavy load! There are numerous organisations responsible for ensuring that the Internet keeps on running. The day they are no longer sustainable, the Internet is going to be reconfigured into something a lot less interconnected.

I’m sorry if this issue was a little too heavy on the terms. I bolded the terms that I’m likely to use again, if it helps to focus your attention. I’ll reintroduce the terms again if I use them in future issues.

## What I’ll be covering next

**Next issue:** DNS lookup and resolving (how do I know which IP address to send this packet to?)

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
