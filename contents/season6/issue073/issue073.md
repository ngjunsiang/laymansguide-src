[**Previously:**](https://buttondown.email/laymansguide/archive/) QuantCast gathers a large amount of data on internet users directly through its **cookie** (which other publishers serve through their websites), and also by cross-checking it against data which it purchases from other **data brokers** who gather their information through other means, such as internet activity and credit card transactions.

What exactly does QuantCast do with all this data?

I’ll take a classic ad-infested website as an example: [HuffPost](https://www.huffpost.com/). HuffPost may not _look_ ad-infested, but peek under the hood and it will look different to those who know what to look for. If you just take a quick skim through the [website’s source code](view-source:https://www.huffpost.com/), you will see that almost a third of the website is just javascript loading!

Do a search for `<head>` and `</head>`, then for `<body>` and `</body>`.

## Webpage loading: header, followed by body

The section flanked by `<head></head>` is the page header. This is the most important section of the page for everyone else besides the reader. When a page is requested by the browser, the HTML code for the entire page is retrieved. But it is not rendered all at once.

The browser starts processing the page header first. It looks at all the file requests: CSS files (for styling the page), fonts (for formatting text), javascript code (for running code to make the page responsive and for loading cookies ([Issue 70](https://buttondown.email/laymansguide/archive/lmg-s6-issue-70-the-cookie-factory/)) etc). It sends off another round of requests for each of these resources. The rest of the page (flanked by the `<body></body>` tags) does not start rendering until critical files have been retrieved.

Often, the javascript code is considered critical, because some of them actually change the page body or affect what is loaded. They are therefore placed in the page header and loaded first before the body is rendered.

Normally, on a non-advertising page, the page header is very short: just the page title, some metadata (to tell Google’s bot what the page is about for ranking in searches), some fonts, some CSS, and a bit of javascript to spice up page interactions. That’s it. A fancy photo carousel or other features will involve a bit more code, but still not a whole lot.

## How ad bidding works

When advertising comes into the mix, the information flow gets much more complicated. The header loads an ad script that passes the cookie (embedded in the page), along with any other relevant information (type of website, device info, etc[^1]) to the advertising exchange.

[^1]: It’s hard to know what exactly is going on because the javascript is often obfuscated with all kinds of codes and renaming. Only folks in the industry will be able to tell you what exactly is going on in their backend, and even then they might not be able to tell you what exactly a competitor is doing.

What does an exchange do? It matches this cookie to its huge database of cookies, and then it conducts an auction. “Here’s a user browsing New York Times! \*Looks up user in database\* Probably a woke young twenty-something, good credit history, into yoga, and health-fad-ish.” So it’s pretty much like a marketplace, but one that you cannot participate directly in. It’s actually automated bidding.

The ad-buyers bid. These bids are not placed on-the-spot, but pre-bidded (through the advertisers’ dashboards, or [through an API](https://buttondown.email/laymansguide/archive/lmg-issue-4-what-is-an-api/)). Higher bids win over lower bids, but more relevant bids win over less relevant bids.

The advertiser’s server sends the winning bid code back to your browser. Then another piece of the advertiser’s javascript code kicks in, sending this code to the advertiser’s **content delivery network (CDN)**.

Yup, online ads need specialised servers to do different things. The **ad exchange** carries out the bidding and determines the winner (much like a stock exchange); this requires intensive CPU calculations and low latency connections. The **CDN**, on the other hand, is a global network of servers that keep the content ready to deliver. Servers in the US can get content to US web browsers most quickly, while servers in South-east Asia are better placed to serve Southeast Asian browsers.

These servers continually talk to each other or to a coordinating server, which determines what content should be on each server depending on the demand from each region. Each regional server caches the most frequently requested ads and cat images in the server memory (which is quick to access), leaving the rest in hard disk or solid state storage (which is slower to access).

These servers are configured for high bandwidth (to serve as many images as quickly as possible) and with large memory + storage space.

This is what that invisible one-third of the page is doing.

**Issue summary:** When a page loads advertisements through header bidding, it sends your cookie along with other information to an **ad exchange**. The ad exchange conducts automated bidding among the ad-buyers, determines the winner(s), and sends the winning code(s) back to your browser. Your browser then sends these codes to the **CDN**, which sends back the winning ads for your page to render in your browser.

Phew, that’s as short as I can describe ad exchanges and CDNs. (one more long-running question answered, yay!) You may or may not be surprised at what is going on at the backend, but often people don’t expect that so much of the internet backend is actually dedicated to just serving ads. But it’s true. The services you have come to rely on—this is the price we pay for them to be “free”.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 74: The Walls Have Pixels

It gets worse … after ad exchanges came about in the mid-2010s, second-order effects were responsible for much of the data leakage and privacy concerns that hog the headlines of some publications today. I’ll explore a couple of them in the next two issues.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- ~~a CDN? [Issue 8]~~
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
