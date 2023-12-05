[**Previously:**](https://buttondown.email/laymansguide/archive/) DoubleClick, the first commercially successfully ad server, launched in 1996. It ran a system that tracked the performance of banner ads across 30 sites, working to optimise their return on investment. This was made possible by standardisation of the web (thanks to the HTTP specification), and the birth of Javascript, a scripting language integrated into the webpage rather than being a separate module from it. All of this happened in 1995–1996.

[The Internet Archive is a 501(c) non-profit](https://archive.org/about/) that aims to achieve nothing less than a digital library of the Internet and its artifacts. [The Wayback Machine](https://archive.org/web/) is your Google portal to the past. This is where you can type in any URL and see how it looked in the past (as long as The Wayback Machine has a saved copy of it from that time).

## Advertising in 1996

Back [in Oct 22, 1996, Yahoo! already had advertising](https://web.archive.org/web/19961022175643/http://www10.yahoo.com:80/) front and centre, right above its search bar. (Google had not even been founded yet.)

![Screenshot of Yahoo! from Oct 22, 1996]({attach}issue067_01.png)<br />
<small>Yahoo! in 1996 already had advertising right above the search bar</small>

The URL of that page was http://www10.yahoo.com:80/, and we can see a few things from that:

1. HTTP 1.0 had not been fully effected yet. When it was, port 80 would be standardised as the port for the Internet. Before that happened, though, you sometimes had to specify the port ([Issue 33]({filename}/season3/issue033/issue033.md
2. The Internet was small, but it was big enough for Yahoo! to need more than 1 server to serve its homepage. Yahoo had one domain name, yahoo.com, to route all internet traffic through, but it had to somehow direct this traffic to multiple servers. 1 such server was www.yahoo.com, the others were named www2.yahoo.com, www3.yahoo.com, ... you get the idea.
3. HTTPS was not yet a thing. Privacy was the last thing on peoples’ minds. Who cares what you were searching for? There wasn’t much on the Internet to implicate people with yet. You couldn’t book hotels or buy stuff online or send a tweet. The Internet was an interesting place, far removed from real life.

## What’s in an ad link?

The URL that the ad points to is http://www.yahoo.com/homet/SpaceID=0/AdID=2754/?http://la.yahoo.com. Why does yahoo.com appear twice? What’s going on?

That link is doing quite a number of things: it is sending an HTTP request to Yahoo’s servers with some information attached:

- **SpaceID = 0**  
  Website owners categorise ad slots into different “spaces”. The primary, busiest parts of the webpage might have ads categorised as SpaceID 0. Pages with less traffic might have ads categorised as SpaceID 1, and so on. This allows for some limited form of ad targeting, and different pricing tiers: SpaceID 0 would be more expensive, SpaceID 1 less so, and so on.
- **AdID = 2754**  
  In the table of customers, AdID 2754 would belong to the Yahoo! Los Angeles page.
- **http://la.yahoo.com**  
  This is the page that users should be redirected to.

Back in 1996, websites like Yahoo! could already track how many times an ad was clicked before redirecting users to the actual page. But it had no way of knowing anything about the user who clicked it. The only information it would have was the user’s IP address ([Issue 27]({filename}/season3/issue027/issue027.md

You might find it surprising that none of this requires Javascript; in fact, that page doesn’t have a single scrap of Javascript in it!

So what does Javascript do for ads?

**Issue summary:** Each click on a link, or even an ad, sends data to the server. This information can include an ID for the link you clicked, or the category of ad you clicked. But without Javascript, the webpage can’t know very much about you.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 68: The Age of Bloat

Still starting slow ... because the picture of online advertising is not complete yet

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
