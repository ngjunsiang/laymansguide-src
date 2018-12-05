An HTTP request header looks like this:

<span align="center">
![An HTTP request header](https://github.com/ngjunsiang/laymansguide/blob/master/issue009/issue009_01.png?raw=true)
A request header
</span>

Really simple. In Issue 6, I said that to use an API we need to send a request using HTTP methods such as GET, POST, DELETE. You can see the GET method in use here. It’s literally just a word in the request header! Followed by the URL which we are requesting, in his case I’m searching for annotations made by me on Hypothes.is.

The rest of the first line in the request header is my request URL. The full URL I am using is actually [`https://hypothes.is/api/search?user=kureshii`](https://hypothes.is/api/search?user=kureshii). Notice that the request header URL does not have the front bit. This request header is already being crafted according to HTTP (which is a protocol, a set of rules) so we don‘t need the https part. “hypothes.is” is known as the host because it is the server hosting the API.

This means that when I enter the full URL in the address bar, my client takes the full URL, notes that I want to use the HTTPS method (future issue!) to request the data from hypothes.is, and then sends the request (which is actually the `api/search?user=kureshii` bit). The full URL is not just one long string, but multiple bits containing information for the client and server.

The third line, `Accept */*`, is the client’s way of saying “I understand anything you tell me, just go ahead”.

The last line is the interesting one.

## How do I make an HTTP request?

As humans, we can’t speak computerese. If I asked the server for information, it would not understand what I said. I need software to help me translate my request in a way the server can understand. This software acts as an *agent* for me, the *user*. So any software that helps to form an HTTP request, send it to a server, and receive the response, is known as a **User Agent**. The user agent needs to identify itself in the HTTP header (because the HTTP, a set of rules for transferring webpages, says so).

## What is my User-Agent?

You can find out your user-agent on websites like [whatismybrowser.com](https://www.whatismybrowser.com/detect/what-is-my-user-agent). Go ahead, it’s safe.

It is 2018, and there are all kinds of user agents out there. Some are highly advanced—think about your laptop web browser. Some are really simple and barebones and can’t handle very much—think of the web browser on your Kindle Paperwhite. A server can actually serve different user agents differently, but first it must be able to identify them. The user agent string, the fourth line in the request header, is how it identifies the user agent and delivers a response, hopefully an appropriate one with `200` in the header.

Ever wondered how some websites or services seem to know what kind of web browser you are using, perhaps even what operating system you are using? If you have ever needed to install drivers or software, some websites figure out whether to give you the Linux version or the Windows version or the Mac version, and they do so through your user agent string.

Yep, that means that on less scrupulous websites, the server can actually know something about you from your user agent declaration. It can, for example, know that you are using an iPhone and hence serve you more relevant ads. In the past, when the old version of Internet Explorer failed to render some pages correctly, some websites took to blocking it from visiting their site entirely, or serving a different, simpler site. They did so by detecting the user agent.

Why does my user agent in the request look so weird? That’s because I’m using an API tester, [apitester.com](https://apitester.com/), to check if I am using Hypothes.is’s API correctly (by looking at the response status code, introduced in Issue 8). I need to do that because I am accessing some information that requires the API to know who I am, and the only way for the Hypothes.is server to know that is for me to provide the information in the header. I can’t do that easily with a regular web browser, so I need specialised software tools.

And that will bring us to authentication and HTTPS.

<hr/>

Issue summary: A user agent communicates with the server on your behalf. It takes your request (a URL), breaks it down into parts (the protocol, the host, and the request string), puts this information and its user agent declaration into the header, and sends the request for you. To take greater control over what gets sent in the request header, you need specialised software tools.

## What I’ll be covering next

**Next few issues:** What’s the difference between HTTP and HTTPS? How do websites actually know if you are really you and not someone pretending to be you?

**Sometime in the future:** What is:
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8] 
