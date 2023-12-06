Title: Issue 164: Linux, the universal operating system
Date: 2022-03-19 08:00
Tags: 
Category: Season 13
Slug: lmg-s13-issue-164-linux-the-universal-operating
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Software that we use usually comes from the OS makers, or from third-party developers. These two groups of developers are not the same, and might even have conflicting intentions and goals.

Last issue, we looked at the following categories of software that an end-user might need:

- System updates
- Software by the OS maker (first-party software)
- Software from other developers (third-party software)

In general, “trusted” software comes from other sources: compact discs or the internet. While “trusted” software comes from a central, authorised source: usually some kind of app store.

This leads to a lot of conflict over who gatekeeps the list of “trusted” software. This privilege gives app store owners a lot of power, which they claim to earn by investing capital into making the OS possible, and implementing screening and filtering processes to ensure only secure software makes its way into the list.

I will not contest those claims here, but instead invite you to consider: what if it were possible for other app store makers to join in curating lists of software for that operating system?

## What is Linux?

Today the term “Linux” refers to a lot of things, which is why we need to clarify here: the term originally referred to [the Linux kernel](https://www.redhat.com/en/topics/linux/what-is-the-linux-kernel), which is the core of the operating system.

The kernel by itself doesn’t do anything without all the other programs that make it actually useable by an informed user: to create, edit, and browse files and folders, run service programs, etc. This collection of programs, along with the kernel itself, is [officially referred to as GNU/Linux](https://www.getgnulinux.org/en/linux) (but s’okay, you can just say “Linux” and we understand you mean GNU/Linux).

So, GNU/Linux is similar to Windows and MacOS: they are *base operating systems*, capable of doing stuff but not actually useful yet.

Where all our software at?

## Software for Linux

In the very early days, because there were a number of different hardware configurations that weren’t as compatible as they are now, Linux software was distributed as source code. You downloaded a zip file containing programming code, you ran a compiler program to compile the code ([Issue 54]({filename}/season5/issue054/issue054.md))) into an executable program. Then there is usually an **installer**, a shell script that puts the compiled program in the correct place so the OS can find it, and creates other helper files (like configuration information).

And then you had to check their website (or even email them, in the days before the mainstream Internet) regularly to see if there are any bugfixes, and if yes, you downloaded the *new* source code and repeated the process …

This was obviously tedious, so people started to compile the useful programs into their own list. This effort expanded, and became automated, so that it was not only a list, it was a collection of different versions of compiled programs for different CPUs (each version of the program is called a **package**). If you were a developer for one of the programs in that list, once you made a new version of your package you could submit it to these guys, they would incorporate the required changes and then add a listing for the newest version.

These projects came to be called **Linux distributions**, or **Linux distros** in short. Distros maintained **repositories** of software for their specific distribution—the people involved are called **maintainers**. Maintainers check new versions of software to ensure that it will work as expected on their distro. Another category of software, called **package managers**, were created for users to be able to use these repositories easily: to check for updates, install them, and perform any other required maintenance.

More and more distros started in the 80s and 90s, as groups of Linux users and developers decided to branch off based on differing principles and philosophies for managing a Linux computer and its software. Today, you have distros focused on reliability and stability, distros focused on simplicity, distros focused on user-friendliness, distros focused on scientific computing, distros focused on hackability, …

It is important to note that the Linux kernel development team itself does not maintain any distros. Any updates to the kernel are for distro maintainers to incorporate into their respective repositories.

## Linux software distribution

This means that for the bulk of users, software distribution on Linux is **centred around the distro’s repository**. Through the package manager, users can search for software, install it, and update it. They can also add the URLs of external repositories to access software from them.

At the same time, if users wish, they are still able to download compiled executables from the internet and run them (with the usual caveats, of course). They can also download source code, compile it themselves, and then run it. These options do not offer the same ease of maintainability as software installed through a package manager, since there is no repository to check for updates.

![Steam website showing Install Steam button for Linux. A popup asks what should Firefox do with the file, steam_latest.deb]({attach}/season13/issue164/issue164_01.png)  
<small>This is what many install pages look like on Linux, for software with Linux versions.<br />  
The Install button usually downloads a compiled executable, which can be run on the computer.<br />  
But installing through the distro’s package manager is recommended.</small>

No system updates sneaking up on you from the OS maker; updates and new software all come from the repository through the package manager. Unless you decide otherwise.

**Issue summary:** Linux software is distributed through Linux distros. The maintainers of distros maintain repositories of software that have been tested with the distro. Most users will access software in the distro’s repositories through a program called a package manager. So users have full control over when updates and new software should be installed.

This is as far as I’ll go for technical detail on Linux. I meant this to pick up from [Season 8]({filename}/season8/issue092/issue092.md)) on apps. It’s easier to go into the bird’s-eye view of how this works on Linux, because I’m more familiar with it; on the Windows and MacOS side of things it tends to be more esoteric and proprietary.

And it’s instructive to know this because … so far this season, we have been talking about distribution—content, code, and software. Notice how all of them involve infrastructure: worldwide clusters of servers for content distribution, a history of code changes for code distribution (and collaboration), and now we have repositories and package managers for software distribution.

What happens as this infrastructure ages?

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 165: The myths of system slowdown

We won’t dive into topics as broad as digital infrastructure aging; that’s beyond the scope for a layperson’s newsletter I think!

Let’s bring it back to personal scale: what happens as your system ages? The predominant symptom that manifests itself is general slowdown: your computer takes longer to switch on, open any app, save any file, and even to shut down. For years I have been googling for reasons why this happens, and satisfying/useful/sensible answers are almost non-existent. The pithy, vague answers about background services (“bloatware”), outdated apps, malware etc are almost insulting; I have relatives who use the same handful of apps, and even after clearing old/large files their phone is still slow!

Next issue, I attempt to look into these stated reasons and see if they make sense.
