[**Previously:**](https://buttondown.email/laymansguide/archive/) Meltdown and Spectre require the programs executing them to have access to kernel memory space. Kernel address isolation attempts to prevent the program from even having access to the kernel address space in the first place. TLB flushing changes the virtual-to-physical memory mapping, disrupting Spectre’s reliance on a consistent virtual-to-physical memory mapping.

One question that makes sense to ask is: if the operating system is supposed to keep the memory used by each program separate, then how is one program able to access the memory of another program? How would a program trying to mount a Meltdown or Spectre attack be able to read the memory of any other program, let alone the operating system?

Let’s face it: it is impossible to completely separate programs from each other. Many programs need to communicate with each other; antivirus software needs to be able to scan the addresses accessed by your web browser for harmful links, Office software needs to be able to send data to each other especially for features like Mail Merge, and of course your task manager has to know how much resources every app is using. So that it can show you this:

![Screenshot of task manager in Windows 10, showing shared memory usage]({attach}issue065_01.png)<br />
<small>Task Manager in Windows 10<br />
You can reveal the shared memory column by right-clicking on the column labels and then “Select Columns”.</small>

or this:

![Screenshot of system monitor in KDE, showing shared memory usage]({attach}issue065_02.png)<br />
<small>System Monitor in KDE (Linux).</small>

What is this shared memory?

## Private memory

The memory I talked about earlier, which every software application has, is used to store various things. It is used to store temporary information, such as unsaved data, application settings, graphics resources (every icon and image shown in the application has to come from somewhere …), but most important, libraries and other functions ([Issue 17]({filename}/season2/issue017/issue017.md

Very few software developers will write every single bit of code used by their program; often, they will use software libraries written by others to provide specialised functions (e.g. encrypting your data, or accessing a database). When program code is compiled into CPU instructions ([Issue 54]({filename}/season5/issue054/issue054.md

That makes the program really huge, doesn’t it? Yes, it does; it is one reason (but not the main reason) that mobile apps, especially Android apps, [have become so bloated](https://trevore.com/post/app-sizes-are-out-of-control/) over the last half-decade or so. But I digress.

## Shared memory

At some point, you start to realise that many of these apps need to use a set of identical functions: at the most basic level, requesting and managing memory, requesting file access, sending data over a network, …, and up to libraries for resizing images, and so on.

It doesn’t make sense for each app to have to bundle their own libraries for that! So the OS actually provides a set of common libraries that applications compiled for that OS can use. Each operating system bundles its own libraries for applications to use; this is one reason why applications compiled for Windows wont work on OSX or Linux, and vice-versa. That also means that these libraries have to be loaded into a part of memory that is accessible to all applications. These shared libraries thus go into **shared memory space**.

What else? Shared libraries can’t be taking up so much space by themselves, they’re just instructions …

Let’s try to find out what else is sitting in there.

## Investigating memory details

On Windows, I’m going to need more specialised tools. I’ve only got an hour; let’s try something else.

Ah! System Monitor actually reveals more details about how an application uses memory. Let’s investigate the top few processes using the most memory.

Here’s Firefox:

![Screenshot of detailed memory usage in Firefox on KDE]({attach}issue065_03.png)<br />
<small>Firefox detailed memory usage in KDE (Linux).</small>

Oops, too much detail. Heres the gist:

1. Firefox uses about 450 MB for its own stuff in private memory, in a place called the heap.
2. To communicate with other processes, it uses about 10 MB privately, and 82 MB shared with other processes (it does so through /SYSV00000000, which is deleted when not in use)  
3. It has loaded one of its core libraries, `libxul.so` (almost all libraries start with the prefix `lib`) in shared space. This core library is shared with other Mozilla applications, such as its Thunderbird email client, so it makes sense to put it mostly in shared memory.
4. It uses a small amount of space for caching things (startup code, its own scripts, etc)
5. It uses some shared memory to communicate with other processes. (The acronym `IPC` in this context usually refers to **inter-process communication**.) This can be for playing audio/video (it has to communicate with the audio/video drivers), or loading content that has to be processed through plugins (used to be Flash content in the past, now it can be other things).

Hmm, interesting. Let’s try to find something more illuminating to wrap up this season with.

## How is shared memory used?

I do my newsletter writing mainly in an app called Atom, made by Github. Atom runs on a platform called Electron (atom … electron … get it?). Electron is a Github project that allows developers to write desktop/laptop apps in Javascript, traditionally the language of web scripting.

In system monitor, I can see an app named atom, and one named electron. Let’s inspect them both.

![Screenshot of detailed memory usage for electron on KDE]({attach}issue065_04.png)<br />
<small>Electron detailed memory usage in KDE (Linux).</small>

![Screenshot of detailed memory usage for atom on KDE]({attach}issue065_05.png)<br />
<small>Atom detailed memory usage in KDE (Linux).</small>

We can see that:

1. Both apps are sharing the `electron` library (it does not have a `lib` prefix, but it is stored in the `/usr/lib` directory which is where libraries go)
2. They both use a bunch of shared libraries: `libicu*` for Unicode support, `libc*` & `libstd*` for standard operating system functions (reading/writing files, etc), `libgtk*` for user interface management, `fontconfig` for fonts, etc
3. Some libraries are still loaded privately, and both programs still have a heap for their own data which is not meant to be accessible to other programs

You can see why the application memory usage shown in Task Manager/System Monitor doesn’t always tally with the total memory usage. Application memory usage usually shows both private+shared memory usage, so that will add up to a number greater than the total memory usage.

**Issue summary:** Shared memory helps to reduce the amount of memory needed by all the applications running on an operating system. It also allows applications to send data to each other, and to communicate.

Long issue, I hope the images make up for it. Computers in the early days didn’t share memory so easily, and that made things really inconvenient. They often had to communicate through one application writing data to a file, and then having the other application reading the data from that file. Slow, and often unreliable. Shared memory evolved as a way to make that process easier.

But shared memory, improperly secured and managed, is also how vulnerabilities like Meltdown and Spectre are made possible, and how malware can do what it does. It’s a double-edged sword.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 66: Before the Cloud

Memory is one of those topics where I think laypeople and engineers have a completely different picture in their heads. I hope this issue has clarified that picture somewhat. It still won't be completely clear until I can talk about heaps, but I wont do that until I figure out how to simplify it.

Meanwhile, the newsletter must go on! I’ve finished Season 5, having explained how computers improve performance through reordering instructions (Out-of-Order Processing) and running instructions ahead of time if it thinks they will be needed (Speculative Execution). Both of these processes use the cache, which is controlled by the CPU hardware directly, not by the operating system. And through an esoteric loophole that exploits timing differences in cache access (cache hit = fast, cache miss = slow), an attacker is able to leak data out from protected kernel memory through the cache.

After this detour, its time to rewind back to where I stopped in Season 3: with networks and the Internet. I went through data types in Season 4 to talk about what complex documents are (because the web is made up of a series of complex documents). Then I laid out a CPU exploit in Season 5, to show you how data can be leaked inadvertently.

Now I’m ready to tell you more about how the current online advertising model became what it is today, and why it is so bad for privacy. You are going to learn a lot more about how ads really work, how advertisers track your online activity, and how they ensnare many companies (especially the big publishers) into a kind of self-reinforcing scheme that lets them target their content more effectively while also letting advertisers improve their targeting.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
