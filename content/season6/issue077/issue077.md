Title: Issue 77: Wearing clothes on the Internet
Date: 2020-06-20 08:00
Tags: 
Category: Season 6
Slug: lmg-s6-issue-77-wearing-clothes-on-the-internet
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Cookies with the same domain as the site are first-party cookies, while cookies with domains different from the site are third-party cookies. Cookies are used for all kinds of purposes, from remembering browsing sessions, to logging users in, to tracking their identity across websites. Blocking all third-party cookies indiscriminately can result in most if not all of these functions breaking. And yet, not blocking them at all means that you are being tracked across all your browsing sessions, likely without your explicit permission.

I apologise for the titillating title, though I believe it is apt. After all, your choice of clothing is not about ensuring not a single square centimetre of skin is seen, nor is it about covering the absolute bare minimum. It is not about everybody having to follow the exact same dress code. It is about giving you *choices* about how far along the spectrum you want to be, from totally uncovered at one end to totally covered at the other end. It is about giving you *options* in deciding where to cover and where not to cover.

But I’m getting ahead of myself. Cover yourself from what? From scripts that seek to see things they shouldn’t. And what are they trying to see? Your *information*.

## What a script sees

There are websites online (such as [privacy.net](https://privacy.net)) which can tell you what information is exposed by your browser (and other settings). They do so by, of course, actually extracting this information by any means possible. Go on, give it a try if you’re not paranoid.

If you are, I did it for you so you don’t have to. Heres what it can see, in decreasing order of control (I skip privacy hacks/cheats here because the list would be almost endless):

1. IP address  
   From your IP address, it is an IP lookup away from finding out your **ISP**, your approximate **location** (using geoIP services)
2. Browser (and probably OS), with version information  
   This lets scripts know if you are using a (possibly outdated) browser version. Since most browser vulnerabilities are published online (to help security researchers patch them), you should keep your browser updated to benefit from these security patches.  
   OS information can provide some demographic information (e.g. if you are an Apple user or Linux user), and also whether you are on a mobile browser or laptop browser. With many data points, a data aggregator can learn if you are on the move often (mostly on mobile browser) or generally static (about 50/50 between mobile and laptop).
3. Screen resolution ([Issue 44]({filename}/season4/issue044/issue044.md)))  
   This can provide enough info to put you in an income bracket; cheaper devices generally have lower resolution. A mid-range or high-end phone usually has a resolution of 1080×1920 or higher.
4. Autofill information  
   Any information you save in your browser, to be autofilled in forms, can be extracted by a script. It creates a hidden input field that the browser detects and autofills. The script can then send this information as an HTTP request back to the originating server.
5. Accounts you are logged in to.  
   A script can sniff other cookies on your browser session and match them against known cookies to do this. These cookies may also containing other info, such as your username, last accessed timestamp, last search term, etc.
6. Information that you have given permission to access  
   If you run browser plugins and third-party services on your accounts (e.g. Google Drive Addons), you may have granted additional permissions that give these services permission to access your contact list, location, microphone, camera, etc. Needless to say, they now have access to that information.

All this, before a script even lays a single cookie on you! Then there’s all the information it can get through the tracking pixels and cookie IDs on the webpage, when it looks up those IDs in its own database. And if it takes a step further and attempts to exploit some common vulnerabilities, it may also know:

7. Your browsing history  
   A script can know if URLs on a page have been visited before (this is why links you have visited before can appear in a different style; if you’re a millennial i.e. Gen-Xer, remember the blue links and purple links?). Scripts are also able to check if a link is visited or not. By applying this check on every URL it comes across, it is able to build up a browsing history of your device, albeit in a limited way.

Okay, I’ll stop scaring you here, although I am by no means done with all the things a script can do once it has been loaded by a webpage. But I hope I’ve made my point: you need to limit what scripts can see about you. In other words, *you need to wear clothes on the Internet*.

Let’s talk about some broadly useful strategies (note: this is a newsletter, not a howto guide. I won’t walk you through the steps here, just outline the strategies available):

## DNS blocking

A quick refresher on DNS ([Issue 28]({filename}/season3/issue028/issue028.md))): each time the browser is given a URL to load, it first figures out the IP address associated with the domain name of the URL (e.g. `facebook.com` is the domain name of a URL like `https://www.facebook.com/<username>/posts/17-digit-number`). It does this through a DNS lookup request to a DNS server.

Your default DNS server is usually your ISP. This allows your ISP to do some content filtering for you (e.g. if you signed up for a parental control service by them), by simply *blocking all requests* to a particular IP address or domain. e.g. if you have ISP parental controls enabled, and the ISP detects a DNS lookup request to resolve a blacklisted domain like `www.xxxchicksxxx.com` to its IP address, it will simply block the request by not returning any result—stopped at the source! (Note: that URL is probably fictional, I have not tested it!)

What if you don’t want to pay for that service? You could use other alternatives, such as [OpenDNS](https://www.opendns.com/). You will need to:

1. Register an account. You need an account for OpenDNS to remember your settings.
2. Change your DNS server IP address to OpenDNS’s servers: `208.67.222.222` and `208.67.220.220`  
   If you do this on your wireless router, anyone using that wifi connection will use the same DNS server—benefits for all!
3. Decide the level of filtering you want. You can customise the blocked domain names, or whitelist some that you need (the higher levels can be pretty aggressive and cause some services to stop working)
3. Register your IP address with your account, so OpenDNS can apply your setting to requests from your IP address. Since your ISP may change your IP address periodically, you may need to enable a DDNS service ([Issue 31]({filename}/season3/issue031/issue031.md))), again best done on your router. Some modern routers may have this built-in for you to configure.

## Script filtering with a browser addon

Some browser addons can help you detect script sources, and **block the script from loading** if the originating domain is blacklisted. The blacklist is full of tracking companies and data aggregators, and being updated by volunteers on a regular basis.

This currently works on laptop browsers only, as most mobile browsers do not support addons.

## Web-filtering mobile apps

Although mobile browsers do not support addons, some mobile apps are able to help you do this blocking. They do so by setting up an app-controlled VPN on your phone, routing all internet traffic through that VPN, and filtering blacklisted DNS lookup requests.

## Conclusion

The options are not many, and they often don’t leave you with much configuration options. Adding a domain to a blacklist/whitelist is tedious, and most users end up not enabling it at all.

**Issue summary:** The default settings of most browsers expose a lot of information to scripts that request it. To prevent such scripts from running, we need services that can filter **the source** of these scripts. These services generally work by matching browser requests against a blacklist, and blocking the request if it comes from a domain known to host malicious scripts.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 78: uMatrix: voyuering the voyeurs

In my virtual travels, I have found an addon that actually makes it easy for you to see what domains the scripts on a page are coming from. It even makes it easy for you to decide if you want to block them in future. It is by no means easy to use, as it requires some background knowledge of what the different kinds of requests are and what they do, but it makes it really easy to experiment and learn about privacy at the same time!

I’ll reserve the last issue fo this season to show you some screenshots from it :)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
