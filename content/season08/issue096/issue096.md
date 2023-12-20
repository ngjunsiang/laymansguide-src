Title: Issue 96: Why are mobile apps so large in size?
Date: 2020-11-28 08:00
Tags: app
Category: Season 08
Slug: issue096
Author: J S Ng
Summary: 
Modified: 2020-11-28 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Mobile apps, unlike web apps, can bundle resources and libraries to be installed to a mobile device. They can also request access to storage, and typically have a higher memory limit than web apps.

In the process of creating an app, a developer often needs to use libraries ([Issue 17]({filename}/season02/issue017/issue017.md))), which are ready-packaged chunks of code she can run without having to write the code herself. Some provide core functions (e.g. sending information via the Internet, or checking if a data connection is available), while some provide optional features (e.g. mobile payments, or user feedback systems).

Libraries that provide core functions are typically provided by the operating system (OS), which ultimately controls the device’s resources, but all else have to be pulled in by the app, somehow.

## Web apps vs mobile apps

Web apps, which I covered in [Issue 94]({filename}/season08/issue094/issue094.md)), pull in any resources they need through web requests. This includes any libraries that they need. The browser allows it to do this, but prevents access to most parts of the operating system, and allows limited access to camera, sound, storage, etc. The sandboxing features of the browser make web apps generally safer to access.

A mobile app, on the other hand, is sandboxed by the operating system. Most of the resources it needs have to be present at the time of running the app, and that includes libraries. In an unsandboxed environment, commonly used libraries (e.g. mobile payment libraries) could be installed in the OS and shared by the apps. But this opens up a means of unauthorised access to multiple apps: hack this library successfully, and all other apps on the OS are also affected!

The sandboxing system in a mobile device does not allow this. Each app must bundle all the libraries it requires, to be installed into storage after downloading. This way, if an app has one or more libraries compromised, it would at least not expose the user’s data in other apps.

## Libraries in a mobile app

The tradeoff to separating all these mobile apps and preventing sharing, is that each app now comes with its own copy of all the libraries it needs. And the file size can really add up—you already see it in the huge app sizes. I unbundled the installation package of a popular shopping app, Lazada, just to see what is inside it.

The list is way too long to post as an image, or even as text; it has over 300,000 code functions bundled inside! I should note that I am not an Android developer and can’t tell you very much about whether these libraries are absolutely necessary, but here are some noteworthy libraries included that I can make an educated guess about:

1. Libraries to translate code from one programming language to another (often to translate an easier language into a faster or better-supported language)
2. Compatibility fallback & device evaluation libraries (probably for devices on older Android versions)
3. Layout libraries (for calculating placement of window frames in devices with different screen sizes)
4. Graphics, media, augmented reality (AR) libraries (for graphics rendering, video playback, capturing images from camera, etc)
5. System, network, version detection and updating, etc
6. Animation libraries (I see one from AirBnB)
7. Analytics libraries (to track user and ad engagement, and do A/B testing)
8. Debug, crash reporting, logging libraries (for troubleshooting app crashes)
9. Integration libraries (for login using FB and other accounts)
10. Maps, location
11. Search, image search, QR code, user feed, and related services
12. Database access (it seems to use Google Firebase, in addition to others)
13. Mobile payments

and then there is the app itself, which contains code for:

14. Address validation, checkout, delivery
15. User feed and homepage, login management, recommendations
16. Search

and many others which I don’t know about.

## Why aren’t web apps so huge then?

They are! But they don’t need many of these (e.g. code translation and compatibility), and most of the libraries in 1–13 would have been loaded separately from the main page (see [Issue 78]({filename}/season06/issue078/issue078.md)) for a visual example). Much of the functionality would not need to be loaded or installed upfront, only when it is required (e.g. map display).

For a web app, many more functions would also have been offloaded to Lazada’s servers, such as address validation. On a mobile app, this code is included upon installation to reduce data usage.

More importantly, you have little idea how large a web app really is, since you are never shown its filesize anywhere ;)

**Issue summary:** Mobile apps are sandboxed by the operating system. As a result, they have to bundle all the libraries they need, and are not allowed to share libraries with other apps. This results in mobile apps with huge filesizes.

It’s worth thinking about what this says whenever we hear about so much data being transmitted over the internet. Much of this data is actually duplicated data (for security of inefficiency reasons), or metadata (for data management), or overhead data (because of the way the data is packaged). Just like Amazon packaging!

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 97: Laptop apps

Finally we can move on to more fully explore the complexity of apps that integrate more closely with the operating system: laptop apps!

This should be enough of a primer before I go on to talk about where all this app data goes, and then about app installation and uninstallation (and hence strike out another “sometime in the future” question, woohoo! 🙌)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
