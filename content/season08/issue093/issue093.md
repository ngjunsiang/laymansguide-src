Title: Issue 93: What's in a web app?
Date: 2020-11-07 08:00
Tags: app, cache
Category: Season 08
Slug: issue093
Author: J S Ng
Summary: Web apps have limited access to the device’ storage, and can only store data in browser-managed databases. Progressive Web Apps (PWAs) can additionally register service workers that run in the background. Because they are so cleanly sandboxed, they can be easily removed by clearing the browser cache and storage, and deregistering any service workers manually.
Modified: 2020-11-07 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Sandboxing is a catch-all term for the concept of ensuring apps don’t have access to resources outside of their privileges. Sandboxed apps are generally safer than non-sandboxed apps in terms of security, and easier to manage, terminate, and uninstall.

The simplest apps we use do not _generate_ data; think about your calculator, which simply crunches calculations and displays the result (conveniently ignoring the ones with memory slots for storing calculated values …). Or currency converters, or timezone converters … no storage needed.

So how do web apps store data?

## Data storage in web apps

As a web-first programming language, Javascript programs were not expected to have to access, open, or create files on the device. That would make it really easy for a malicious script to download malware to a folder, where it could be accidentally invoked! Instead, it relies on other features to store and retrieve data for specific purposes:

1. To remember user logins (the “Remember me” feature you see on almost every login screen), web apps can set/unset cookies ([Issue 69]({filename}/season06/issue069/issue069.md))) in the browser.
2. To obtain files for use, the web app can invoke a File Select dialog for the user to choose a file, such as for uploading to the server. The web app is not allowed to access arbitrary files this way.
3. If data needs to be provided to the user in the form of a file, it can be stored on the disk with the user’s permission through a download dialog.
4. The web app can store data through a browser feature called **localstorage**. This is a *key-value database*, managed by the browser, that allows you to store data (the *value*) tagged to a *key*. The same way a hotel lobby holds your luggage for you and lets you access it through a luggage tag, or the way you can rent a locker for storing your stuff (*value*) and access it through the locker *key*.
5. For data that is only needed in that tab (e.g. partially filled form data), and can be safely deleted when the tab is closed, the browser provides **sessionstorage**. This works similarly to localstorage.
6. For more significant amounts of data, web apps can use IndexedDB, a more advanced database also managed in the browser. It is a document database ([Issue 88]({filename}/season07/issue088/issue088.md))), with each document tagged to a key in a key-object system.

![Firefox DevTools, showing the Storage tab. Local Storage is selected, displaying a list of keys and values.]({attach}/season08/issue093/issue093_01.png)  
*DevTools in Firefox lets you inspect the data that web apps keep.<br />The Storage tab shows what is stored in cache, cookies, IndexedDB, localstorage, and sessionstorage.<br />IndexedDB, localstorage, and sessionstorage are key-value databases that store the data (value) tagged to a key.*    

## Requesting and receiving data on a server

So a web app doesn’t much in the way of storage access, but they were not designed for that at all. Most of the heavy lifting is not meant to be done in the browser, but elsewhere, on a server. A web app would send heavy workloads to a server (typically owned by the same company) through an API ([Issue 4]({filename}/season01/issue004/issue004.md))) through a web request ([Issue 9]({filename}/season01/issue009/issue009.md))), and receive the results through a server response ([Issue 8]({filename}/season01/issue008/issue008.md))).

A web app would also need resources for display: images, videos, PDFs, ... these are requested and received via web requests as well.

Cool, so a web developer can just write Javascript code to get the data and resources it needs, display stuff to the user, wait for the user to interact, and then make more requests to the server to calculate stuff, or send the app more data (such as the user’s tweets or posts or other stuff).

Just one problem with this: if internet connectivity is intermittent or laggy, none of this is going to work! Even when the internet is fine, it makes for a very slow experience. How do we improve this?

One way is to cache ([Issue 39]({filename}/season03/issue039/issue039.md))) as many things as possible: header images, logos, emojis, icons, … these can all be stored in localstorage and accessed even when the app is offline.

Some apps, such as Google Docs, will also store user data in IndexedDB for a smoother experience—imagine having to wait for a request-response round-trip to the Google servers for every word you type. The data gets modified in IndexedDB first, and then synced to the servers. If the device gets disconnected from the internet, at least you will still be able to read whatever is in IndexedDB (and if you have enabled offline access, you can even edit the data in IndexedDB, and the Docs app will attempt to sync it to the server once connectivity is restored).

## Running background processes

Then what’s with these popups on some websites asking you to install them? And how are some websites actually able to send us notifications? Something has got to be running in the browser background for these to happen, and none of what we have learned so far explains that … what gives?

Enter **Progressive Web Apps** (PWAs). With some Googling and lots of reading on StackOverflow and other web documents, a web developer can get started meeting the various requirements needed to create a PWA.

And in exchange for that inconvenience, she can use **service workers**: javascript scripts that run on their own and are not dependent on the browser tab staying open. These service workers can listen for messages from the server, carry out some processing, make requests and receive responses, all independently from the app running in the tab. On mobile devices, they are gradually gaining more features as well, such as access to the Share feature (enabling users to share content with the PWA), and being able to access cameras, microphones, location services, and other things (provided the user grants permission).

## Installing web apps

Okay, wait. WHAT?!

I imagine most folks would be okay with cookies, with localstorage and even IndexedDB. You want things from an app, you gotta give it space to work, right? That’s fair.

But service workers, what?! You mean if I click Install, these apps get to run stuff *in the background* in my browser, even after the tab is closed? If I’m not cool with that, I can just choose not to install and then these service workers won’t get installed, right?

Umm, I don’t know how to break this to you gently, but nope.

Once you visit a site (URL) with a registered service worker, your browser automatically registers it. The only thing the Install button does is to add a shortcut on your Desktop/Home Screen, and perhaps enable some features (such as mobile Share). But the service workers are already there.

## Uninstalling web apps

And now the good news.

Because web apps are so cleanly sandboxed, they don’t stick tendrils into your operating system or device storage (beyond the space reserved by the browser, anyway). Removing apps and their files just involves clearing your browser cache and website storage. You will, however, have to deregister the service workers manually; please google for instructions.

**Issue summary:** Web apps have limited access to the device’ storage, and can only store data in browser-managed databases. Progressive Web Apps (PWAs) can additionally register service workers that run in the background. Because they are so cleanly sandboxed, they can be easily removed by clearing the browser cache and storage, and deregistering any service workers manually.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 94: Why do web browsers take up so much memory?

I’m finally starting to answer one of the sometime-in-the-future questions below, and can’t wait to get to the meat of “What is involved in installing a piece of software?”; it’ll be a ride! :)

Before I move on to compare web apps with mobile apps, I’m going to take a short detour next issue and answer a question I hear all too often: “Why do web browsers take up so much memory?”

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
