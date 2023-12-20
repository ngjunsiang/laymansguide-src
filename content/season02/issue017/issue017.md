Title: Issue 17: Libraries
Date: 2019-04-06 08:00
Tags: 
Category: Season 02
Slug: issue017
Author: J S Ng
Summary: 
Modified: 2019-04-06 08:00

Welcome back! Last issue must have been exhausting to read, and I want this issue to be more readily digestible. So there’re only going to be two examples. Promise.

A shell script works really well when you just need to do things with folders, and run programs to work on files. But anything more advanced, such as [making network requests](https://buttondown.email/laymansguide/archive/a6941efd-86bf-4fd8-92c9-009fe14a8c2a), quickly gets tricky. Usually this is where the programmers start to whip out their favourite programming language. But …

## Low-level Sockets vs High-level Requests

In python, crafting an HTTP request from scratch looks like:

```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 
s.connect(("www.hypothes.is" , 80))
s.sendall("GET /api/annotations/GqDxiuhpEeiMa6f5UN7ttA HTTP/1.1\r\n\r\n")
print s.recv(4096)
s.close
```

5 lines of code every time I want to get an annotation from Hypothes.is? That’s going to add up fast … I could wrap that code up into a function, and then it would be easier to just call that function in one line instead of 5.

Carry that thought to its logical conclusion, and you get a library.

Creating an HTTP request with the [Requests library](http://docs.python-requests.org/en/master/) be like:

```
import requests

r = requests.get('https://www.hypothes.is/api/annotations/GqDxiuhpEeiMa6f5UN7ttA')
```

A good library makes complicated things simpler, so you can focus on what you need to do.

## There’s a library for it

Apple’s App Store slogan, “There’s an app for that”, is so famous that [they actually trademarked it](https://trademark.trademarkia.com/theres-an-app-for-that-77980556.html). So it is with programmers. For almost everything you want to do in the most commonly used programming languages, someone has created a library for it. If they haven’t, then it’s up to you to make one.

But sometimes, some projects are just way beyond your current level of knowledge. If you wanted to dabble in advanced machine learning(i.e. AI), one option is to go for a PhD … or tinker with [Google’s TensorFlow platform](https://www.tensorflow.org/).

How do you do that in Python? You need the [TensorFlow Python library](https://www.tensorflow.org/install). And then you probably [need some tutorials](https://www.tensorflow.org/tutorials) to get started.

If there isn’t a library available … you might as well get started on that PhD.

But TensorFlow only comes with a Python library. What if you don’t use Python, but use Ruby instead? Then your best hope is to petition Google for a Ruby library, or [hope someone else ports it for you](https://medium.com/@Arafat./introducing-tensorflow-ruby-api-e77a477ff16e).

Either way, it’s plain to see that without these advanced libraries, it would take much longer to get started.

**Issue summary:** Libraries make it easier to do the same thing in a programming language, or enable advanced functionality that wasn’t available previously. Libraries are usually specific to a particular programming language, and can’t be used in another programming language.

-----

Okay, so it turned out I only wrote one example, and linked extensively to another one. This didn’t need to be complicated, and aside from the code I hope I didn’t lose you. Was this issue too difficult to grasp, or am I moving too fast? Drop me an email, I can adjust :)

## What I’ll be covering next

**Next issue:** Frameworks

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those '\r\n's in the HTTP request packet [Issue 12,17]?

Yep, if you’re sharp-eyed you might have noticed the '\r\n's in the socket example ;) All in good time.
