**Previously:** When a webpage document loads (Stage 1), it is processed by the web browser, which then
loads other requested resources, such as stylesheets, images, and scripts (Stage 2). Scripts and other interactive code may then request more resources (data fetches, images, icons, data, etc) which are then loaded subsequently (Stage 3, 4, 5, …).

Last issue, I showed you using Developer Tools how a webpage is loaded in stages, and how that contributes to latency alongside DNS querying and data routing. We saw that it could add up to a few seconds of latency, which would be unbearable for a lot of people (first-world problems!).

Searching for anything takes time. Need to fill out a form? You need to search for a pen first. Need to call someone? Before speed dial and contacts apps existed, You used to need to look up a number in order to dial it. If you do it often enough, you would make sure you always had a pen with you, or you would write the number somewhere convenient for you to see so you don’t need to hunt for it.

Computers use the same trick, and it is called **caching**. Any information it needs repeatedly which is unchanging is stored in a **cache**. What kind of caches does a computer use to reduce network latency?

## DNS cache

When you load a webpage or service and send requests to it, the first thing that happens is the DNS query. Once your OS knows the IP address to send requests to, it doesn’t make sense for it to keep querying the hostname, does it? IP addresses don’t change that quickly! The computer stores the hostnames and associated IP addresses in the DNS cache. You can view the DNS cache on a Windows PC by opening Command Prompt and typing `ipconfig /displaydns`.

<span style="text-align:center">
![The DNS cache](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue039/issue039_01.jpg?raw=true)<br />
The output of `ipconfig /displaydns`
(I used Powershell instead of Command Prompt,
but it will look the same in Command Prompt.)
</span>

The computer always goes to the DNS cache first. If it can’t find the hostname (e.g. facebook.com) in the DNS cache, it will perform a lookup, then store the hostname and associated IP address in DNS cache. This information is stored for a day, then discarded, just in case the information has been refreshed.

Sometimes, this causes problems. A company or service may be in the process of moving servers and thus changing IP addresses. If the move didn’t go smoothly, your computer may be stuck with the wrong DNS information for some hosts. Or sometimes something just goes wrong with the DNS query and you are stuck with bad information.

When this happens, tech support will usually just flush the DNS cache to remove all information from it (yes, the bad with the good). On Windows, you can do so by opening Command Prompt and typing `ipconfig /flushdns`.

## Browser cache

Notice that the first time your web browser loads any page you haven’t visited before, it often takes quite a while, but subsequent loads are really fast? That’s because we now skip a DNS query (grabbing the IP address from the DNS cache instead). Each time we do a lookup to retrieve a file or piece of information from the server, we can skip the DNS query!

The caching trick isn’t applied only to the IP address; many elements you see on the page have been cached: the document itself, images, scripts, stylesheets, … most of the elements from [Issue 38](https://buttondown.email/laymansguide/archive/lmg-s3-issue-38-loading-a-web-page/) are cacheable, and the browser will cache it.

How long does the browser cache these files? It depends ... I know it’s not an answer you like since it means more things to learn about, but I’ll keep it short.

Remember this? It’s the response header we saw from [Issue 8](https://buttondown.email/laymansguide/archive/lmg-issue-8-http-error-codeshow-does-a-server-let/) on HTTP error codes:

<span style="text-align:center">
![HTTP response header](https://github.com/ngjunsiang/laymansguide/blob/master/season1/issue008/issue008_01.png?raw=true)
A response header from Hypothes.is
</span>

See the line that says `Cache-Control: no-cache`? That is the server, hypothes.is, asking my browser not to cache this response (because the next time it makes the same API request, the response might be different).

The server can also set a different `Cache-Control` time, especially for resources that are used repeatedly on pages (such as logos and headers). On heavily accessed sites, these resources may have a `Cache-Control` time of up to a year!

If you want to bypass the cached version of the page and force a full reload, you can do so on most browsers using the hotkey `Ctrl-F5` instead of `F5`.

## Flushing the browser cache

The browser typically stores cached files and data until it exceeds the storage limit set in the browser, at which point it will begin ejecting the oldest files. You can force the browser to remove these files through a menu setting usually named something like “Clear browsing data” or just “Clear data”.

On some sites, especially internet banking sites, you may be asked to flush your cache after you log out; they are asking you to clear cached files and cookies stored in the browser, especially if you are on a public computer or some device that is not your own. the hotkey for doing so (if you are on a laptop) is usually `Ctrl-Shift-Del`.

**Issue summary:** Your computer and browser speed up a lot of lookups by caching information that is unlikely to change from the last view. When the same information is requested, your computer or browser will first look in the cache to find that information, and retrieve it from cache if it is there, otherwise it will load the information (and store it in cache if allowed to). There are usually ways to bypass a cache if the information is stale or no longer correct.

<hr/>

And Season 3’s a wrap! I know I may have mentioned that I don’t intend to write howtos in this newsletter, but clearing the cache is something I google for so often, and I see many others googling for it too, that I figured it might help to include a bit of info for those who want to know. At worst, many more people now know how to force-reload a page … 😅

## What I’ll be covering next

**Next season:** I’ve talked so much about networks: how they work and what they do, and then used that to build up to an explanation for “why is the internet so slow?”. It’s not a complete explanation yet—that will still take awhile—but I think we’re off to a good start.

As I wrote Season 3, it gradually became clear to me that before I start writing about cloud computing, I’m going to need to talk about data first. Computers ultimately store everything in binary, like `010101011100101000100101`, so how do they use something so basic to represent everything from text to images to audio to videos and more? and how do they set up a system for storing and retrieving this information easily?

I’m not going to talk about binary and hex numbers much if at all; I don’t think it’s relevant for a newsletter like this. But since so many things are measured in bits and bytes, it’s impossible to escape that discussion. I want to build the issues up to answer questions I’ve been getting, like “why do my JPG files have this weird fuzz”, and “why are my audio files so large”, and “can I make this zip file smaller by putting it in another zip file”, and “why do I get these weird rectangles or question marks in my web browser”, and many more :)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- ~~a cache? [Issue 8]~~
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n’s in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML [Issue 38]
