[**Previously:**](https://buttondown.email/laymansguide/archive/) When a page loads advertisements through header bidding, it sends your cookie along with other information to an ad exchange. The ad exchange conducts automated bidding among the ad-buyers, determines the winner(s), and sends the winning code(s) back to your browser. Your browser then sends these codes to the **CDN**, which sends back the winning ads for your page to render in your browser.

So how does Facebook know what you just bought on Amazon? I hope the previous post sheds some light on that. But not everything is a web browser, and not everything uses cookies (especially apps). This post is about another way that your data gets shuttled along to whoever has a data-sharing agreement with the site you are on.

## Tracking pixels: another way of sending information

Even if you disable third-party tracking cookies and javascript that didn’t originate from the same page, information about where you went can still be sent to these servers. Can you guess how?

Obviously when you loaded the page, some information already went to the server to tell it what your browser wants. But beyond that, have you ever wondered about the images that get loaded?

Let’s revisit HuffPost again, this time filtering only for image loads:

![Screenshot of DevTools in Vivaldi browser, filtered to show only image loads.](https://github.com/ngjunsiang/laymansguide/blob/master/season6/issue074/issue074_01.png?raw=true)<br />
<small>Chrome DevTools showing filtered image requests.<br />
A request for a tracking pixel is highlighted in blue.</small>

Hmm … why does an image request need to be so long? Anytime you see a long URL like that, with a `?` after the URL proper, and peppered with `&`s and `=`s, alarm bells should be going off in your head: data is being sent to the server ([Issue 70](https://buttondown.email/laymansguide/archive/lmg-s6-issue-70-the-cookie-factory/))!

Let’s see what this image looks like:

![Vivaldi browser tab showing a tracking pixel.](https://github.com/ngjunsiang/laymansguide/blob/master/season6/issue074/issue074_02.png?raw=true)<br />
<small>This is a tracking pixel.<br />
You can’t see it. The image info sidebar shows that its dimensions are 1×1 pixels.</small>

Wha—?!

What is your browser doing, loading a useless 1×1 image? If it appears to be doing something useless, you’re not looking in the right place. The image itself is clearly useless; its just a way to get your browser to send information to a server.

## Tracking pixels work hand in hand with cookies

This request for the tracking pixel was sent from a script. My cookie information was embedded in the request URL when it was sent. So a tracking pixel is another mechanism for sending cookies, besides sending a generic document request via the script like we saw in [Issue 70](https://buttondown.email/laymansguide/archive/lmg-s6-issue-70-the-cookie-factory/).

If you have a popular website, ad exchanges will ask to pay you to put their ads on your website. These ads are served after the user’s browser sends the user’s cookie to the ad exchange, which triggers an automated bidding process. The winning bid gets sent to the CDN (content delivery network), which serves the ads ([Issue 73](https://buttondown.email/laymansguide/archive/lmg-s6-issue-73-the-heart-of-darkness-header/)).

On the other hand, data companies don’t serve ads. They usually ask to put a tracking pixel on your website, which means they ask you to put in their script. This script will scrape whatever data it can about the page the user is on and related user activity, and embed it in the pixel request along with the user’s cookie.

When you visit Facebook, it looks up your cookie and sees if you have been visiting any websites recently, or left any shopping carts un-checked-out. Then it knows what ads to serve you :)

**Issue summary:** There are two ways your browser can send cookies back to the server:

1. By sending an HTTP *document* request (known as an **XHR**, short for XmlHTTPRequest) which usually returns a chunk of text data,
2. By sending an HTTP *image* request which usually returns a 1×1 pixel, known as a **tracking pixel**.

Data companies use the data they have gathered to determine what ads to serve you when you visit sites that load their cookie-setting scripts.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 75: The Costs of Data Leakage

Notice at this point that ad and data companies are still more concerned with **what you are doing**, not **who you are**. That’s right; they don’t gather names, credit card numbers, and the like; that is useless for serving ads!

I kind of did some time travel in the past few issues. One moment, it was 2006 and ad companies were still just serving static images with some request tags and QuantCast had just discovered the power of the cookie. The next moment, there are a gazillion ad companies and a billion ad exchanges all bidding to serve ads before your eyeballs. How did this happen so abruptly?

It didn’t. Not abruptly anyway, but quite rapidly. The costs of data leakage have already been paid, not by us but by the websites. They have been greatly diminished in the value chain, replaced by ad exchanges which have sopped up most of the profit of advertising like a sponge.

Next issue, I’ll describe how this happened.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
