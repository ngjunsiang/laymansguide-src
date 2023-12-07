Title: Issue 95: What’s in a mobile app?
Date: 2020-11-21 08:00
Tags: 
Category: Season 8
Slug: issue095
Author: J S Ng
Summary: 
Modified: 2020-11-21 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Web apps require the browser to request memory on their behalf, and thus their memory usage shows up under the browser process in the OS Task Manager. Web apps use this data to store a more convenient (but larger) representation of the webpage document, and to store the data needed by the app.

“Why use the mobile app when there’s already a website?”

“Why even have a mobile app that looks almost exactly like the website?”

I’m not going to answer from an aesthetic or user experience point of view, you’re all experts in your own preferences :) Instead, I’ll focus on whats actually under the hood in this newsletter issue.

If you haven’t read [Issue 93]({filename}/season08/issue093/issue093.md)) on web apps (a.k.a. websites), I’d recommend you do that for the full context, because in this issue I’ll highlight some key differences between web apps and mobile apps.

## Resources

Web apps have to request every single image, video, non-text object on the page via a web request. Caching ([Issue 39]({filename}/season03/issue039/issue039.md)))—storing these resources for offline use—can reduce subsequent load times, but the first load will still be the most painful.

A mobile app can package the most common, unchanging resources (logos, button images, backgrounds, etc) into the mobile app itself, so they can be loaded directly in the app, without having to make a web request and wait for the response. This lets it load faster (theoretically … in practice, many apps still have to retrieve other data from the server, so the loading speed improvement is marginal)

## Flexibility

The document object model, or DOM ([Issue 94]({filename}/season08/issue094/issue094.md))) is how web apps keep track of all the elements and their contents on a page, but it is not the most efficient way to do so. A mobile app has more choice in deciding which user interface library ([Issue 17]({filename}/season02/issue017/issue017.md))) it wants to use.

## Storage access

A mobile app can request permission to access storage on the mobile device, allowing it to store files (images, data, ...) on the device without having to interrupt the user each time. It is not limited only to browser storage interfaces (localstorage, sessionstorage) and browser databases (IndexedDB)—see [Issue 93]({filename}/season08/issue093/issue093.md))—but can use other kinds of interfaces and databases, if they are available on the mobile device, or bundled into the mobile app.

## Memory use

Both Android and iOS impose a memory limit on each app that is running. And they treat a mobile browser as a single app, despite all the web apps running inside it. So a web app has to share that limit with all the other web apps running in the mobile browser (which is why your tabs have to reload so often—they are also cleared often!).

On the other hand, a mobile app can have that per-app limit all to itself.

----------

All told, a mobile app has more resources, which it requests directly from the OS instead of via the web browser, and it has more freedom in using those resources.
How so? And more importantly, why are some mobile apps just so darn *huge*?

This and mobile app sandboxing explained next issue.

**Issue summary:** Mobile apps, unlike web apps, can bundle resources and libraries to be installed to a mobile device. They can also request access to storage, and typically have a higher memory limit than web apps.

Mobile apps are a bit of a weak spot for me since I haven’t had as much experience here as I had in other areas, but nonetheless the limits of sandboxing are pretty visible. For the most part, we have accepted this tradeoff between size and security since storage space became much cheaper. But this tradeoff is also apparent not only in software, but also in business management and other areas: to increase security, we often also have to increase bloat.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 96: Why are mobile apps so large in size?

Remember the days when most apps we downloaded and installed on a laptop were 2MB or less? Today, mobile apps are many times that size. This is partly because of the way sandboxing is done for mobile apps. How so? I’ll go into more detail next week ;)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
