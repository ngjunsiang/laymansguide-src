Title: Issue 94: Why do web browsers take up so much memory?
Date: 2020-11-14 08:00
Tags: app, cache, memory, operating system
Category: Season 08
Slug: issue094
Author: J S Ng
Summary: 
Modified: 2020-11-14 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Web apps have limited access to the device’ storage, and can only store data in browser-managed databases. Progressive Web Apps (PWAs) can additionally register service workers that run in the background. Because they are so cleanly sandboxed, they can be easily removed by clearing the browser cache and storage, and deregistering any service workers manually.

Apps once lived on a computer. You double-clicked them or pressed Enter or right-clicked Run, a window pops up and a rectangle appears on your taskbar. If Task Manager is showing you that it is using up gobs of memory, you just End Task and the rectangle disappears. Later in this season I’ll say more about what it is like to live in a computer, but we are on web apps now.

Web apps are somewhat more complicated. Because they are so tidily sandboxed ([Issue 92]({filename}/season08/issue092/issue092.md))), they cannot actually live on your computer. Instead, they live in your browser.

## Living in a web browser

Living in a computer means that the operating system (OS) takes care of you; it gives you the memory and disk space you need, gives you CPU time to run your processes, and gives you access to devices (such as the screen and keyboard).

When you live in the browser, the browser takes care of you. Everything you need is requested from the operating system (OS) by the browser. The space that the web app uses in localstorage, sessionstorage, IndexedDB, and the cache, is space that the browser requested. The CPU cycles that the web app needs are cycles that the browser has requested.

When you open the OS Task Manager, where do these requests show up? Under (one of) the browser processes, naturally. If you have more than 20 browser tabs open for more than 5 apps, it shouldn’t be surprising that they are using a lot of memory; I’ll go into why shortly. More worryingly, that’s not helpful if you’re trying to figure out which browser tab to close so you can play your memory-consuming video game.

Only the browser has that information; you will have to open the browser’s Task Manager (another google away) to see that information.

## A web app’s needs

I have a browser tab open now, with a Google Sheet loaded. What is the Google Sheet app doing on that page? Let’s open DevTools and find out.

DevTools has a really cool tab labelled “Memory”, and it has a nice visual depiction of what the app is doing with all that memory:

![Firefox DevTools, showing the Memory tab. The app is using 83.84MB of memory, and 32MiB of that is used by objects.]({attach}/season08/issue094/issue094_01.png)  
*DevTools in Firefox lets you inspect the memory that web apps use.<br />The Memory tab shows what is stored in memory.<br />Most of the memory here is being taken up by javascript objects.*    

Javascript `object`s here are Javascript’s own internal representation of data, which is quite similar to a document database’s format. Altogether, they take up 32 MiB of memory space (difference between MB and MiB is covered in [Issue 40]({filename}/season04/issue040/issue040.md))). Google Sheets is juggling a lot of data internally, data which is not stored in IndexedDB or localstorage!

`other`, taking up 15 MiB, seems to be pointing to a javascript library that Google Sheets is using to render the spreadsheet.

`strings` are simpler than `object`s, each one representing a snippet of text, or possibly even a number. They only take up 5MiB. `scripts` are the internally stored scripts that the page is executing; they take up 11 MiB.

`domNode` is where it gets interesting. We are used to seeing HTML documents ([Issue 50]({filename}/season04/issue050/issue050.md))) as a plain text document with lots of formatting, but in a browser it becomes more than just text. Each part of the page, an HTML element, can have its properties changed by Javascript as the page reacts to new data, or to user input.

## The HTML Document Object Model

It would be too computationally taxing to keep scanning through the text document to figure out which part of the page is meant to be changed. Instead, the browser has its own way of storing the *hierarchy* of elements: each menu option falls under a menu heading, which falls under the navigation bar, which falls under the header, which falls under the main document, and so on. If each browser had its own way of doing that, a web developer would have to learn all of them to make a webpage that worked across all browsers; that’s terrible!

Instead, the web standardised on one way of doing so: the HTML **Document Object Model (DOM)**.

Internally, a web browser converts the HTML page into a DOM—a data structure that makes it easy to find the specific HTML element (or elements) that need to be modified by each function. The HTML DOM for the page I’m on takes up 14 MiB, which may sound like a lot, until you remember that each element also has associated metadata stored along with its content. And Google Sheets has lots of elements!

----------

**Issue summary:** Web apps require the browser to request memory on their behalf, and thus their memory usage shows up under the browser process in the OS Task Manager. Web apps use this data to store a more convenient (but larger) representation of the webpage document, and to store the data needed by the app.

And that is how a web app uses up 84MiB of memory space. If you have multiple tabs running the same app (e.g. multiple Google Sheets open), some of the memory can be shared ([Issue 84]({filename}/season05/issue065/issue065.md))) by these tabs (e.g. `scripts`), but otherwise each tab is going to have its own memory needs.

In the earlier days of the internet, when spreadsheets were still a separate app, this memory usage would have showed up in the OS Task Manager under Lotus 1-2-3, Microsoft Excel, or some other spreadsheet program. Today, it shows up under Chrome or Firefox, and the details are only inspectable through the browser’s Task Manager.

No wonder browsers get all the blame these days.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 95: What’s in a mobile app?

This issue felt like a data dump; I know it’s a lot all to take in 😅 In my childhood, I had access to lots of books with these cutaways showing the inner mechanisms of devices of all sorts, and I loved those books. It’s rather harder to do the same with software, since there’s nothing to physically slice through (even if only in the imagination!) I hope that the screenshots in this season of LMG will help you imagine the inner mechanisms of apps. Let me know if it’s working for you, and if there’s anything you’d like to see :)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
