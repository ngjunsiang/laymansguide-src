[**Previously:**](https://buttondown.email/laymansguide/archive/) Instead of GPS satellites, smartphones can also use wifi points and cell towers to determine their position (if enabled in the OS).

All businessmen know that distribution is everything. How good your product is, is secondary to how you get your product to the customer. This act of getting things to your customer—it’s called distribution, and entire businesses have been built around excellent distribution.

In [Issue 157](), I described how time is synchronised from time source to server and on to other servers, down the strata of the hierarchy tree of time servers. whereas GPS/wifi location ([Issue 158]()) has a much shallower distribution system: everybody gets their location directly from a GPS satellite if there’s nothing else available, otherwise they get it from the nearest wifi point or cell tower.

What about content?

## The difficulties of content

You make a website, type in the headers and body text, upload the images and videos … and it just works right?

Let’s think through the **distribution** of that content. Text is generally small in size and easy to pass around, even through multiple hops ([Issue 36](https://buttondown.email/laymansguide/archive/lmg-s3-issue-36-latency/)) from server to client.

### Server load

What about the heavy stuff, like hi-res images and videos? Thousands or millions of clients all requesting the same large video file from your hosting server. That server is going to be spending many CPU cycles ([Issue 58](https://buttondown.email/laymansguide/archive/lmg-s5-issue-58-cpu-optimisation-part-1-out-of/)) receiving requests, retrieving the data, splitting and encapsulating it into data packets to be sent out. All that processing adds to the server load. If there are too many clients waiting for the same data ... they gonna wait. And that adds to latency ([Issue 36](https://buttondown.email/laymansguide/archive/lmg-s3-issue-36-latency/)); those viewers are going to be seeing loading spinners for a while.

Some of that processing can be mitigated with techniques such as caching ([Issue 39](https://buttondown.email/laymansguide/archive/lmg-s3-issue-39-caches-and-caching/)), but not enough; you will eventually need to add more servers.

### Bandwidth and transfer fees

Your hosting provider is going to be paying lots of egress fees to transfer your data out of their servers (imagine sending the same 4GB video to a few thousand Youtube viewers), and they’ll likely pass on the fees to you as well.

### Latency again

If the client is geographically far away from the server, possibly even on the other side of the world, the data is going to go through a lot of hops from server to server. And if any of the servers along the way drop the packet, it is going to need to be resent.

## Improving content distribution

So how do we lighten the server load on the hosting company’s servers, reduce the amount of data to transfer from that server, and improve latency for the clients?

You place distribution servers as close as possible to the clients, wherever they may be. This usually means you have your servers globally distributed, with regional clusters.

You place the most often requested files from that region in its distribution server, so that it can serve those files without the request hitting the hosting server. Because the distribution server is so near the client, the data goes through fewer hops to get to the client.

The main document data is still served from the hosting provider, so that any changes you make to the page get served to clients almost immediately. Otherwise every little change you make has to be reflected in every distribution server that has a copy of that data. For this reason, distribution servers are typically used for **static data**: data that doesn’t change frequently, or at all—images and videos especially.

## A content distribution network (CDN)

These distribution servers, along with their supporting infrastructure, are collectively known as a **content distribution network** (CDN). Sometimes, when you are grabbing the URL of an image, you might see “cdn” in the URL domain—now you know what it means!

**Issue summary:** A content distribution system comprises multiple servers around the world that are able to quickly distribute static content (typically images and video) to viewers that request it. This avoids overloading the hosting server, which would otherwise have to serve data over the network, possibly through many intermediary hops.

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 161: Security and XSS

With this piece of info, our mental picture of the loading of a webpage is getting more and more complex. No longer can we assume that the web document itself, its images, videos, and other content are all being loaded from the same server: static content might be coming from a CDN, and other content (e.g. ads) might be loaded from elsewhere.

Let’s talk about this from a security standpoint next issue.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
