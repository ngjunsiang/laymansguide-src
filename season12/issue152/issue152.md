[**Previously:**](https://buttondown.email/laymansguide/archive/) The Java Runtime Environment (JRE) bundles the Java VM and supporting libraries. The JRE has to be installed on the user’s system for Java programs to work, unless the program bundles the supporting libraries. Solo programmers can start programming with OpenJDK for free with fewer features and less support, while commercial companies can license Oracle JDK for better support and features.

So you started taking up programming. Maybe you went to a class, where everything was set up for you and you didn’t have to worry about installing and configuring necessary software. Or you took an online course, where step-by-step instructions were provided and you mostly didn’t have to spend time scratching your head. That’s how it should be; you paid to learn *programming*, not to learn how to configure a software development environment.

Once you actually have to start writing code though …

## Setting up a development environment

Let’s suppose you are writing code for a web application. You start by installing the software for the compiler/interpreter program, which either executes your code directly or compiles it into an executable binary ([Issue 54](https://buttondown.email/laymansguide/archive/lmg-s5-issue-54-compiling-programming-code-into/)).

Now you begin writing your code. Along the way, you begin to install various libraries ([Issue 17](https://buttondown.email/laymansguide/archive/lmg-s2-issue-17-libraries/)) and frameworks ([Issue 18](https://buttondown.email/laymansguide/archive/lmg-s2-issue-18-frameworks/)) that your code relies on. These are provided in things called **packages**, which are basically zipped files containing all the files and metadata for the library/framework. You install these packages using another program, called a **package manager**, through the command line terminal ([Issue 15](https://buttondown.email/laymansguide/archive/lmg-s2-issue-15-sysadmins-and-the-command-line/)).

You write more code. And one day … you’re done! The real pain has just begun!

## Deploying code

Thus far, you have been programming on your own laptop. But your laptop can’t handle a full webserver load once people start using your app, so you wisely decided to lease a virtual machine (VM: see [Issue 147](https://buttondown.email/laymansguide/archive/lmg-s12-issue-147-operating-systems-on-virtual/)) from a cloud provider instead. You boot up the VM, it goes through its bootup process ([Issue 112](https://buttondown.email/laymansguide/archive/lmg-s9-issue-112-bootstrapping-into-existence/)), and finally completes. You are greeted with a familiar command line, the caret position blinking cheerfully.

How are you going to get your code on that machine?

Maybe you set up a code repository ([Issue 19](https://buttondown.email/laymansguide/archive/lmg-s2-issue-19-version-control-and-git/)) on another server, and then download your code onto the VM with some commands.

Maybe you decide to turn your app into a package instead: you add more files and some metadata to the app, write software instructions (more code!) for which files to copy where, and how to configure everything, and then pack it up. You install yet more software (called **build tools**) to help you automate this part. Then you set up another file server, upload the package onto it from your laptop, download it from the VM, and install it on the VM using the package manager.

You test it, and after many hours of cursing, confused pacing and mumbling, and much hair-tearing, it finally works. Phew!

## Expanding the app

Unfortunately, the tiny toy server that you used to test your web app doesn’t hold up to real-world loads. You’ll need to put the app behind a Real™ web server; as more and more users use it, you may even need to deploy your app to multiple servers to handle the load, all managed by a **load balancer**. The balancer receives the web requests ([Issue 9](https://buttondown.email/laymansguide/archive/lmg-issue-9-how-do-i-make-an-http-request/)), decides which of the multiple servers has the lowest load so far, and directs the request to it so it can serve a web response ([Issue 8](https://buttondown.email/laymansguide/archive/lmg-issue-8-http-error-codeshow-does-a-server-let/)).

Does that mean you have to do the above all over again?!

**Issue summary:** Actually making a web application requires you to set up lots of supporting software and carry out lots of steps to create a suitable app environment.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 153: Using the cloud

I hope this issue adequately describes the problem that the cloud attempted to resolve! When people talk about “using the cloud”, what is that actually like?

Next issue, I’ll give a peek. Short issue guaranteed.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]
