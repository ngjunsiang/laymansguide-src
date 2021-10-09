[**Previously:**](https://buttondown.email/laymansguide/archive/) System VMs provide a set of virtualised hardware that the OS interacts with. Process VMs provide a set of libraries that a program (written in that programming language) interacts with.

If the Java VM lets us write programs that work across multiple Oses, why don’t we write everything in Java then?

Actually a lot of enterprises do! But there are some tradeoffs to make this work.

## What’s bundled

The code required to make a Java program run on every operating system is not simple; somehow all this complexity needs to make its way to the target computer, whether it uses it or not.

Ideally, we have one part: the program you want to distribute, bundled and delivered to the user. The other part, like an adapter (the Java VM), allows your program to work on the target computer.

Up to this point I have given the impression that the Java VM is all that is needed for the adapter to work. This is inaccurate; the Java VM interprets the program instructions (in an intermediate set of instructions called *bytecode*). It still needs a whole set of supporting libraries to enable interfacing with the OS.

The Java VM and these supporting libraries are installed in a software package called the Java Runtime Environment (JRE). If you hear the term “runtime environment”, this is what it refers to: the program plus the libraries it needs to run.

If you want to write Java programs, you’ll need more than the JRE though. you will need supporting tools especially for debugging, and these are provided in the Java Development Kit (JDK). this is not only true for Java, but for many other languages as well; if you are getting into programming, and asked to pick a download, you usually want the one that says “development kit”.

# Tradeoffs in distribution

If you want to keep the software bundle size small, you’ll have to ask the user to install the JRE separately (about ~80MB downloaded, more when installed). If you don’t want your users to face that hassle, you’ll have to take on the work of bundling the required libraries into your program yourself. Are you going to bundle libraries for all targeted OSes, or just for one particular platform? The more you bundle the larger the size ...

Nobody said multiplatform support is easy!

## The legalese

Java is free to use—but only on a personal basis. Once you intend to distribute your program, and maybe even make money, the issue of licensing rears its head.

Java was originally created at Sun Microsystems in 1995, but was acquired by Oracle in 2010. They do enforce their licensing pretty strictly, so be prepared to pay for the convenience!

## Java and open-source

If the only way to distribute programs with multiplatform support is to pay a licensing fee, Java would see much lower takeup, which would hurt long-term profits ... so a big portion of the Java core is open-sourced as [OpenJDK](https://openjdk.java.net/). This is free to use and extend, and many businesses have been successfully releasing software based on it. But it si going to be a lot more work carrying out testing and writing code for features which are not provided.

On top of OpenJDK, Oracle JDK—Oracle’s commercial release of the JDK—adds some proprietary code, plus lots of enterprise support and testing. In general you’re going to have a much easier time writing your code with Oracle JDK instead of OpenJDK—that is how Oracle makes money!

If you just want to get familiar with the language, or are working on a personal project, OpenJDK lets you do so for free, legally. If you are a corporation trying to get your engineers to write code that runs on multiple platforms so as to simplify your systems, Oracle JDK helps you to save time doing that, for a fee.

It’s the best of both worlds.

**Issue summary:** The Java Runtime Environment (JRE) bundles the Java VM and supporting libraries. The JRE has to be installed on the user’s system for Java programs to work, unless the program bundles the supporting libraries. Solo programmers can start programming with OpenJDK for free with fewer features and less support, while commercial companies can license Oracle JDK for better support and features.

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 152: Getting started with programming

Hold on, I thought—

Nah, Layman’s Guide to Computing has not suddenly switched to being a Guide to Programming! But we are still on the topic of the cloud and the history of commercial computing. Where I last stopped, I was talking about how co-hosting transitioned to virtual-hardware VM rental to containerisation, before a short segue into process virtualisation and the Java VM (this issue).

Before I continue further on this to explain how we got to the current state of the cloud, there’s one thing that the average layperson would not be familiar with, and which I need to talk about:

Why is it so difficult to *do* programming, even with experience? Yes, *do* programming, not merely learn it!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- ~~a good reason developers write code and give it away for free online? [Issue 21]~~
- OpenType? And what are fonts anyway? [Issue 42]
