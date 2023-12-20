Title: Issue 19: Version control and git
Date: 2019-04-20 08:00
Tags: 
Category: Season 02
Slug: issue019
Author: J S Ng
Summary: A **version control system** (VCS) tracks changes to documents. Git is a version control system for source code. Keeping a change history enables a VCS to roll back code in a previous point in time. A change history can also be used in areas other than coding.
Modified: 2019-04-20 08:00

Have you ever worked on a large document with a team of people before? If you have, did it go well? Did people get along and not get into conflict with each other over conflicting ideas or changes? If it did, please drop me an email and let me know! In my experience it is so frustrating and I have difficulty seeing how it can be done without some kind of standardised, automated process for keeping everyone updated.

In the past, when documents were still mostly managed manually (before the Internet happened), important documents used to be in a file for everyone to reference. Maybe there were multiple copies for VIPs. Whenever that document got updated, it had to have a **change log** attached to say what had changed and when. You still see this sometimes today, in some reference documents, and in software updates. The idea behind being able to see the *history* of a document—a record of how it has changed over time—is an idea that has survived and been passed down to each generation of makers. We often refer to such inherited ideas as wisdom, and the modern form of this idea is known as **version control**.

## Version control in software today

Some examples you may or may not be familiar with:

1. Google Docs/Sheets/Slides has a line beside the document title, “All changes saved in Drive”. That is [a link that shows you the **version history**](https://support.google.com/docs/answer/190843?co=GENIE.Platform%3DDesktop&hl=en) (also known as **change history**) of the document.
2. Microsoft Word [has something similar](https://support.office.com/en-us/article/view-the-version-history-of-an-item-or-file-in-a-list-or-library-53262060-5092-424d-a50b-c798b0ec32b1).
3. [Dropbox keeps a file version history](https://help.dropbox.com/security/version-history-overview) (for 30 days on the free plan) so that you can recover deleted files, or restore a file to an earlier state. Each time you change a file inside Dropbox but keep the filename the same, the file version history is updated.
4. Wikipedia keeps a change history of every article, as well as the discussion page for that article. [Here’s the change history of the Wikipedia page on Git](https://en.wikipedia.org/w/index.php?title=Git&action=history).

This is version control simplified for the everyday person, and if you were already aware of these features, you might already have benefited from being able to roll back a document you accidentally overwrote, or undeleting something you thought you no longer needed.

But what about software, which often consists of more than one file? The addition of a significant feature may involve changes in more than one file, and those changes must be considered together to make any sense of it. How do programmers do that?

## Git: modern version control

The modern-day tool which (almost) all developers have standardised on is called git, and it was [made in 2005](https://en.wikipedia.org/wiki/Git#History). Its name is Git, and it was written by Linus Torvalds, the same man who first began working on the Linux kernel.

Git tracks changes across _multiple files_. For example, if you added a new About page to your project, it may involve adding a new file about.html (the actual content), updating app.py (to create a new route so people can access the URL), and adding a new line to the changelog (so other members of your team have an easy-to-read changelog). You inform the git server (we covered clients and servers in [Issue 7]({filename}/season01/issue007/issue007.md)) that you have changed those 3 files by creating a **commit**. Git can prepare those commits for you, and they look like this:

![A commit on Github]({attach}/season02/issue019/issue019_01.png)  
*A git commit on Github. Yup, this newsletter is also a project on Github.*    

The screenshot above makes it look fancy, but a commit is really just a simple text file that records the changes of the commit.

```
    Issue 014 updates

--- a/season02/issue014/issue014.md
+++ b/season02/issue014/issue014.md
@@ -57,7 +57,7 @@ Beyond writing apps, code is also written for many other purposes. I outline som
 Yes, code can be written to process data! This is one of the coolest uses of software, because manually searching through data and performing calculations is tedious, and computers can do it so much faster.

 **System administration**
-A sysadmin’s job is to make sure a server, or group of servers, remain up and running. I might detail the kinds of trouble a server can get up to once I have enough stories to tell, but I think [Rachel](https://rachelbythebay.com/w/) tells much more interesting stories about those, albeit with lots of technical detail.
+A sysadmin’s job is to make sure a server, or group of servers, remain up and running. I might detail the kinds of trouble a server can get up to once I have enough stories to tell, but I think [Rachel tells much more interesting stories](https://rachelbythebay.com/w/) about those, albeit with lots of technical detail.

 A sysadmin might have to write code to automate processes, to troubleshoot, to create new users, to manage files, and for many other reasons. They work primarily in the command line, because most system administration tools are written as commandline tools, although sometimes a user interface might be created to make a popular tool easier to use.
```

This is a short snippet of a commit. It records some text before and after the change so it’s easy to place the change, and then records both the old version (prefixed with a -) and the new version (prefixed with a +).

## Version control systems

So … if I want to see how the code looked at a particular point in time, I have to go through all the commits and mentally imagine the old version in my head?

Well, no. That’s what we have computers for :) Git (and any decent version control system really) can handle that for you to show you the code before/after the commit(s). It can also merge commits, roll back the code to a particular point in time (i.e. undo commits), and more.

If you’ve ever thought “hmm, when did this part change? I don’t remember it looking like this …”, a change history, coupled with the right tools, makes it easy for you to know when that happened. But that means setting up a VCS (such as git), which requires maintenance.

If you don’t want your code being online, git can be installed on your own computer, but the far more popular way that developers use it is in the cloud. And the most popular platform for code today is [Github](https://github.com/about). It’s so popular that Microsoft, realising just [how much of their code is on Github](https://github.com/Microsoft), decided [to buy Github](https://blogs.microsoft.com/blog/2018/06/04/microsoft-github-empowering-developers/).

When you create a Github account, you get a repository that you can put your code in. This repository is managed by a git server that you can push commits to, and pull changes from. You get complete change history for your code that is uploaded (here’s the [change history for this newsletter](https://github.com/ngjunsiang/laymansguide/commits/release)). You don’t have the same level of control you would over a git server that you run yourself, but it saves you much more time and hassle.

## Using a VCS for non-code purposes

Your eyes are probably glazing over at this point—just another techie gushing about *one* particular technology, right? Git may seem really cool for code, but it can’t be used for anything else … well actually it can!

People have tried to use git for writing academic papers. Here’s [a workflow for writing papers in LaTeX](https://medium.com/@rvprasad/a-git-workflow-for-writing-papers-in-latex-4cfb31be4b06). [Here’s another one](https://sites.duke.edu/stochastically/2014/07/23/using-git-to-write-papers/). [Writers use it too](https://joebuhlig.com/writing-with-github/). [So can designers](https://medium.com/@dfosco/git-for-designers-856c434716e).

The cool part is not that they are all using git. Git works, but primarily for text-based mediums. But increasingly, people are seeing the value of a change history, and are trying to apply it in ways that make sense. Designers certainly are catching on. [Versions](https://versions.sympli.io/) and [Abstract](https://www.abstract.com/) are two platforms that try to apply the concept in a way that makes sense for designers.

**Issue summary:** A **version control system** (VCS) tracks changes to documents. Git is a version control system for source code. Keeping a change history enables a VCS to roll back code in a previous point in time. A change history can also be used in areas other than coding.

-----

Phew! I thought this was going to be short, but I was sorely wrong. In fact, I’m not completely done with the issue on version control yet—I realised as I was writing that it would make more sense to talk about testing first.

This is the first big idea I’ve introduced this season: version control. Knowing about version control and not being able to introduce it into workflows that would really benefit from it is frustrating. If you use Google Docs, Dropbox, or anything that has simplified version control, and you’ve asked yourself questions that can actually be resolved by checking a change history, do try it out and get familiar with the idea!

How can version control improve the way you work? If you’ve got an idea for applying version control where no version control has boldly gone before, hit reply and let me know :)

To wrap up, I realised that this issue took me 1.5 hrs to write. That’s not what I promised when I started this newsletter, that each issue should be short and digestible and possible for me to write in an hour. I’ll look at how to further split up future issues to keep to this promise. If you do actually prefer longer issues, drop me an email and let me know!

## What I’ll be covering next

**Next few issues:** Testing, and how git stops people from wanting to kill each other

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those '\r\n's in the HTTP request packet [Issue 12,17]?
