Title: Issue 7: What is HTTP?
Date: 2019-01-26 08:00
Tags: 
Category: Season 1
Slug: issue007
Author: J S Ng
Summary: 
Modified: 

Before I jump into talking about requests, maybe we should start with a more fundamental question: what is HTTP?

HTTP: HyperText Transfer Protocol

Let’s break that term down:

### Protocol

A protocol is “a procedure or set of rules”. So HTTP is a set of rules. For doing what?

### Transfer Protocol

Okay, this tells us that HTTP is a set of rules for transferring something. Most likely referring to data, right? 

### HyperText

“[HyperText](https://en.wikipedia.org/wiki/Hypertext)” is a term coined by author Ted Nelson in 1963 to describe documents that can reference each other. Today, we know these references as “hyperlinks” or “URLs” (Uniform Resource Locators. Not important.) So hypertext is what we simply know today as “webpage”.

### HTTP = HyperText Transfer Protocol

So, putting all that together, HTTP is a set of rules for transferring webpage data from one computer to another. Not too difficult, was it?

-----

## Who sends and who receives?

Oh man, you got me there. Just kidding. Obviously, before the sending and receiving happens, someone has to request, and someone has to respond.

Usually, you’re the one requesting. Okay, you’re not actually requesting directly; your web browser (Safari, or Chrome, or Firefox, or Edge) does so on your behalf. So it (the browser) is known as the **client**. Your request is sent to the computer that has the data. The computer then *serves* you the data, so it (the computer with the data) is known as the **server**. When you read about people talking about *client-side blahblah* or *server-side blahblah*, they are talking about the requesting computer or the responding computer.

To add just a bit more jargon (you can take a little bit more, right? It’s not difficult, I promise): the data your browser sends to ask for a webpage is known as the **request**. And the data the server sends back to you is known as the **response**. There, I promised you it wasn’t so difficult.

Summary: The client (that’s you!) sends a request for data to the server. The server returns a response with data to the client.

-----

Huh, that sounds pretty nice on paper. But in real life, with humans, we know that’s not how it works. The client asks for something, the server says “nope, we’re all out of avocado toast”, the server sometimes forgets your order, sometimes the client forgets to request data and waits for the server to take their order which never happens …

All kidding aside, computers aren’t that complex, but obviously that’s not all there is to HTTP. There’s a client who sends a request, and a server who returns a response, and a million and one ways to miscommunicate. How does the server let the client know that what they’re asking for is out of stock or not on the menu?

-----

**Issue summary:** HTTP is a set of rules for sending and receiving webpages that link to other webpages. According to the rules, if you want a webpages, you (the client) must send a (HTTP) request to a server, which will return a response.

## What I’ll be covering next

**Next few issues:** How does a server let the client know if there’s something wrong with their HTTP request? What does an HTTP request look like? How do I make an HTTP request? What’s the difference between HTTP and HTTPS?

-----

The past two issues have been pretty dry and text-only. Definitely pictures to come in the next issue, I promise.

—JS
