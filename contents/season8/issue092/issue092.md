[**Previously:**](https://buttondown.email/laymansguide/archive/) Depending on what you need a database for, there may be online database platforms that can manage and automate much of the work for you. Airtable, Smartsheet, Knack, and Zoho Creator are just 4 of many options that offer an easier way to set up and input your data, then access them through apps or other means.

There was a time when apps, short for _applications_, were these files that came on a CD or diskette, usually ending in `.exe` (if your settings enabled you to see file extensions). You double-clicked them or pressed ‘Enter’, and things happened.

Today … the idea of an app is more nebulous. The `.exe` files are still there, but now there are also apps that you install from the app store. And what’s up with webpages that display an app installation pop-up and create an icon on your home screen or desktop? Are they the same kind of app? If not, what’s the difference between them?

Before I answer that question, we need to talk about an important concept called **sandboxing**.

## Why do apps need to be sandboxed?

An unrestrained app running in your operating system would have access to any and all resources on that machine. It could potentially modify or remove system files, halt running programs or accidentally overwrite their memory contents, and so on.

[The operating system]([Issue 56]({filename}/season5/issue056/issue056.md

This is why sandbox systems were already being researched as early as the 1970s, and are still an ongoing research interest at many institutions.

## What is sandboxing?

If you are old enough you might remember playing in a sandbox. While there are usually no explicit rules about how to play in a sandbox, there is usually one unspoken rule:

What was in the sandbox, stays in the sandbox.

A sandbox limits the mess, yet gives you unrestrained freedom _within_ that box.

In a computer, a sandbox system imposes restrictions on running applications. Some common restrictions include:

- only being able to access/change/delete files within a particular subfolder
- only having access to some OS resources (e.g. not being able to access USB devices, or audio, or webcam)
- having limited privileges while the application is not active (e.g. no internet access when not being directly interacted with, and just running in the background)

These restrictions are intended to limit any damage and keep the system more stable than it might otherwise have been.

So one way to categorise laptop apps, mobile apps, and web apps is in the amount of sandboxing they are subject to.

**Issue summary:** Sandboxing is a catch-all term for the concept of ensuring apps don’t have access to resources outside of their privileges. Sandboxed apps are generally safer than non-sandboxed apps in terms of security, and easier to manage, terminate, and uninstall.

Keeping it vague in this issue because the details really differ between operating systems, kinds of apps, and even the way they are distributed. We’ll be digging into details next issue, starting with the most heavily sandboxed app: the web app.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 93: What’s in a web app?

From just little snippets of script that animated buttons and counted visitors back in the 90s, Javascript now powers a huge portion of the Internet, processing payments, serving ads, and much more besides. We’ll look at how this gets packaged into a web app next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
