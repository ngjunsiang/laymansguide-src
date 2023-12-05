Title: Issue 15: Sysadmins and the command line
Date: 2019-03-23 08:00
Tags: 
Category: Season 2
Slug: lmg-s2-issue-15-sysadmins-and-the-command-line
Author: J S Ng
Summary: 

If something’s not working correctly in your operating system, someone has to dig into the settings and configuration, figure out what’s wrong, and resolve the issue. If you have ever been in those shoes, you have been basically doing a sysadmin’s job. (Okay, put away those pitchforks you sysadmin purists and hear me out …)

Every system you have ever interacted with needs to run on a computer, usually hidden away somewhere: point-of-sale systems, advertising screens, email servers, print servers, web servers, … and these systems can start going awry too. Sysadmins, experienced or otherwise, are the ones who fix them. If this system has a screen and a place to plug in a keyboard, fine. But what if it doesn’t?

Before graphical interfaces and the mouse cursor came about, there was a primitive (but no less powerful) interface: the command line.

## The language of the command line

A computer is just a box of chips waiting to do your bidding, and the command line is one way to give it commands (get the name now?) But of course, that means you’ll need to learn its language.

First, some names/terms. You may see the command line also referred to as a **terminal** (Mac/Linux), command prompt (Windows), or shell (also Windows). The differences are technical, they all refer to that window with the pointer waiting for you to enter your commands.

What does a command look like? It can look as simple as:

`touch image.iso`

or as complex as:

`ffmpeg -i input -c:v libx264 -preset slow -crf 22 -x264-params keyint=123:min-keyint=20 -c:a copy output.mkv`

If for whatever reason you have to try to interpret what a command is doing, here’s the one thing all commands have in common: the first word is always the name of a program. The first line is calling the *touch* program, the second line is calling the *ffmpeg* program.

The second thing is that any word starting with `-`, `--`, or `/` (used by Windows) denote options. Like, you know when you go into an app’s settings and change stuff? This is how command lines do the same thing. If you don’t give any options to the command line program, it will use its defaults, just like any other app.

All other words which come after the first word are just options. So let’s try to interpret those two command lines:

`touch image.iso` → Tell the program *touch* to do its thing to the file `image.iso`

`ffmpeg` → Tell the program *ffmpeg* …  
`-i input` → to use the **i**nput file `input` …  
`-c:v libx264` → and use the **v**ideo **c**odec **lib**rary called `x264` …  
`-preset slow` → and the "slow" preset …  
`-crf 22` → and use **c**onstant **r**ate **f**actor 22 …  
`-x264-params keyint=123:min-keyint=20 -c:a copy output.mkv` → okay nevermind, I think you get the idea 😅

It took me years of gradual exposure to various command line programs and their options to know what they can do, and I don’t expect (m)any of you to be heading down that path, but if you ever encounter a command line instruction, I hope it strikes less fear in you than it used to, because now you know how to read it!

## Why do people use command lines?

### Fallback mechanisms

Let me use an analogy:

When you go camping, you sleep in/on a sleeping bag (or air mattress, or hammock, or …) and not a bed, right? When the car breaks down and you don’t have a spare, you cycle or walk. When your school computer blocks you from using filesharing apps, you resort to emailing yourself.

When your usual powerful methods don’t work, you fall back to more primitive methods.

The command line is a fallback for graphical interfaces when they crash. If Windows encounters a problem while starting up (this process is known as **booting up**, we’ll get to this in a future series on hardware), it usually tells you to get a technician to look at it. But in Linux, when the computer encounters a bootup problem, it drops you to a command line so you can at least try to fix the problem. Any time the graphical interface in Linux starts getting glitchy, you can always drop to a terminal (another name for command line, remember?) to figure out what’s wrong. If even the terminal is glitching up, something really bad is happening … (probably a video driver issue, but we haven’t gotten to troubleshooting yet).

### Remote work

The really cool thing about a lot of developer work (including sysadmin work) is that you’re just manipulating text on a screen (after manipulating a lot of ideas in your head first). This is something you can do remotely, over the Internet! There is no reason you need to be physically present where the actual machine is.

Sysadmins of large systems often have to manage multiple servers that may be in another part of the building, or even spread across the world: remote management. A manager works with remote workers by telling them what to do over email/video call, a sysadmin tells her remote servers what to by sending them command line instructions, usually over an encrypted line, because you wouldn’t want these instructions intercepted by a malicious person.

Why don’t they do it through a graphical interface?

I don’t have any single primary reason, but if you ask developers why they prefer command lines, they’ll probably tell you something along the lines of:

- “Who’s going to make that graphical interface? No one, because it’s more work and we’d prefer command line anyway.”
- “I can type commands faster than I can click a mouse.”
- “Sending graphics over the internet takes a few thousand times the bandwidth it takes to send text. The lag is so bad, I’d rather use text commands.”
- “What’s wrong with command lines?”
- “You can save commands into a script file and run them. That makes our work insanely easier. No graphical interface needed!”

I guess it’s something that just has to be discovered through experience ;)

-----

**Issue summary:** A command line is a way of giving commands to the computer in the form of text. An instruction consists of the name of the program to be run, and the options that it needs to use. Command lines provide a fallback mechanism when graphical interfaces break down, and are a much more remote-friendly interface.

Phew, slightly over 1100 words! So this issue is about 40% shorter than the previous :) I know movies and dramas like to make hacker work look all mysterious-like and one popular way is to randomly show some hoodie guy hunched over a command line. May this issue make such things less scary and encourage more people to dabble in it, even if only a little bit.

I intentionally left the juciest bit for the last: “You can save commands into a script file and run them.” Amazingly few people know this! I suspect a big reason people get so jazzed up over AI is an ignorance that many of the use cases they imagine for AI can already be handled by sufficiently complex script files.

I’ll save my fingers the typing and let the Internet provide the stories of automation:

- [A programmer wrote scripts to secretly automate a lot of his job — and email his wife and make a latte (Business Insider)](https://www.businessinsider.sg/programmer-automates-his-job-2015-11/?r=UK)<br/>
Here’s an extreme (and not very nice) example, but look at all the things you can do with just the command line! (But do nicer things of course.)
- [What are some of the most common things you can automate with python? Looking for ideas (Reddit)](https://www.reddit.com/r/learnpython/comments/8uwonh/what_are_some_of_the_most_common_things_you_can/)<br/>
More of what you might expect to be able to do in daily life. If you’ve been procrastinating on picking up Python because you can’t think of a project to do, try this thread for ideas.
- [Automation is fun. Do you have any stories? (Reddit)](https://www.reddit.com/r/sysadmin/comments/779vf5/automation_is_fun_do_you_have_any_stories/)<br/>
A bragging-rights thread, I put this here because the original poster’s story really illustrates why sysadmins love command lines. Which is what this issue is about, right?

I want to talk a little about how this automation is done in the next issue. Again, not a howto, just an explanation of what goes on. And hopefully it helps you see that you don’t actually need AI for many of the problems you face.

## What I’ll be covering next

**Next few issues:** Shell scripts and automation, Libraries, Frameworks

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those ‘\r\n’s in the HTTP request packet [Issue 12]?

(I know I’m taking a while to get to these. I’ll touch on specifications later in this series, but the rest will have to wait until we return to networking and the Internet again, probably.)
