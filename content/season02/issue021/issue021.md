Title: Issue 21: Forking and merging
Date: 2019-05-04 08:00
Tags: 
Category: Season 02
Slug: issue021
Author: J S Ng
Summary: 
Modified: 2019-05-04 08:00

So far I have been describing things as though only one developer was working on a project. What happens when two developers are involved? Any kind of collaboration between people working on one thing usually leads to issues coordinating their efforts. How do developers manage this?

Usually, by not working on the same part of the code at the same time. But in addition to that, developers have also come up with some good practices and work philosophies to minimise the friction involved in working together.

In this issue, I want to introduce **forking** and **merging**, key ideas behind version control systems and how they keep developers sane.

## How developers suggest changes

One really cool thing about developers is how much they love to share their code online. When you see someone else’s code online and you can see improvements you’d love to make to the code, what can you do?

The typical non-developer way is to email them politely, spend a long hour thinking about what to write to explain your point of view, and ask them if they can consider incorporating your proposed change to the code which looks like [attachment].

The typical developer way is to fork their **repository** and make a pull request (usually after dropping them a quick message to ask first). The repository is where they store their code, and this repository is managed by a [version control system (VCS)](https://hackernoon.com/top-10-version-control-systems-4d314cf7adea), typically git.

## Forking: making your own (copy of the) world

**Forking**, simply speaking, is making a copy of their code. You need a complete copy of their code so that you can run the app and test the changes you make. It’s called a fork because it’s like coming to a fork in the path of coding. Now there are two paths: the original path, and the path you are about to create.

You could do it stealthily (just copy and paste!), but it’s best not to. Instead, [you should do it through git](https://help.github.com/en/articles/fork-a-repo). This informs the code owner that someone has forked their repository and is possibly working on changes to it. It also makes it easy for you to pull any subsequent changes the code owner has made to the code and merge it with your code automatically, so you can test your changes with the latest copy of the code. And more importantly, it allows git to help you with merging your code back into the main codepath (more on this later).

Forking somebody’s project is usually a compliment. It means you find their work interesting enough to want to fork it and work on it!

## Pull requests: joining the main codepath again

It’s no fun just working on your own copy of the code. The best part is incorporating your changes back into the main codepath so others can enjoy your work too.

In git, this means **merging**. When two codepaths are merged, git checks the commits of each codepath (see why version control is so important?), and automagically merges the commits into one path. In the process, it highlights any conflicts (when two commits change the same part of the code) which require human intervention—usually by the owner of the main codepath.

You know how much it drives you nuts when you arrange your stuff a certain way, and the person sharing your table rearranges it. Or when you are working on something and you have your tools set up a certain way, and someone else working on it with you changes the way things are done.

Git forking and merging allows contributions to take place in a saner and more controlled manner. But it does not eliminate the need for discussion and coordination; it just makes the collaboration much more sane and less tedious.

# Github: the social network + collaboration platform of developers

Coordinating all this development work offline involves lots of emails and messages, and an online platform helps to ease that problem. Out of many such competing platforms, one particular platform has become the most talked-about: [Github](https://github.com/about), introduced in Issue 19.

Github is like multiplayer git. It lets you create your own account, create your own projects (each one with its own git repository running on Github’s machines), lets you browse other people’s projects, comment on them, report issues and request features, and also fork their repository. Many developers use it to show the code they have been working on, to coordinate efforts for online projects, and to build code that is used around the world.

Why would developers want to do this, to make things for free and let others benefit from it and no cost? The history of open source development is interesting and important to the future of the Internet, but it’s far more than I can cover in one issue—perhaps I’ll do that in a future season.

**Issue summary:** In git, forking a repository creates a copy of it for you to work on. Merging a repository with the original combines the commits from both so that they become one repository again. Conflicts arising from commits from both codepaths that affect the same part of the code will need to be resolved manually. Developers do most of this forking and merging in Github, an online platform for working on and talking about code.

-----

I’ve simplified a *huge* portion of how git works, which I think isn’t important to know about for laypeople, so as to focus on the key features of git and how it makes collaboration much saner for developers.

Do you use any online platforms for collaborating with others? If your work is primarily text-based and you would like a way to work on it more easily with people, Creating a git repository on Github is something you might want to try. It is a little less automated than Dropbox, but it gives you more control, especially when you need to roll back changes.

Sometimes, forking and merging can go bad.  For example, two codepaths could change parts of the same code so much that it is more effort than it is worth to combine the changes back again. Or sometime, legal issues stand in the way. In the next issue, I want to talk about one way that developers usually set things up to make it as easy as possible to edit code without breaking anything. It is called Continuous Integration.

## What I’ll be covering next

**Next issue:** Continuous Integration: how to not break software while working on it

**Sometime in the future:** What is/are:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n's in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
