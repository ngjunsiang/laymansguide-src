[**Previously:**](https://buttondown.email/laymansguide/archive/) Typeface families consist of multiple fonts for each style in the typeface. Each font consists of glyphs, which are mathematical shapes described by curves joining points. These shapes need to be rasterised for display on a computer screen, or for printing on paper. Font files usually come in `.ttf`, `.otf`, or `.woff` formats.

Brief recap of the past few issues:

- **Content distribution:** Images and other media are distributed with the help of content distribution networks (CDNs, [Issue 160]({filename}/season13/issue160/issue160.md
- **Code distribution:** Webpage documents and web scripts (in Javascript) are distributed from the host server (which may comprise more than one computer).

And all of these takes place over the World Wide Web, often through the HTTP protocol ([Issue 7]({filename}/season1/issue007/issue007.md

What about the software we use, and the oft-dreaded Windows Updates? How does that get to us?

## Software distribution on Windows and MacOS

Okay there’s not actually anything new to say here, just checking if we have the same understanding of how to find new software:

You’ve got your system updates and whatnot, inconveniences that sometimes force themselves on you. These generally come from a secure server from the operating system (OS) maker, which is Microsoft or Apple.

You’ve got software made by Microsoft/Apple, which you either download from their website or install through your browser.

Then there’s the software in their app stores. These app stores are listings of software which developers pay to have their software listed in. A big selling point of app stores is their supposed security: app stores usually have a screening process to ensure that submitted apps are not doing Evil Things™ which harm their users. So when you download an app it is assumed that this app has passed some kind of rigorous screening process.

Developers often pay a proportion of their revenue to the app stores for this “privilege”.

And then there is … all the other software you can download from the internet.

I’m guessing the internet is where most of the desktop/laptop software you use comes from.



## Software distribution on Android and iPhone

On the mobile side of things, it looks remarkably similar, but with the weightage somewhat different.

System updates, coming from the OS maker — check.

Software made by the OS maker — check, but coming through app store instead of internet.

App stores — check, still the same.

Software from the internet — Android allows installing software from “unknown sources”, but you’ll have to enable a system setting to allow that. It is off by default. On iPhone, this is just not possible.[^1]

[^1]: Okay not true, you can replace the OS on your phone through a process called **jailbreaking**, but this is a layperson’s newsletter and I do not recommend this without much more extensive reading and careful consideration.

I’m guessing the app store is where most of the mobile apps you use come from.



## Software as an ecosystem

Notice that in neither case is finding software like foraging for berries: there is an entire ecosystem that goes into making these actions possible!

The **OS makers** obviously have to distribute their OS, supporting software, and updates reliably and securely, so that other software can rely on its continued existence. An OS by itself doesn’t usually do much for users; they need software to create and manage their files, and access the internet. And much of this software is going to be created by other developers, not the OS makers.

The **developers** need documentation and sample code to understand how to write the software, and these usually come from the OS makers. But it can also come from a thriving community of other developers who are writing software for the same system.

And then there are the **discovery mechanisms** that users need to find useful software; Google is the fallback when this doesn’t exist, but you usually want users to have a better experience than googling for installers and potentially installing malware.

Even this understanding is incomplete, but it’s the beginning of a more nuanced model of software development that will help you understand why software often does not do what it should. We are talking about factions in software development.

Far too often I see users who have no awareness of this divide, and seem to operate on an assumption that software comes from “programmers”, a hallowed, unreachable group of entities that blesses users with features or curses them with bugs at their whim.

**Issue summary:** Software that we use usually comes from the OS makers, or from third-party developers. These two groups of developers are not the same, and might even have conflicting intentions and goals.

If I keep going on in this vein I’m going to bring in politics, and I don’t want to do that. Instead, I’ll introduce a slightly different kind of software ecosystem, which non-Linux users are likely not familiar with. My hope is for you to see that \*handwaves at above paragraphs\* _this_ isn’t the only way for software distribution to work!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 164: Linux, the universal operating system

What does a model look like when there is no central app store, controlled by the OS makers? That is how the Linux distribution system works!
