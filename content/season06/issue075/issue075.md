Title: Issue 75: The Costs of Data Leakage
Date: 2020-06-06 08:00
Tags: 
Category: Season 06
Slug: issue075
Author: J S Ng
Summary: 
Modified: 2020-06-06 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Data companies use the data they have gathered to determine what ads to serve you when you visit sites that load their cookie-setting scripts. This data is sent from your browser via a document request, or via a tracking pixel request.

## Content adjacency

Ads used to be much more discriminate: You would publish only certain kinds of ads in Playboy magazine, another kind of ad in The New Yorker, and yet another kind in The New York Times. This, of course, is seldom dictated by the publishers themselves; mostly, the advertisers self-selected where they would like their ads to appear. IBM wouldn’t publish their ads in Playboy; they won’t reach their target group this way, and their ad spending would be wasted.

This idea was known as content adjacency: to reach your target group, you want to place your ads next to content that they would read. Content adjacency gave publishers a lot of power, since they were the gatekeepers to published ads.

But today, that power has mostly leaked away, to ad exchanges. The ads on HuffPost, NYT, and just about any newspaper look largely similar. These advertising slots are sold to ad exchanges, which decide (through the automated bidding) which ads to display to the viewer; no two viewers see the same set of ads. Content adjacency is irrelevant here. The power of ad filtering lies not with the publishers, but with the ad exchanges now.

## The danger of advertising: cookie leakage

In [Issue 71]({filename}/season06/issue071/issue071.md)), I mentioned that part of the value QuantCast brought to the table is that in exchange for letting them put a cookie on your site, they would also tell you more about your audience—far more than you could ever know collecting information on your own.

But here’s the thing: it is very hard for a website’s publisher to know when an advertiser is setting a cookie. When an advertiser is allowed to put advertisements on a website, you are tacitly allowing them to put in a script that is **supposed** to request an ad from the ad server (after getting a winning bid from the ad exchange). This script could easily, at the same time, set a cookie and return cookie data along with that request.

The only way to catch this is to load the page yourself, compare the site data before and after, and see if any cookies are being set. You could automate this, but you’ll need resources to run that regularly on every webpage you publish—resources that publishers were loathe to spend to protect their data and their readers.

## The danger of cookie leakage: audience leakage

Why would advertisers want to sneak cookies like this? Let me put it this way: nobody ever uses the Internet just for reading The NYT. NYT readers might head to Facebook to see how their friends are doing (and view Facebook ads), they might send out some angry tweets on Twitter (and see Twitter ads), they might head to Amazon or Barnes & Noble or any number of sites to do the necessaries.

And these readers can be reached on these other sites if the advertisers buy advertising slots with them. They no longer needed to rely on The NYT to reach a particular class of consumers. If The NYT thought they could price their advertising slots more expensively for the exclusive reach to upper-class readers, they now no longer have that advantage. Those readers are tied to a cookie ID now, not to a website URL.

The publishers were being cut out of the value chain.

**Issue summary:** By not enforcing strict cookie policies on their own sites, publishers allowed advertisers to sneakily set cookies on their site audience. This allowed advertisers to reach the same audience via their advertising slots on other websites, which could be bought more cheaply. The publishers were cut out of the value chain and were no longer “gatekeepers” to their own site readers. They could not sell their advertising slots at a premium.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 76: Third-parties and cross-site resources

One way that web browsers and privacy advocates are trying to protect users is by pushing for stricter third-party cookie restrictions. Firefox started blocking third-party cookies by default since Sep 2019, Safari started doing so in Apr 2020, and Chrome intends to do so from 2022.

Many sites are against this, arguing that it will break some “basic internet functionality”. What is this furore about? I’ll explain what third-party cookies and resources are in the next issue, and summarise some of the objections that sites are raising.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
