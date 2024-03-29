Title: Issue 8: HTTP error codes—How does a server let the client know if there’s something wrong with their HTTP request?
Date: 2019-02-02 08:00
Tags: 
Category: Season 01
Slug: issue008
Author: J S Ng
Summary: A request or a response consists of a header and a body. The response header contains information about the response. The status code in the response header determines if the request was successful or unsuccessful.
Modified: 2019-02-02 08:00

Last issue, I said that HTTP is a set of rules for sending and receiving documents that link to other documents. According to those rules, if you want a webpage, you (the client) must send a (HTTP) request to a server, which will return a response.

I almost forgot one of my rules here, that it is just as important to know *why* you should do something as to know how to do it. All I need right now is to craft an HTTP request to get my data from Hypothes.is. In fact, HTTP requests and responses form the backbone of everything we do on the internet. Knowing what I know about them, I want to go a little in depth (just one issue, I promise), so that later some of the things I say about internet security will make a little more sense.

Last thing before the dive: A request or response typically has two parts: a **header** and a **body**. Think of the body as a letter you receive; the header is the envelope that the letter came in. It tells you something about where or who this letter is from, whether it was returned or successfully delivered, maybe even a date stamp.

## What does an HTTP Response header look like?

We'll get to looking at what kind of data goes out in the HTTP request next issue. Right now, the HTTP response is simpler and easier to talk about. This is what an HTTP response from the Hypothes.is API ([Issue 4](https://buttondown.email/laymansguide/archive/fe8b59fc-c5fd-49f2-9d01-9f21fa3df95c)) looks like:


![An HTTP response header from Hypothes.is]({attach}/season01/issue008/issue008_01.png)  
*The response header from Hypothes.is*    


Whoa there, I thought this was supposed to be simple to talk about?? It really is! We’re not going to go through all of that, I just wanted to show you an HTTP response first.

The key parts of the response for us are all in the first three lines:

```
HTTP/1.1 200 OK
Date: Sat, 17 Nov 2018 04:01:02 GMT
Content-Type: application/json; charset=UTF-8
[...]
```

In the first line, `HTTP/1.1` tells us that this is version 1.1 of the HTTP specification (in use since 1990), and the response from the server is `200` which means OK (more on this below).

The second line is just the date and time that the response was sent. Nothing new.

The third line tells is what kind of data was sent with the HTTP response. We’ll have a look at the data after the response and request, but for now we can see that the data is sent in JSON format which I introduced in [Issue 5](https://buttondown.email/laymansguide/archive/fb0c4cc9-040a-4826-b1d0-0cf703c78115).

UTF-8 stands for “**Unicode** Transformation Format - 8 bit”, which means it is a format for transform letters and symbols into 1s and 0s. `charset=UTF-8` tells us that the *char*acters in the data come from this *set* of tables known as Unicode. The tables matter, because characters not in the table cannot be used. You sometimes see this in webpages as � or □. We’ll talk about Unicode when we get to emojis :)

-----

## HTTP status codes

Phew, that was some unpacking. Now let’s get to the core of this issue: from this response, how would my client (i.e. your web browser) know if there was something wrong with the request?

It is all in the first line: The `200` part is what we call a status code, since it is a number code that tells us the status of the request. Like error codes that you get from your electronic devices or appliances, there is [a whole list of error codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) defined by the HTTP/1.1 specification to tell you the exact status of your request. It looks long and scary, so here’s the gist.

Status codes are always three digits. The first digit tells you the category of status:

**1XX status codes** are technical, and you should never see them as they are supposed to be invisibly handled by your client (i.e. your web browser).

**2XX status codes** are good news: it means everything is okay! `HTTP 200` means OK (as you saw above) and is the usual response your client gets when browsing the internet. If you are using an API, you may also get status codes `201`, `202`, `203`, and `204`. We do not need to go into those today but they are generally good news.

**3XX status codes** are response headers that basically say “your princess is in another castle!” In general, they are usually redirects. If you have noticed your web browser going to a URL and then jumping to another one by itself, you’ve just experienced a redirect. These codes are usually handled invisibly by your client so you shouldn’t run into them often.

**4XX status codes** are bad news, and generally the server’s way of blaming the client.  
`400` means the server didn’t understand what you meant (I didn’t understand your English).  
`401` means you don’t have permission (this place is members only; do I know you?).  
`403` means you don’t have permission and may not ask for permission (These are not the droids you are looking for).  
`404`, the often-parodied status code, means what you are looking for at that URL didn’t exist.

**5XX status codes** are also bad news, but this time round the server is blaming itself.

`500` means “something is wrong with me; I can’t fulfill your request” (be right back; learning how to make avocado brioche!).  
`501` means “I don’t know how to do that yet” (but coming soon to a browser near you!).  
`502` means “I was trying to help you but when I asked Server C it gave me nonsense so now I can’t help” (please complain to your Member of Parliament on Facebook).  
`503` usually means “all our customer service officers are currently busy, please try again later.”  
`504` is the worst: you’ve waited until the request timed out and didn’t get a response. (the lights are on but nobody’s home …)


![An HTTP response header from Hypothes.is]({attach}/season01/issue008/issue008_02.png)  
*A 404 response header from Hypothes.is*    


-----

**Issue summary:** A request or a response consists of a header and a body. The response header contains information about the response. The status code in the response header determines if the request was successful or unsuccessful.

-----

### Bonus: What is a URI?

If you scrutinised the rest of the header, you’ll notice terms like “cookie”,  “cache”, “XSS Protection”, and acronyms in the URL such as “cdn” and “uri”. I will get to those other terms in a future issue, but let’s zap one of those now: A **URI** is a Uniform Resource Identifier. It is a string of text that helps to uniquely identify the thing that was tagged with the URI. The URLs (Uniform Resource Locators) we have all come to know and use are a special type of URI that uniquely identifies the page we are visiting.

## What I’ll be covering next

**Next few issues:** What does an HTTP request look like? How do I make an HTTP request? What’s the difference between HTTP and HTTPS?

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
