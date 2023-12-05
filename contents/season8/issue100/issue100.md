Title: Issue 100: Where does all the app data go? A look at Windows systems
Date: 2020-12-26 08:00
Tags: 
Category: Season 8
Slug: lmg-s8-issue-100-where-does-all-the-app-data-go-a
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) MacOS, Linux, and other similar systems treat everything as a file, organised into appropriate subfolders.

Previous issue: Mac- and Linux-like systems. Since the key points are so short, let’s summarise:

On Mac-like systems, the top-level folders are

- an `/Applications` folder for apps
- a `/Library` folder for shared files (see [Issue 17]({filename}/season2/issue017/issue017.md), but on Mac this extends to things like sounds, profile pics, colors, ...)
- a `/System` folder for, well, you know what.
- a `/Network` folder for accessing resources on the network (such as shared folders)
- a `/Users` folder for accessing user folders and files
- a `/Drives` folder for accessing other storage devices (e.g. USB drives)

Linux systems are similarly divided, but into differently named folders.

This issue: (A rant on) Windows.

## Windows-like systems (who am I kidding, there’s only Windows)

Unlike Mac-like systems, where all data comes in the form of a file, Windows systems recognise two types of data: settings, and files.

### Files in Windows systems

- Apps get put in `C:\Program Files` or `C:\Program Files (x86)`, for 64-bit and 32-bit programs respectively[^1]
- Library? Shared files? Ha! (I’ll talk about this further down)
- System files go into `C:\Windows`
- Network resources, well ... don’t really have a ... well they are a different category of location that does not start with a drive letter and instead starts with `\\`, unless you assign these locations to a drive letter, then they have a drive letter. Sorta.
- User files go into `C:\Users`
- Other storage devices are auto-detected and assigned a drive letter, though not always consistently.

[^1]: I really was hoping not to have to explain 32-bit vs 64-bit programs ever since [Issue 55]({filename}/season5/issue055/issue055.md), so for now let’s just say 32-bit programs are for 32-bit CPUs and 64-bit programs are for 64-bit CPUs. Unfortunately many old 32-bit apps have not caught up with the times and converted themselves to 64-bit apps, so Windows has to do hacky stuff to make old 32-bit apps work on modern 64-bit CPUs.

And now we talk about settings.

### Settings in Windows systems

Settings are stored in the `C:\Windows\System32\Config\` and `C:\Windows\Users\Name\` folder, which technically makes them system files, which ... wait, how are apps supposed to access them then?

App developers are supposed to do it through a system library, which provides variables named like `ApplicationData.LocalSettings`, `ApplicationDataCompositeValue`, and `RoamingSettings`. These variables let developers store and retrieve settings, which all end up stored in a system known as the **Windows Registry**. And Administrators can edit them using something known as the Registry Editor.

The Windows Registry consists of 5 top-level areas (known as hives), each one beginning with the word `HKEY_`:

- `HKEY_CLASSES_ROOT` is for storing application settings, and file extension information (e.g. which app to use to open each type of file extension)
- `HKEY_CURRENT_USER` is for storing settings and configuration specific to the current (logged in) user
- `HKEY_LOCAL_MACHINE` is for storing settings and configuration common to all users (e.g. default settings)
- `HKEY_USERS` is for storing settings and configuration of each user. The `HKEY_CURRENT_USER` data for all users is stored here, and copied to `HKEY_CURRENT_USER` when they log in.
- `HKEY_CURRENT_CONFIG` is for storing information about the computer’s configuration and resources

The usual way of finding out how to modify a particular setting for X is to google “registry setting for X” and proceed from there.

Logos, backgrounds, buttons, and other application data? They go into `C:\Program Files` (or `C:\Program Files (x86)` if still 32-bit) for traditional Windows apps, or into `C:\Program Files\WindowsApps` for Windows App Store apps. What if other apps also need to use them? Then they go into ~~`C:\Library`, just kidding, if only it were so easy~~ `C:\Program Files\Common Files`, but you’ll notice it’s pretty empty. Usually, they’ll be stored within the app’s folder, and you have to find out where to edit the Windows Registry so other programs know where to find them (apparently you can look in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs`). Whoa, wait, what happened to apps not messing around in each other’s folders—

OKAY MOVING ON—What if a user installs a program that they don’t want other users using? It goes into `C:\Users\username\AppData\`. User settings? They go into—nah, they don’t go into a file, they’re supposed to be settings so they go into the Windows Registry somewhere under `HKEY_CURRENT_USER`. Temporary files? They go into `C:\Windows\Temp`; isn’t that a system folder? Well yes, but if you put it in `C:\Temp` folks will complain and Disk Cleanup will not find it.

So to uninstall a Windows app, you run its uninstaller. Which may or may not work perfectly. Or it might remove its files but still appear in the Program List because it did a terrible job cleaning up its settings in Windows Registry. So you reinstall the program, this time using a third-party app that helps you track app installations and registry changes, so that it detects what new files/settings it creates, and then when you uninstall the program you do it through the third-party app so that it hopefully removes all traces once and for all.

Phew. And that’s all I hope.

**Issue summary:** Windows systems categorise data into two types: files, and settings. Files are stored under an appropriate subfolder in `C:\`, while other storage devices and network locations are stored elsewhere or given their own drive letters. Settings are managed through the Windows Registry, which is stored in `C:\Windows\System32\Config\` and `C:\Windows\Users\Name\`.

Okay so this ran much longer than I expected. In fact, it ran so long that I split it into two issues. I promised to explain computers as simply and jargon-free as possible, and I hope I have managed to do that. I am definitely biased, and that I do not apologise for, because this newsletter issue would be half its original length if \*muttering\* *some* operating systems would just follow sensible principles that *other* operating systems have no problem following ...

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 101: Why do apps crash?

Moving on from app files and settings, the next few issues will explore common app problems. Coming up next issue: why do apps crash?

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
