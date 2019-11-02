In the past 12 issues I’ve talked a bit about different kinds of programs ([web, desktop, mobile, …](https://buttondown.email/laymansguide/archive/lmg-s2-issue-14-what-do-developers-do/)), different kinds of code ([frontend, backend](https://buttondown.email/laymansguide/archive/lmg-s2-issue-14-what-do-developers-do/)), tools that programmers use while programming ([command line](https://buttondown.email/laymansguide/archive/lmg-s2-issue-15-sysadmins-and-the-command-line/), [libraries](https://buttondown.email/laymansguide/archive/lmg-s2-issue-17-libraries/) and [frameworks](https://buttondown.email/laymansguide/archive/lmg-s2-issue-18-frameworks/), [version control](https://buttondown.email/laymansguide/archive/lmg-s2-issue-19-version-control-and-git/), [bug/issue trackers](https://buttondown.email/laymansguide/archive/lmg-s2-issue-24-issue-trackers-bug/), [text editors and integrated development environments](https://buttondown.email/laymansguide/archive/lmg-s2-issue-25-text-editors-and-integrated/)), and ideas they use to work more efficiently ([specifications](https://buttondown.email/laymansguide/archive/lmg-s2-issue-23-specifications-in-software/), [testing](https://buttondown.email/laymansguide/archive/lmg-s2-issue-20-testing/), [continuous integration](https://buttondown.email/laymansguide/archive/lmg-s2-issue-22-continuous-integration-in-software/)).

To wrap this up, let’s answer one final question: how do they actually get their code out to the rest of the world?

## Mobile apps

Let’s start with the easiest: mobile apps, of course, get published to the app store ([Apple App Store](https://www.apple.com/sg/ios/app-store/), or [Google Play](https://play.google.com/store), for most phones). Programmers could, of course, encourage people to enable installation of third-party apps and ask them to download and open an installation file … but how many people are going to do that?

The process of putting an app onto the app store is known as **publishing**. This often involves lots of steps—see [Google Play’s publishing process](https://developer.android.com/studio/publish)—including adding images and writing for the app’s page.

Before a program can be uploaded, a lot of extra information is needed by the app store: the app author’s name and particulars, the version number, minimum OS requirements (e.g. some apps won’t work on Android versions older than 4.4), and so on. The app store may also need a manifest, a list of files in the app. The process of adding all this information and organising the files into something that can be uploaded to an app store is known as **packaging**.

How is code for other platforms packaged and released? That depends, really, on the community.

## Linux: software repositories

On Linux, in the old days, you had to download the source code, compile it into an application (*self-note: this needs explaining in a future issue*), and install updates for each application individually … this soon became a gargantuan effort for a user. Then some smart people got together and thought: why don’t we make a list of applications, and where they can be found? And then automate it so that a computer can download the source code and compile it automatically? Or, even better, have a central place containing compiled applications that can be downloaded, ready to use? And thus the software repository was born. (don’t confuse this with a code repository, which I introduced in [Issue 19](https://buttondown.email/laymansguide/archive/lmg-s2-issue-19-version-control-and-git/).)

Each Linux distribution ([Ubuntu](https://www.ubuntu.com/), [GNOME](https://www.gnome.org/), [Linux Mint](https://linuxmint.com/) are some of the more popular ones) has its own software repositories (also known as **repos**). These repositories contain the most important or popular applications that their users need, and are updated and maintained regularly by **maintainers**, developers who take on the role of testing code for compatibility. The maintainers often have to make changes, some little and some big, for the applications to run well with their distribution (also known as **distro**).

Linux distros will often have multiple repositories to organise the huge list of applications available, and users can configure which repositories they want to use. They can edit the list of repositories directly, but most users will use a **package manager**, a program that helps users search for, install, and update the applications on their computer. Many of these package managers are command line applications, but there are graphical package managers available as well.

## Plugins: it depends …

Really popular software that allows users to write and release their own plugins will often also have a way for users to search for them. For instance, Wordpress has a Plugins page for Wordpress users to add plugins to their Wordpress blog. Depending on what kind of plugins you are writing, the release process will vary widely. Sometimes this plugin repository is run by a community, sometimes it is run by the application developer, and sometimes it is run by a heroic volunteer, so … it depends :)

## Libraries: package repositories

If you are learning a programming language, chances are you will have to use at least one third-party library. The easiest way to find them is with a package repository. These are the most popular package/gem repositories for the most popular programming languages:

- Python: [PyPI](https://pypi.org/)
- Ruby: [RubyGem](https://rubygems.org/)
- NodeJS: [npm](https://www.npmjs.com/)
- Javascript: uhh, wow … there’s just so many specialised ones and no single central repository. But [yarn](https://yarnpkg.com/en/) is an up-and-rising one

**Issue summary:** A developer can simply put up a download on a webpage and hope people download it and figure out how to get the app on their devices. But often, the more popular way is to publish the app to a repository (also known as an app store, for mobile devices). Before this can be done, the code or application needs to be packaged according to the requirements of the repository.

-----

It’s the end of Season 2 of Layman’s Guide. I hope the programmer’s world looks a little less murky now, even if it looks a lot more complex!

Many programming courses tell their students that they can just jump into programming without worrying about all these. And they often set up their courses minimally, introducing Github or a package repository on occasion when they can’t avoid it. But for the most part, they don’t explain what these parts of the programmer’s world are and how to use them.

To me, that’s like bringing a friend from overseas to your country and not explaining how the transportation system works, how to buy things, what the most popular methods of payment are, how to cross the road … you can kind of hole yourself up at home and maybe venture out to the convenience store down the street, but what fun is that?

These are tools and ideas you can learn and use separately from programming (I’m using Github to get version control on Layman’s Guide, in fact), and you can get really good with them while knowing very minimal programming. And if you learned anything from Season 2 that really rocked your world, gave you an idea for how to improve things, or changed your view of the way things are done, please drop me an email and let me know :)

## What I’ll be covering next

**Next season:** Data? Cloud?

Pick your own adventure! Let me know what you’d like me to write about next:

**Data**: different types of data (text, images, video, code). Why JPGs are so small and BMPs are so huge and PNGs are kinda in-between. Why video files are so huge and so difficult to compress. How do cloud companies prevent losing data when a hard disk goes kaput? Things like that.

**Cloud**: What happens to all the images I upload on Instagram? How does data actually travel from wherever it is to my laptop or smartphone? How do people actually start making their programs use the cloud? Things like that.

I’ll take another break next weekend to get Season 3 hashed out. Expect the first issue end-June!

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
- compiling code into an application [Issue 26]?
