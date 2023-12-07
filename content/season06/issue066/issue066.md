Title: Issue 66: Before the Cloud
Date: 2020-04-04 08:00
Tags: 
Category: Season 6
Slug: issue066
Author: J S Ng
Summary: 
Modified: 2020-04-04 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Shared memory helps to reduce the amount of memory needed by all the applications running on an operating system. It also allows applications to send data to each other, and to communicate.

Season 5 focused on the vulnerabilities that arise from optimising CPUs for speed. Speed means sharing; the more easily data is made available to the CPU without all kinds of permission checks, the more quickly the processing that take place.

This season, Season 6, I will finally go back to the topic that got me started writing Layman’s Guide to Computing in the first place: online data privacy. But this is a huge, complex topic, and I’ve spent two weeks so far trying to build a timeline of key events, identifying key moments, and chasing interesting connections down deep rabbit-holes. Where do I even start?

Part of the difficulty of getting started is trying to definitively find out when it all started. Today, when you dig into a website’s code, it is mostly a gobbledygook of interacting code, advertising tags, accessibility declarations, and more. A mere 25 years ago, early in 1995, websites were still only static content! How did it turn out like this?

Did it start, maybe, in 1993? When Tim O’Reilly, who had already founded what would later be O’Reilly Media, started the first online information project, Global Network Navigator. (Yahoo! would follow suit with Yahoo! Directory a year later, trying to create the world’s biggest index of websites. By hand.) The site had to be funded somehow, since online commerce had not been born yet—the web was still static content, remember? The enterprising O’Reilly, taking a page from the huge highway banner ads, sold the first clickable ad to a Silicon Valley law firm. After all, 5 months later, Hotwired, a commercial web magazine (which would later be renamed to just WIRED), started doing just that in large quantities.

That seems to be a reasonable starting point … except that was not the same as the online advertising we know today. People emailing each other image files and signing off advertising contracts on paper is not the same as online ad space being sold to the highest bidder within microseconds while your page loads.

## The birth of Javascript

No. I think it started in mid-1995, when Netscape hired Brendan Eich to create a scripting language for the web. They already had Java, a language which the web didn’t understand; it had to be compiled ([Issue 54]({filename}/season05/issue054/issue054.md))) to a Java application (which you might know as a java applet) and put into its own little box so it wouldn’t hurt the rest of the webpage. But they wanted a **scripting language**, which could be run directly in the browser without compilation, in real time, *as part of the page*. [In Eich’s words](https://www.infoworld.com/article/2653798/javascript-creator-ponders-past--future.html), “The idea was to make something that Web designers, people who may or may not have much programming training, could use to add a little bit of animation or a little bit of smarts to their Web forms and their Web pages.”

Mr Eich created a prototype for the language, Mocha, in 10 days, just in time to be included in Netscape Navigator 2.0 beta 3 when it was released in November that year. Its name had been changed to LiveScript. But in December, when his prototype language was announced to the world by Netscape Communications and Sun Microsystems, it would be known as Javascript.

The same year, Internet Explorer 2.0 was also released to the world. Work on it had also started early that year. Both Netscape Navigator and Internet Explorer were based on very similar codebases: both originated from NCSA’s Mosaic browser, which began development by Eric Bina and Marc Andreessen three years ago, at the end of 1992. (Andreessen would later be best known as co-founder of Andreessen-Horowitz Capital Management.)

By Spring 1996, things were heating up. Before this point, web browsers were only working with [HTTP v0.9](https://www.w3.org/Protocols/HTTP/HTTP2.html), a protocol so simple I probably wouldn’t need to laymanise it for you. But a new standard was needed to support all the new things that Web 2.0 was supposed to be able to do. That new standard, HTTP v1.0, was published in 1996. (See [Issue 7]({filename}/season01/issue007/issue007.md)) if you’re still wondering what HTTP is.)

What else happened in that magical year of 1996?

- As if to signal a shift in the zeitgeist, Global Network Navigator was bought by AOL that year; by year-end they were shuttered, their subscribers moved to AOL. Static banner ads would go the way of the dinosaur.
- The Internet Advertising Bureau was founded to streamline industry standards and provide legal support—instead of stunting growth through regulation like today, this was meant to help growth by standardising things when most things were non-standard, such as the pixel dimensions of online ads.
- Adobe introduces Flash. It would have a good run for 15 years until Apple decided not to support it in their iOS devices, and it would see browser support removed entirely in 2020, just 25 years after its beginnings.
- While Google was the first to successfully monetise putting ads in your search, Yahoo! was the first to [put their search engine in an ad](https://www.youtube.com/watch?time_continue=17&v=Aa0WaSSVeIw&feature=emb_logo). They launched their IPO in April of 1996.

And one more thing. Slow as the internet seemed to be growing, people quickly ran into the limits of static banner ads. You couldn’t do very much on static websites. You couldn't track clicks, for instance, and you couldn’t quickly deploy different ads to different websites to see which ones did better. To do something like that, you had to work with different websites—talking to them over phone or email(!)—and work out performance metrics and tracking arrangements with them. In an era when it was hard to know precisely how much a TV ad, poster, or radio ad contributed to your campaign’s success, many companies were hoping to change things with an online presence through ads. It was unsurprisingly turning out to be harder than expected.

But right then in 1995, one company figured out how to do just that. Instead of serving their own ads, they decided to run their banner ad system, deployed across 30 sites, and sell ad space to other companies. By early 1996, they decided to launch their business. DoubleClick, an ad server, was born.

They would be acquired almost 10 years later by Google for US$3.1 billion.

**Issue summary:** DoubleClick, the first commercially successful ad server, launched in 1996. It ran a system that tracked the performance of banner ads across 30 sites, working to optimise their return on investment. This was made possible by standardisation of the web (thanks to the HTTP specification), and the birth of Javascript, a scripting language integrated into the webpage rather than being a separate module from it. All of this happened in 1995–1996.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 67: The Innocent Times

The more astute by this point could have imagined the portentous future that Javascript would herald. But this was still an age of innocence, still enchanted by the immense untapped potential of the desktop and still-new laptop.

Online advertising already existed even then. Visually, it would look familiar. But at the backend, ads today work very differently from how they did in 1996.

In the next issue, I will try to trace how online ads developed, as the industry changed and grew and shifted, to show you how they became what they were today.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
