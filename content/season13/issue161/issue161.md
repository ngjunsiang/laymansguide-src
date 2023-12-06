Title: Issue 161: Security and XSS
Date: 2022-02-26 08:59
Tags: 
Category: Season 13
Slug: lmg-s13-issue-161-security-and-xss
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) A content delivery network comprises multiple servers around the world that are able to quickly distribute static content (typically images and video) to viewers that request it. This avoids overloading the hosting server, which would otherwise have to serve data over the network, possibly through many intermediary hops.

When you load a modern webpage with all its bells and whistles, it is usually loading its content from a content delivery network (CDN; see previous issue). At the same time, it is running scripts that came with the webpage. These scripts may load other scripts on the same server (first-party scripts), or scripts on other servers (third-party scripts).

What could go wrong?

## First-party scripts

These are scripts you trust, because you host them on your own server (or a server you administer). Ideally you also have network security measures in place and other ways to ensure those scripts are not modified by malicious actors.

It’s usually safe to load them in the webpage because they are from the same site (i.e. same server).

## Third-party scripts

These are scripts that are loaded from a remote server. You’d usually do this to load scripts from service providers: for analytics, to serve online ads, or to use libraries and frameworks ([Issue 17]({filename}/season2/issue017/issue017.md)), [Issue 18]({filename}/season2/issue018/issue018.md))). This is mightily convenient: as a third-party service provider, you have the flexibility of updating this script and immediately benefiting your client without them having to do anything. Can’t beat that for convenience!

But once you open the door to third-party scripts, they could be loaded from *anywhere*. And without some mechanism for verification, the client won’t actually know if they are loading your script, or someone else’s.

## Cross-site scripting (XSS)

If a webpage is insecurely scripted, e.g. by inserting data directly from a request without verification, a malicious actor might be able to subvert the source of the request and inject malicious code into the page. This malicious code, though sandboxed by the browser, still has access to data that is on the page.

This is called a **cross-site scripting** attack.

## The weakest link

The chain of security is only as strong as its weakest link, so even if your own security is tight, a malicious actor would look at your tech stack (the set of hardware/software/services your company uses), notice that your webpage is loading scripts from a third party, and attempt to hack the third-party's servers (which might be less secure). When you draw on features from multiple libraries, you are in effect setting up a circle of trust that is only as secure as the least secure library/third-party in your web.

## Protections

This is why all browsers today have [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) active by default. This prevents scripts from loading other third-party scripts; only loading of first-party scripts are supported by default. To enable loading of scripts from other sources, your server must include special data in the HTTP response header ([Issue 8]({filename}/season1/issue008/issue008.md))) that specify these sources explicitly. It’s tedious, but it is much more secure, and it is also why learning web programming is much harder today than it was a few years ago.

**Issue summary:** Cross-site scripting attacks occur when a webpage loads malicious code from a third-party, usually carried out by a script in the page. Today, websites are protected from loading unauthorised scripts through cross-origin resource sharing (CORS) policy implemented in browsers, which only allows a website to load scripts from authorised domains.

Ughh, this is already getting more tedious and bureaucratic to write about. As you can see, even in the world of programming there is a load of red-tape to cut through, all to protect our works from malicious actors and ensure there is a chain of authorisation running through everything. I guess there’s a life lesson in here somewhere.

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 162: Fonts

I’ve covered content distribution, code distribution (for the web), and now I think we can go a little wider: let’s talk about software distribution!

But before that I want to slot in a little issue about fonts: just what are they? And how do they work?

// Hopefully all my readers have had the experience of searching for and actually downloading software. What kind of system is behind this? And how do system and software updates actually get to our devices?

Get ready for a deeper dive!

**Sometime in the future:** What is:

- ~~XSS? [Issue 8]~~
- OpenType? And what are fonts anyway? [Issue 42]
