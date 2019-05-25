Last week, we talked about how developers plan out a project and describe specifically what needs to be done: they write out a specification, and then they write code to make their app meet the specification. Specifications are also used to standardise the way apps communicate, such as they way to report time.

So what happens when apps and programs do not follow the specification?

## Bugs, bugs, and more bugs

There’s a reason for it, and that reason is usually a bug. A bug is a mistake in the software that causes it to not follow the specification. Sometimes it’s a little typo, sometimes it’s a logic error, sometimes it’s running code causing a computer to run out of resources (usually memory), sometimes a [library (Issue 17)](https://buttondown.email/laymansguide/archive/lmg-s2-issue-17-libraries/) you rely on has changed, sometimes it’s just way-too-complex code that nobody can fully figure out … and often, you won’t know until you have spent enough time investigating it.

Software everywhere is full of bugs. They are like bacteria; you can kill them but there are always more!

## Why are they called bugs anyway?

In the early days of electromechanical computers, which carried out computation through a mix of electrical and mechanical parts, problems that arose during the computer’s operation were not always caused by wrong instructions sent to the computer. In 1946, operators of the Harvard Mark II encountered an error that was eventually traced to a moth trapped in a relay. Bug hunting then was literal; today it is figurative, but the term has stuck.

<div style="text-align:center">
![A dead moth taped to a page](https://github.com/ngjunsiang/laymansguide/blob/master/season2/issue024/issue024_04.jpg?raw=true)<br />
A page from the Harvard Mark II electromechanical computer's log, featuring a dead moth that was removed from the device. [Source: Wikipedia](https://en.wikipedia.org/wiki/Software_bug)
</div>

## How do developers keep track of so many bugs?

This refrain should start to sound familiar … they do so with the help of machines :)

Software that helps to keep track of bugs are known as bug trackers. Today, when problems with software can sometimes go beyond bugs, such software may also be known as issue trackers.

Such features may also come with other software or services; Github has a built-in issue tracker.

<div style="text-align:center">
![Github’s issue tracker](https://github.com/ngjunsiang/laymansguide/blob/master/season2/issue024/issue024_01.png?raw=true)
Github’s issue tracker. From Kenneth Reitz’s `requests` package.
</div>

This is where developers working on a piece of software can report bugs or issues they discovered. Often, these reports also come from users of the software.

Through the issue created in the issue tracker, developers can communicate with the user who reported the bug, ask for more information, clarify uses of the software, assign the problem to other developers, or close the issue if it is resolved.

<div style="text-align:center">
![An issue in Github’s issue tracker](https://github.com/ngjunsiang/laymansguide/blob/master/season2/issue024/issue024_02.png?raw=true)<br />
What an issue in Github looks like. From Kenneth Reitz’s `requests` package.
</div>

Projects will often have a contributing guideline to help users understand how best to write a good bug report. Reading and understanding a bug report can be really trying, especially if it is unclear or does not provide enough information, and this can make the debugging work of developers an emotional drain.

It is considered polite to read the project intro and contributing guidelines to understand how the project is being managed and how to write a helpful bug report.

<div style="text-align:center">
![Contribution guidelines for requests](https://github.com/ngjunsiang/laymansguide/blob/master/season2/issue024/issue024_03.png?raw=true)<br />
Contributing guidelines for Kenneth Reitz’s `requests` package.
</div>

Issue trackers are never empty. Popular software gets lots of attention from users, who will use it in all kinds of ways not considered or intended by the developers, so there is always something to be worked on!

If you found a bug in a piece of software you use, and don’t know where or how to inform the developers, try searching to see if it has a place to submit bug reports or issues. Most active projects do, and their issue trackers are often easier to find than their email addresses :)

**Issue summary:** A bug tracker, or issue tracker, is where users can submit problems they encounter with the software. To submit a helpful issue, users should understand the project’s philosophy and purpose, and read the contributing guidelines.

<hr/>

This is a short one, and one I’ve been waiting to write. So many people don’t know that some of the software they use every day have issue trackers, and they can contribute to the healthy development of their favourite software by helping to submit issues they encounter.

How is your workplace keeping track of issues raised by staff? Are they doing it manually in a document? Would an issue tracker help make this job easier?

Next week, I’ll try to answer a question I sometimes get: why do developers like Notepad so much? (They don’t! Just because it is all text does not make it the same as Notepad!) We’ll talk about the kind of editing tools that developers use.

## What I’ll be covering next

**Next issue:** Editors and IDEs: what’s the difference?

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
