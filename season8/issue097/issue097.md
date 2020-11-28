[**Previously:**](https://buttondown.email/laymansguide/archive/) Mobile apps are sandboxed by the oeprating system. As a result, they have to bundle all the libraries they need, and are not allowed to share libraries with other apps. This results in mobile apps with huge filesizes.

This issue is going to be short, because laptop apps are … well, almost unlimited in what they can do.

Web apps are sandboxed by the web browser. Mobile apps are sandboxed by the mobile operating system (OS). Laptop apps are sandboxed by the desktop OS (yup, Windows on laptop and desktop is practically the same).

The main difference here lies in the difference between a mobile and desktop OS. Mobile OSes do not allow mobile apps to share libraries with other apps, and restrict their privileges ([Issue 96](https://buttondown.email/laymansguide/archive/lmg-s8-issue-96-why-are-mobile-apps/)). Desktop OSes, on the other hand, let you do anything that is computationally possible … if you have permission.

## The Admin account

A desktop OS often has an all-powerful user, known as the Administrator (Windows/MacOS), or root user (Linux). This user does not need permission to do anything. But with great power comes great responsibility, and with an admin account it is all too easy to do something that renders the computer unuseable.

So lower-privilege accounts exist—these are the user accounts. Logging in as a user gives you limited privileges: often you cannot change OS files, install or remove apps, or do anything risky. This is, for the most part, how desktop OSes sandbox the computer environment from damage by other apps.

## What an admin can do

So what happens when you run an app on an admin account?

This app can:

1. Edit, delete, rename OS-related files
2. Create new “virtual” (emulated) hardware devices, and manage drivers for it
3. Send data to any device, or receive data from any device
4. Make changes to storage devices, including the disk where the OS itself is installed (but not the partition[^1] where the OS is installed)
5. Run programs in the background
6. Send data over the network to any IP address, over any port ([Issue 33](https://buttondown.email/laymansguide/archive/lmg-s3-issue-33-port-numbers/))
7. Prevent other programs from doing so ([Issue 34](https://buttondown.email/laymansguide/archive/lmg-s3-issue-34-firewalls/))
8. Install libraries that can be used by other programs
9. Access OS settings and make changes that affect OS operation
10. ... and many more things!

[^1]: I’ll talk about partitions in a future issue, when I move on to hardware devices

## User Account Control

What if a user needs access to some of these permissions (but not all)? Does that mean they need to become an Admin?

Windows, and other OSes as well, usually has some way to give users limited permissions for some tasks. Windows uses User Account Control, which pops up a dialog box to alert the user. If the user gives permission for the app to proceed, then it is able to do so. If it is running on a user account, it can only perform tasks that the user account is allowed to perform. Linux uses the concept of groups; for a user to have permission to access bluetooth, for example, the linux OS often requires the user to be added to the `bluetooth` group in the OS.

**Issue summary:** A laptop app can do practically anything, if it is running through the Administrator/root account. Sandboxing is carried out through permission control.

This is the reason why you should still buy a machine with a desktop operating system if you plan to be doing anything really productive; the sandboxing systems of web and mobile apps ultimately still impose a significant limit on what you can do with the device. This is intentional; it is done for your safety! But if you want your device to do more, you’ll often need to override these “safety limits”, and that is where desktop operating systems come in.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 98: Temporary files

Next issue is going to round off this mini-arc on how different kinds of apps operate. In the process of doing whatever it is they do, apps often generate temporary files that can be safely removed. How does this work for web apps and mobile apps? And for laptop apps?

From there, I’ll expand to talking about how apps store their data on and retrieve their data from the operating system.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
