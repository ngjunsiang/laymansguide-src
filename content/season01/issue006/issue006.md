Title: Issue 6: How do you use an API?
Date: 2019-01-19 08:00
Tags: 
Category: Season 01
Slug: issue006
Author: J S Ng
Summary: 
Modified: 2019-01-19 08:00

You ask it nicely, of course.

Sorry, I didn’t mean to be snarky. But that really is what you do. The question is, “what is a *nice* request?”

These days, the answer is “a request that follows REST principles”.

Nope, I’m not going to tell you what REST (REpresentational State Transfer) is. It is not something you must know to get around. But there are some things about it you *should* know:

1. It is simpler and easier to use than what came before it (SOAP).
2. It uses existing features of the internet as we know it, such as HTTP/HTTPS (okay, okay … I will get to this at some point), rather than trying to come up with yet more systems to build.
3. Because of (2), it uses familiar methods from HTTP to send/receive data, such as GET, POST, DELETE. These were originally proposed by Tim Berners-Lee in 1996 (with PUT and DELETE in 1999) in the HTTP specification (what’s that? Another issue on this sometime in the future …)
4. It uses error status codes (such as the all-too-familiar 404 error) to tell you if you succeeded or failed, and why. So you aren’t left guessing. Unlike some people you know.
5. These days, everyone uses it. Just like they do with JSON.

To receive data, you need to craft (and send) a GET request. To send data, you need to craft (and send) a PUT/POST/PATCH request. To remove data, you need to craft (and send) a DELETE request. Don’t know what these are? Don’t sweat it. We’ll get to them … sometime.

Issue summary: There are different kinds of HTTP requests-GET, PUT, DELETE, for example. To use an API, you need something that can craft an HTTP request.

## What I’ll be covering next

**Next few issues:** What is HTTP? What does an HTTP request look like? What’s the difference between HTTP and HTTPS? How do I make an HTTP request? And what are error codes?

**Sometime in the future:** What is a specification?

-----

Okay, I am really starting to lay on the terminology thick in this issue. I did that consciously because I thought the HTTP request types (GET, PUT, DELETE, but there are others) would be clear enough even for non-techies. REST and SOAP are there on the off-chance that someone might want to Google it. You are also going to see REST commonly enough elsewhere on the internet once you start googling about APIs, and at least now you know it means it is easy to ask it nicely for data. HTTP requests are what I'm going into next, and while it isn't critical understanding for everyday digital life, it gives background understanding for the meat of Season 1: why HTTPS is important and how it protects you.

Am I going too fast? Any suggestions for clarity or ease of reading? What do you like/dislike? I would love to hear your comments.
