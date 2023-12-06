Title: Issue 72: The Data Brokers
Date: 2020-05-16 08:00
Tags: 
Category: Season 6
Slug: lmg-s6-issue-72-the-data-brokers
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) In 2006, Quantcast offered complete audience analytics for any site that puts _their_ cookie on the site. In this way, they managed to gather information on a wider audience than they, or any single website, could reach on their own.

I’m almost about to begin talking about Quantcast’s proposition to advertisers, and how that led to the ad exchange, and what an ad exchange is, but to avoid confusing you, I had better talk about data brokers and what they are first.

## The demand for data, and its players

There is a huge market out there for data. In a way reminiscent of the slave trade of the 16th to 19th centuries, in which people were being auctioned and sold and shipped to countries far from their homeland, data today is being sold in data markets, copied to places far from their point of origin, and used to put together profiles of consumers. Who are these data brokers?

Some are sources of information: subscription lists of email addresses to free journals and magazines, (anonymised) credit card activity (how much money spent where by what income bracket), your social media clicks and likes and other activity, your browsing web history, even your mobile device telemetry data (coming from a data-mining app disguised as a mobile game which you unwittingly downloaded). They sell this data to other third-parties, or to advertisers directly (rare).

Some are middlemen: third-party brokers who offer a consultancy-like service: they buy information, recompile it into profiles that are more legible to advertisers, and then resell this information.

Some are end-buyers: insurance and other risk-management companies, investigation firms, fraud detection services, … just about any company that may need information on a person or category of consumer.

[FastCo has a (non-exhaustive) A–W list](https://www.fastcompany.com/90310803/here-are-the-data-brokers-quietly-buying-and-selling-your-personal-information) of some of these companies, if you’d like a more detailed sampling.

QuantCast, in effect, was _acting_ like a data broker (though it didn’t buy or sell this information, it gathered them directly through its cookie).

# The data QuantCast gathers

The end result looks like what a soulless Santa Claus would have managed to gather on its own. A Privacy International journalist sent a Data Subject Access Request to QuantCast for the data it has gathered on her[^1]. By her own analysis, QuantCast has “amassed […] more than 46 columns worth of data including URLs, time stamps, IP addresses, cookies IDs, browser information and much more.” Furthermore, the data she received “suggest that [it was obtained through] data brokers like Acxiom and Oracle, but also MasterCard and credit referencing agencies like Experian.”

Interestingly enough, first name, last name, Social Security identification, and other personally identifying information is hardly collected. Such information is of little interest to advertisers; it is too specific and tells them nothing about whether an ad can be served at you, to extract another click.

[1]: QuantCast is legally obligated to fulfill [such requests](https://www.quantcast.com/privacy/data-subject-rights/) under the terms of the GDPR legislation which was implemented in 2018.

**Issue summary:** QuantCast gathers a large amount of data on internet users directly through its **cookie** (which other publishers serve through their websites), and also by cross-checking it against data which it purchases from other **data brokers** who gather their information through other means, such as internet activity and credit card transactions.

That’s … a lot of information, but how does it help advertisers? How does the engine of ad customisation work? All this and more in the next few issues.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 73: The Heart of Darkness (Header Bidding)

What we have come to know as “targeted advertisements” are known in the advertising industry by other terms, depending on the mode of operation: sponsored search auction, real-time bidding, etc. Generally, they are known as **header bidding**, because the code tag that triggers it is embedded in the header section of a webpage.

An entire cascade of bidding operations, reminiscent of eBay bidding but entirely automated, is completed in mere milliseconds; the smorgasbord of ads vying for your attention are shaken out, winners emerge, and are served into your browser view while you wait for the page to load.

Stay tuned next issue as we super-slo-mo this process to a speed you can grasp.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
