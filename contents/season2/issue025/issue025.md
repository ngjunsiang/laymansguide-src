Title: Issue 25: Text Editors and Integrated Development Environments
Date: 2019-06-01 08:00
Tags: 
Category: Season 2
Slug: lmg-s2-issue-25-text-editors-and-integrated
Author: J S Ng
Summary: 

Last week, I introduced issue trackers, which are software tools that developers use to keep track of problems and issues with their software. Issue trackers are usually places that users can submit bug reports to help out the developers in tracking down a bug.

In the second-last issue of this season, I'm going to do a little detour to talk about what developers use to edit their code. Yeah, the actual software they type their code into.

## Editor: something used to edit text

Newspaper editors, book editors, photo editors … nope we’re not talking about those. Text editors are software that is used to edit text. The simplest example you know of is probably Notepad. On the other end of the scale you can have really fancy editors like [Sublime Text](https://www.sublimetext.com/) or [Notepad++](https://notepad-plus-plus.org/), or [Atom](https://atom.io/).


![Sublime Text]({attach}issue025_01.png)
<small>Sublime Text</small>


Every programmer has their own favourite. They can get prickly and defensive about their text editors of choice, so be careful what you say about their preferred text editors.


![Notepad++]({attach}issue025_02.png)
<small>Notepad++</small>



![Github Atom]({attach}issue025_03.png)
<small>Github Atom</small>


Text editors do what is written on the box: they let you edit text. Often (but not always), that means code. It may have nice features that help you autocomplete words, or close your brackets for you, or highlight keywords to make the code easier to read, but it doesn’t help you think about the flow of logic in your code. For that you need …

## IDE: an Integrated Development Environment

An IDE is rather different. Yes, it probably has a big window for you to edit your code. But it has to do much more. It is called a **development environment** because it lets developers *explore* their code. An IDE can run your code, show you the values of the variables within your code in real-time, or let you pause the code at a point so you can see what the program is doing before it exits or crashes. This helps greatly with the debugging process.


![Spyder]({attach}issue025_04.png)
<small>Spyder IDE, showing its object inspector (for checking variables) and built-in console (where the code is run)</small>


An IDE can test the performance of your code to let you know where it is running slowly (a process known as **profiling**).


![Netbeans]({attach}issue025_05.png)
<small>Netbeans IDE showing its profiler at work</small>


An IDE integrates many tools into one software package so you can do your work mostly without having to switch around windows.

**Issue summary:** A text editor helps programmers to edit their code. An IDE (integrated development environment) helps programmers to see what’s going on in their code, test their code’s performance, and provide almost all the necessary tools in one package.

-----

This is a short issue that I wanted to write to answer questions I get on “where to start learning programming”? The usual answer they get is books and websites teaching you how to code, but I contend that the first piece of software you use is critically more important.

In every hobby or pursuit, the tools, gear, and equipment determine the pleasure you get out of it, and likely determine whether you continue to stick with it. Anyone beginning to learn programming should start with a good text editor, and gradually move on to an IDE if they’re working with complex code.

I will save the recommendations for other places; I don’t think a newsletter is appropriate for that. The best text editor for you is going to depend on your use case, your OS, your machine (laptop or workstation), and potentially many other factors.

## What I’ll be covering next

**Next issue:** ???

I haven’t quite decided what I’ll wrap up this season with. I said in Issue 14 that I started this season to help people understand what developers do, to build up their picture of Computing before they start trying to learn programming. Maybe I’ll do a short introduction to operating systems, or maybe we’ll talk about package distribution :) We’ll see next week!

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n's in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
