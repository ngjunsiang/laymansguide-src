Title: Issue 14: What do developers do?
Date: 2019-03-16 08:00
Tags: 
Category: Season 2
Slug: issue014
Author: J S Ng
Summary: 
Modified: 

Last season, I used an app I was making to get into the differences between HTTP and HTTPS. It wrapped things up at a point I’m pretty happy with, left some questions unanswered (for now), and got me thinking what to cover next. I’ve thought about how best to cover the remaining topics, and I could well continue in the same thread, going on to say more (relevant and untechnical) things about networking and its technicalities, but from experience it gets dry and dreary very quickly.

One question I get pretty often is: “I’m interested in Computing, but where should I start? What should I do?” The first thing I tell them is not to learn programming, but to understand what developers do, because this is not obvious knowledge. So I’m going to try to build up your picture of computing first, before we get back to networking.

Season 2 is going to be about the work of developers: what they do, a bit of how they do it, and the cool things they get to play with. Yup, there are 13 issues worth of things to talk about!

Let’s start with the obvious: developers write code. They write code that runs all the services you use. The not-so-obvious part: not all code is the same. Just as the same letters can be used in different languages, the same keyboard can type code in different languages. The code serves different purposes.

Because code is so complex, and very very few people can really be proficient at every aspect of it, developers tend to specialise. And when they specialise, they label their specialties to make it easier for employers to understand what they do. I’d like to start us all off on the same page and get these terms out in this issue.

## A primer to applications

When you open an app on your phone or laptop, what you see is not all there is. It’s like a customer service desk: there’s the front desk, the back-office, the storeroom, and behind all of that is the sprawling mass of how the company delivers value to you, its customer.

Likewise, what you see when the app opens is only the **frontend**. You type data into the **interface**. The **application** processes some of that data, and sends some of it to the **backend**, where it is processed further, or used to look up information, which gets returned to the application.

## Frontend, backend, and application

The meat of frontend development is closely linked to user design. Frontend developers work closely with designers to understand how they are supposed to make the app look and behave. While default templates can make a webpage look slick and professional, it does not help an app differentiate itself. So frontend developers often code custom animations, button behaviour, and figure out ways to make an app do things out of the ordinary, among other things.

**Frontend developers write code in:** HTML, CSS, Javascript, PHP, ASP.net, and more

Backend development is hidden from the user, and so is primarily concerned with speed and stability. Many backend applications-server, database, custom software-run concurrently in the same system and must communicate to each other. Figuring out how to make everything work together harmoniously and bug-free is a full-time job, and the work of the backend developer.

**Backend developers write code in:** Java, C/C++, Ruby, Perl, Python, PHP, Javascript, Go, Rust, and more

Anytime there are two (or more) kinds of people, there is the potential for them to split into two tribes, each blaming the other for some way the system has gone wrong. This is where you need developers who are entrenched in both worlds, and are able to understand how the frontend and backend interact with each other to produce the final outcome. Developers that work in both frontend and backend in the course of their work are called **full-stack developers**.

A “stack” is a way of thinking about applications that work together; as you go from frontend deeper into the backend, you are going down the stack. Complex applications can have more than 20 different services running concurrently, and a full-stack developer needs the skills to diagnose what is happening when something goes wrong *somewhere* in the system.


![A stack consisting of user interface, user interface plus interaction, server communication, and server]({attach}/season2/issue014/issue014_01.png)
<small>A web development stack, just one of many. From [Eden Vital on Medium](https://medium.com/@edenvidal/the-rise-of-the-full-stack-designer-and-the-tools-he-uses-3daf015eb3fc).</small>


Frontend, backend, and full-stack describe which part of the code a developer is working on. But the kind of application a development team is working on can vary widely depending on where it is being used.

## Applications

**Web applications** are primarily run in a browser, even if that browser is embedded in a mobile app or installed device. These applications primarily interface with a web browser and the internet. They are device-agnostic, which means they can technically run in any device that is able to connect to the internet and run a browser.

**Laptop/desktop applications** are run in an operating system (Windows, MacOS, Linux). They are typically OS-specific, although with the right tools a developemnt team can develop versions for multiple operating systems without adding too much complexity to the code.

**Mobile applications** have a bit less leeway as compared to laptop applications, due to the sandboxed nature of smartphones and other mobile platforms. That means mobile apps have fewer privileges and do not have access to many parts of your smartphone (which is why they keep asking you for permissions).

**Embedded applications** run on low-power devices, typically routers, home gadgets, and other devices that require access to the internet. Because of their limited speed, embedded developers have to be skilled at optimisation and low-level coding (explained further down in this issue).

**Game engines** run on ... well, any of the first three really. A game engine helps game developers to not have to worry about rendering 3D graphics, setting up a quest system, and inventory system, character behaviour, scripted events, cutscenes, ...

**Enterprise applications** are applications which are developed primarily for use by large corporations. It may be adapted from consumer apps (e.g. GMail), or from scratch (e.g. SAP).

## Specialties

Beyond writing apps, code is also written for many other purposes. I outline some of them below, although people who write code for these purposes might not actually have “developer” in their job title.

**Data Science**
Yes, code can be written to process data! This is one of the coolest uses of software, because manually searching through data and performing calculations is tedious, and computers can do it so much faster.

**System administration**
A sysadmin’s job is to make sure a server, or group of servers, remain up and running. I might detail the kinds of trouble a server can get up to once I have enough stories to tell, but I think [Rachel tells much more interesting stories](https://rachelbythebay.com/w/) about those, albeit with lots of technical detail.

A sysadmin might have to write code to automate processes, to troubleshoot, to create new users, to manage files, and for many other reasons. They work primarily in the command line, because most system administration tools are written as commandline tools, although sometimes a user interface might be created to make a popular tool easier to use.

**Graphics**
Graphics engineers specialise in the art of rendering: turning data about a 3D object into an image. This work is very much mathematical, and needs to be performed quickly, because any lag in visual output is easily noticed.

**Machine Learning**
What is currently also referred to as “AI”. Machine learning researchers try to come up with ways to spot patterns in data, and use those patterns for various purposes, such as classifying data, generating realistic images, predicting behaviour, or just for fun, really.

**Cybersecurity**
A server is designed to give administrators and managers more privileges, and give users fewer privileges. Cybersecurity researchers figure out ways to make a server reveal more data than it should, to enable a user to do things they shouldn’t, or to downright gain access to a server they shouldn’t have access to. These are known as **exploits**. They publish information about these exploits, in the hope that the software developers responsible for those software will fix those bugs and keep people safe.

## Levels of programming

Some developers like to work “close to the metal”; they write **low-level code**. They often have a deep understanding of the hardware they are working on and the algorithms that are being used, and are able to write code that is lean and efficient. They may be able to speed up a function by a few thousand times by rewriting it in low-level code! But this is tedious work to maintain, and can’t be done for an entire software project, so such code is often employed in strategic areas only.

To manage low-level code, developers write compilers, interpreters, and debuggers that compile or interpret high-level instructions and break them down into lower-level instructions that get run instead. This makes it possible to write high-level code like `open('file.txt','r')` and be able to open a text file without having to know all the low-level code required to make it happen. **High-level code** is what most people learn when they learn programming, because it enables them to do cool things quickly without needing to understand all the intricate details; high-level code **abstracts** away the detail of low-level code and handle it for the developer.

Low-level code and high-level code are not a classification; they are a sliding scale. You can place different programming languages on this scale to indicate what level of abstraction they work at.


![Programming languages arranged from low-level to high-level]({attach}/season2/issue014/issue014_02.png)
<small>Some programming languages, arranged from low-level (left) to high-level (right). From [codecommit.com](http://www.codecommit.com/blog/java/defining-high-mid-and-low-level-languages)</small>


-----

Issue summary: Developers can specialise in frontend, backend, or full-stack development. They write applications for more purposes than I can really count. Not all code is written for an application; some code is written for specialised purposes. And code can be written at different levels of abstraction. High-level code is easier to understand and write because it hides the details of how a computer operates, while low-level code is detailed and able to squeeze the most performance from a computer, but difficult to understand and write.

Phew! This was a long issue, and I apologise for that. Subsequently I am not going to be covering such a broad scope, although the tools I talk about could potentially be used in any of the above areas.

In the next issue, I want to talk about a tool that laypeople almost never encounter: the command line. Because humans have a tendency to believe that what they see is what others see, I think it is important for people to understand that most of computing doesn’t happen with a graphical interface. And although laymansguide will not teach you how to program, it will hopefully help you to stop fearing the command line.

## What I’ll be covering next

**Next issue:** System administration and the command line.

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those ‘\r\n’s in the HTTP request packet [Issue 12]?
