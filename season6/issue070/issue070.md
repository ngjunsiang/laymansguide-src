[**Previously:**](https://buttondown.email/laymansguide/archive/) Cookies are little fragments of information with a name and a value, and associated with a domain address. They are most commonly used to identify new or returning users. This cookie is issued by a website upon the first visit, stored in the browser, and returned to the issuing server whenever the server requests it.

This issue is a short one, just to put one more piece in place. Last issue, I said that `analytics.js` loaded a `_gid` cookie with a value of `GA1.2.1807773255.1584140066`. At that point, the cookie only existed in my web browser. How did it get sent back to Google Analytics for counting?

Let’s watch what is happening with Google DevTools:

![Screenshot of DevTools in Vivaldi browser, with a request by analytics.js highlighted.](https://github.com/ngjunsiang/laymansguide/blob/release/season6/issue070/issue070_01.png?raw=true)<br />
<small>Chrome DevTools showing the (filtered) sequence of requests made by the webpage I loaded.<br />
The request made by `analytics.js` (third-last line) is highlighted in gray. The Initiator column tells us this requested was initiated by `analytics.js` on line 25 of the script.</small>

The full URL of the highlighted request is `http://www.google-analytics.com/collect?v=1&_v=j81&a=227860763&t=pageview&_s=1&dl=http%3A%2F%2Fwww.adopsinsider.com%2Fad-serving%2Fhow-does-ad-serving-work%2F&ul=en-us&de=UTF-8&dt=How%20Ad%20Serving%20Works&sd=24-bit&sr=3840x2160&vp=1319x1284&je=0&_u=QACAAAAB~&jid=&gjid=&cid=184706471.1584140066&tid=UA-13115681-1&_gid=1807773255.1584140066&gtm=2wg340NLT927&z=1600454420.`

That’s unreadable for humans!

In layman terms, `analytics.js` sends a request to http://www.google-analytics.com (yup, unsecured transmission since it does not use HTTPS) with the following information:

```
v: 1
_v: j81
a: 227860763
t: pageview
_s: 1
dl: http://www.adopsinsider.com/ad-serving/how-does-ad-serving-work/
ul: en-us
de: UTF-8
dt: How Ad Serving Works
sd: 24-bit
sr: 3840x2160
vp: 1319x1284
je: 0
_u: QACAAAAB~
jid:
gjid:
cid: 184706471.1584140066
tid: UA-13115681-1
_gid: 1807773255.1584140066
gtm: 2wg340NLT927
z: 1600454420
```

See anything interesting there? Here, let me highlight it for you:

`_gid: 1807773255.1584140066`

Yup, `analytics.js` sets a cookie if there isn’t one, or retrieves the existing cookie if there is one. It sends the cookie back to `google-analytics.com` with your cookie ID, so Google Analytics knows who is visiting the page and can count visitor stats for the webpage.

It makes sense for a webpage to embed `analytics.js` so that Google Analytics can help it count page visits. But why would a webpage allow Facebook and other ad services to put their cookies on a reader’s browser and then send it back to their own servers? Doesn’t that worsen the site experience? What is the benefit to them?

That is the key insight that Quantcast arrived at.

**Issue summary:** When browsing a webpage, a tracking script retrieves the browser's existing cookie, if there is one, or sets a cookie for the browser if there isn’t one. The tracking script sends the cookie information back to the originating server, along with many other fragments of information.

Short issue just to close the loop on cookie setting and returning. Enjoy the mental break! :)

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 71: The Rise of Audience Analytics

When it comes to ad networks, there is the How aspect, and the Why aspect. The How aspect is almost hopelessly complicated, an ever-evolving race of advertisers vs ad-blockers, each trying to outdo the other. I will focus less on this aspect, and more on the Why aspect. I think it is more critical to understanding what information advertisers actually extract, and why it does not make any sense for them to want to know your personal details.

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
