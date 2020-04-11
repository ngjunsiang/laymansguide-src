[**Previously:**](https://buttondown.email/laymansguide/archive/) The old CPM model (cost per thousand impressions) in the early Internet was replaced by the CPC model (cost per click) after the dot-com bust. But CPC only works well if publishers and advertisers could get users to click; they need to target advertisements accurately to users. QuantCast figured out a way to do so in 2006.

How to do that? The key, it turns out, centres around cookies.

## Wait, what’s a cookie?

When you visit any website in Chrome or Firefox, if you click on the icon to the left of the address bar:

![Screenshot of website info popup in Vivaldi browser](https://github.com/ngjunsiang/laymansguide/blob/master/season6/issue069/issue069_01.png?raw=true)<br />
<small>Clicking the icon to the left of the address bar shows basic site information</small>

It shows you some basic information, including the cookies loaded by the website.

![Screenshot of cookies in use popup in Vivaldi browser](https://github.com/ngjunsiang/laymansguide/blob/master/season6/issue069/issue069_02.png?raw=true)<br />
<small>You can view the content of cookies through that window in Chrome or Vivaldi. This information is also available in other web browsers through a different menu option.</small>

The cookies themselves are only just little fragments of information. They are identified with a name, they have a bunch of content (usually gibberish to humans), and they are associated with a website. Above, you can see that this website has a cookie named `_gid` with a value of `GA1.2.1807773255.1584140066`.

![Screenshot of website source in Vivaldi browser. The script line that loads analytics.js is highlighted](https://github.com/ngjunsiang/laymansguide/blob/master/season6/issue069/issue069_03.png?raw=true)<br />
<small>The script code used by Google Analytics is named `analytics.js`.</small>

Little snippets of javascript create and delete cookies. These snippets of Javascript are usually loaded as a script, with a `.js` file extension. The script code used by Google Analytics is named `analytics.js`.</small>

## What do cookies do?

This cookie was loaded by  [analytics.js](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookies-user-id) after the web browser runs the script. It is how Google Analytics identifies users on the website. the value stored in the `_gid` cookie is the client ID assigned by Google Analytics to identify a unique user.

Many bloggers and website owners rely on Google Analytics to tell them how much internet traffic their website is getting every month, which countries they are from, what time of day they are most active, which search results and bringing these visitors to the site, and so on.

But each visit represents one browser loading the page; how do we know that’s not the same user repeatedly refreshing the page waiting for something to happen? (It happens on auction sites, or game sites, and many other places).

Whenever the webpage is loaded, the cookie information gets sent to the Google Analytics server. That is how Google Analytics know it’s the same fella on the same browser doing it. The cookie associates each client [Issue 7](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/) with a `_gid` id. But if the user is using two different web browsers, or using a smartphone browser and doing it on their laptop, that actually gets classified under two different identifiers, even though it’s the same person!

# Plain cookies are not enough

Before 2006, this wasn’t a big issue. Users mostly browsed the internet on their desktops and browsers, and they seldom used more than one as their regular device. The famous Intel Core series processors had not even arrived yet—they would come a year later, in July 2007—and the first iPhone would arrive a month before Intel Core.

That meant the average user was using a Pentium-based computer to browse the internet, and that was probably their only internet-enabled device. At most, they had a desktop at home and a laptop at work. If you got a website visit with a user’s cookie, you know it’s not coming from a smartphone or their Amazon Alexa or any other smart device—those did not exist yet. One or two cookie identifiers was enough.

In a year, this would change.

**Issue summary:** Cookies are little fragments of information with a name and a value, and associated with a domain address. They are most commonly used to identify new or returning users. This cookie is issued by a website upon the first visit, stored in the browser, and returned to the issuing server whenever the server requests it.

Time to dispel some myths: cookies don’t actually contain any information about you. At least, in the context of advertising, what gives you away is not the cookie information. Think of cookies as queue numbers or collection slips that you get when you go shopping. They are impersonal identifiers simply used to ensure that a product gets delivered to the person who actually paid for it.

So what’s actually leaking your information, and helping Facebook know what you bought on Amazon? We’ll get there, patience please. The pieces are not yet in place.

Earlier in this issue, I said

> Whenever the webpage is loaded, the cookie information gets sent to the Google Analytics server.

How does this actually happen? In [Issue 38](https://buttondown.email/laymansguide/archive/lmg-s3-issue-38-loading-a-web-page/), I showed you a graphic from Chrome’s Developer Tools that represented the loading sequence a webpage goes through. With that same feature, we can find out when and how the Google Analytics cookie gets returned to the server.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 70: The Cookie Factory

We’ve seen how cookies are served, next issue we’ll get a bit closer. We’ll see how information from the cookie is returned. And then in the subsequent issue, you’ll understand Quantcast’s genius insight, and how it led to the ad landscape we have today.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- ~~a cookie? [Issue 8]~~
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
