[**Previously:**](https://buttondown.email/laymansguide/archive/) Apps generally handle three categories of files: its own (permanent) app files, (shared) user files, and (ephemeral) temporary files.

What we are here to find out is: where do these apps keep their data, and how can we get rid of them (if we really want to)?

Web apps and mobile apps will not be discussed here, because they are much more heavily sandboxed, everything gets confined into the app’s little prison, and we generally don’t have these concerns when it comes to them.

## Just one little niggle ...

I am so sorry to burden you with this otherwise unrelated information, but since there are a significant number of Windows users and a significant number of MacOS users, I had to bring this up at some point.

Windows and Mac manage this differently, so we are going to have to talk about two different kinds of systems. I will spend more time on the Windows system, because it needs more time.

Let’s get the easy one out of the way first: this issue deals with ...

## Mac-like systems[^1]

[^1]: The technical term is "Unix-like systems", but we don’t need to know that, even if all the Unix fanfolks are pointing pitchforks at me now.

On MacOS (and Linux) systems, everything is a file. All files get stashed into some kind of folder.

I personally prefer this because you have everything sorted into sensible top-level folders[^2]. Mac has:

[^2]: There’s lots of things that make less sense once we get into more detail, but fortunately we don’t do that here.

- an `/Applications` folder for apps
- a `/Library` folder for shared files (see [Issue 17]({filename}/season2/issue017/issue017.md
- a `/System` folder for, well, you know what.
- a `/Network` folder for accessing resources on the network (such as shared folders)
- a `/Users` folder for accessing user folders and files
- a `/Drives` folder for accessing other storage devices (e.g. USB drives)

and then, similar to Linux, it has `/bin`, `/etc` and other weird-looking folders that we don’t need to worry about at this point. Just treat them similar to system files and try not to touch them. The apps that we install generally do not clutter up these folders unnecessarily.

Logos, backgrounds, buttons, and other application data? They go into `/Applications`. What if other apps also need to use them? Then they go into `/Library`. What if a user installs a program that they don’t want other users using? It goes into `/Users/username/Applications`. User settings? They go into `/Users/username/Library` (under a subfolder for the app). Temporary files? They go into `/Library/Caches`.

Linux systems are similarly divided, but into differently named folders. Everything is still a file, and belongs in some folder somewhere.

So to uninstall an app, you remove its files from `/Applications` or `/Users/username/Applications` and from `/Library`, and that’s usually it. Apps are usually quite good at doing that themselves, so you don’t need to worry.

And then we deal with Windows systems in the next issue.

**Issue summary:** MacOS, Linux, and other similar systems treat everything as a file, organised into appropriate subfolders.

I’m keeping this issue short because the next issue will be much longer. \*Ominous music plays\*

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 100: Where does all the app data go? A look at Windows systems

The reasons for the difference between Mac-like systems and Windows systems is, again, historical, but I better prepare you because you are not going to like the next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- a password hash? [Issue 63]
- a driver file and why do I need one? [Issue 98]
