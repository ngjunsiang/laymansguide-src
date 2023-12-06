Title: Issue 98: Temporary files
Date: 2020-12-12 08:00
Tags: 
Category: Season 8
Slug: issue098
Author: J S Ng
Summary: 
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) A laptop app can do practically anything, if it is running through the Administrator/root account. Sandboxing is carried out through permission control.

Thus far, I’ve summarised the salient differences between web apps, mobile apps, and laptop apps (my own terminology). I think we can move on to talking about their similarities.

There is a category of app that needs access to your device storage. It might be Youtube trying to download (part of) a stream onto your device for playback. Or it might be Tiktok trying to help you record a video for uploading. These apps need storage access so they can stash all the data into files, rather than hogging device memory with it. The same way we stash things into drawers and cabinets when we don’t need them, so they don’t clutter the space around us. And then we forget about them until we run out of space 😅

You almost never see where those files appear. They get hidden ... *somewhere* \*gesticulates around\*.

## Temporary files

These files are short-lived; they typically don’t stick around for more than a few days. For that reason, they are known as **temporary files**.

In a webapp, the browser generally stores these files into one of its allocated folders, somewhere in `C:\Users\[USERNAME]\AppData\Local\Google\Chrome\User Data\Default\Cache` or the like. They get cleared when you clear your browser cache. On a mobile or laptop app, the operating system designates a space for temporary files, in `C:\Windows\TEMP` or `AppData\Local\Temp` for Windows, or `/tmp` on Linux. You can clear those files through Disk Cleanup in Windows.

In general, temporary files are things you are not supposed to think about too much. The operating system has ways to clear them regularly. Apps are supposed to use these standardised locations to stash temporary files, and attempting to place them anywhere else is considered impolite, like leaving your stuff lying around in an office or otherwise public space.

## User files

But then, sometimes the app produces useful data that you want to keep around! Your journal which you keep in a Word document, photos of your cat or dog, and the copious, copious video files ...

Webapps have no space for you to do that. You are just supposed to save them onto your phone or laptop; the browser has no way for different users to stash their own files.

Most smartphones assume they are going to be used by a single user, and you just stash those files directly into phone storage. Not the best system, but it is what it is.

Laptops are where it gets a bit more interesting. Most laptop operating systems (OSes) assume they might be used by multiple users, each on their own account (hence the login screen), and therefore allocate separate spaces where each user may keep their stuff, inaccessible to other users except Administrators ([Issue 97]({filename}/season8/issue097/issue097.md))).

On Windows, these users each have their own folder in `C:\Users\`; on MacOS, that’s in `/Users/`; on Linux, it’s typically `/home/`. (Don’t ask about the `\`s vs `/`s; its one of those things that’s just the way history happened and has no real technical reason behind it.)

## App files

Of course, each app needs to have *its own space* to keep *its own files*, which allow it to do what it does.

Webapps get their own folder somewhere in `C:\Users\[USERNAME]\AppData\Local\Google\Chrome\...`, they can only see what is in that folder, and they cannot see what is in the parent folder, or sibling folders. It’s sandboxing, again ([Issue 92]({filename}/season8/issue092/issue092.md)))!

Mobile apps get stored into `/data/app` or some similar folder, and you’re not supposed to think too hard about where, because of \*handwaving\* *sandboxing*. The same idea applies: The app is not supposed to know, or be able to see, where other apps store their data! Eyes on the app’s own data only, and the user’s data (you did give it permission to access storage, right?), and any temporary data which it has created.

Laptop apps get stored in `C:\Program Files`, and interestingly enough have some kind of civil arrangement where they agree not to delete each others’ files, although antivirus programs have this passive-aggressive low-key thing where they like to mark each others’ program files as potential malware \*shrug\*.

## System files

These files were around ~~in the beginning of time~~ when the OS was installed; that means when you bought your laptop, they were already there, and any sensible system would prevent non-Administrators from mucking around with them. Windows stashes them in `C:\Windows`, while MacOS and Linux store them in `/bin/`, `/lib`, and various similarly opaque folders.

I might go into more detail about these, possibly in a future season when I talk about operating systems, but for now we are done talking about categories of files. Phew!

**Issue summary:** Apps generally handle three categories of files: its own (permanent) app files, (shared) user files, and (ephemeral) temporary files.

In reality, there are a whole bunch of different filetypes and other little details that apps need to worry about, but this is a newsletter for layfellas so let’s start simple.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 99: Where does all the app data go? A look at Mac-like systems

I separated temporary files and user files in this issue. Temp files are files that come and go, like stray cats, while user files are shared with other apps as well and there’s really not very much that you can predict about them except hope users don’t do anything too crazy. System files are strictly off-limits so don’t even think about that.

But meanwhile, as an app developer, even after you exclude the above categories of files, there is still a whole bunch of questions you kinda need to worry about at some point:

- where do I store my logos and backgrounds and buttons and other data?
- where do I keep my settings?
- where do I keep user settings?
- if my program is meant to make a USB device useable, where do I drop the driver files? (Yep, that’s gonna need its own issue)
- what if someone uninstalls my program but I want them to be able to keep their settings around in case they decide to reinstall and then it can feel exactly the way they left off?

Yeah I have no idea who actually thinks about that last question either, but it’s something that seems to get asked in every software uninstallation \*shrug\*.

So let’s get into that in the next issue.

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
