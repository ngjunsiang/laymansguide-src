Title: Issue 152: Getting started with programming
Date: 2021-12-25 08:00
Tags: 
Category: Season 12
Slug: lmg-s12-issue-152-getting-started-with-programming
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) The Java Runtime Environment (JRE) bundles the Java VM and supporting libraries. The JRE has to be installed on the user’s system for Java programs to work, unless the program bundles the supporting libraries. Solo programmers can start programming with OpenJDK for free with fewer features and less support, while commercial companies can license Oracle JDK for better support and features.

So you started taking up programming. Maybe you went to a class, where everything was set up for you and you didn’t have to worry about installing and configuring necessary software. Or you took an online course, where step-by-step instructions were provided and you mostly didn’t have to spend time scratching your head. That’s how it should be; you paid to learn *programming*, not to learn how to configure a software development environment.

Once you actually have to start writing code though …

## Setting up a development environment

Let’s suppose you are writing code for a web application. You start by installing the software for the compiler/interpreter program, which either executes your code directly or compiles it into an executable binary ([Issue 54]({filename}/season5/issue054/issue054.md)).

Now you begin writing your code. Along the way, you begin to install various libraries ([Issue 17]({filename}/season2/issue017/issue017.md)) and frameworks ([Issue 18]({filename}/season2/issue018/issue018.md)) that your code relies on. These are provided in things called **packages**, which are basically zipped files containing all the files and metadata for the library/framework. You install these packages using another program, called a **package manager**, through the command line terminal ([Issue 15]({filename}/season2/issue015/issue015.md)).

You write more code. And one day … you’re done! The real pain has just begun!

## Deploying code

Thus far, you have been programming on your own laptop. But your laptop can’t handle a full webserver load once people start using your app, so you wisely decided to lease a virtual machine (VM: see [Issue 147]({filename}/season12/issue147/issue147.md)) from a cloud provider instead. You boot up the VM, it goes through its bootup process ([Issue 112]({filename}/season9/issue112/issue112.md)), and finally completes. You are greeted with a familiar command line, the text cursor blinking cheerfully.

How are you going to get your code on that machine?

Maybe you set up a code repository ([Issue 19]({filename}/season2/issue019/issue019.md)) on another server, and then download your code onto the VM with some commands.

Maybe you decide to turn your app into a package instead: you write software instructions (more code!) to tell the **package manager** (mentioned earlier) how to install the package, and how to configure everything. You add some files with metadata, a file manifest containing all the files used by the package, and then pack it up. You install yet more software (called **build tools**) to help you automate this part. Then you set up another file server, upload the package onto it from your laptop, download it from the VM, and install it on the VM using the same **package manager** software.

You test it, and after many hours of cursing, confused pacing and mumbling, and much hair-tearing, it finally works. Phew!

## Expanding the app

Unfortunately, the tiny toy server that you used to test your web app doesn’t hold up to real-world network loads. You’ll need to put the app behind a Real™ web server; as more and more users use it, you may even need to deploy your app to multiple servers to handle the load, all managed by a **load balancer**. The balancer receives the web requests ([Issue 9]({filename}/season1/issue009/issue009.md)), decides which of the multiple servers has the lowest load so far, and directs the request to it so it can serve a web response ([Issue 8]({filename}/season1/issue008/issue008.md)).

Deploying more servers … does that mean you have to do the above all over again?!

**Issue summary:** Actually making a web application requires you to set up lots of supporting software and carry out lots of steps to create a suitable app environment.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 153: Using the cloud

I hope this issue adequately describes the problem that the cloud attempted to resolve! When people talk about “using the cloud”, what is that actually like?

Next issue, I’ll give a peek. Short issue guaranteed.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
