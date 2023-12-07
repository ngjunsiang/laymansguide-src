Title: Issue 104: Storing sensitive data
Date: 2021-01-23 08:00
Tags: 
Category: Season 8
Slug: issue104
Author: J S Ng
Summary: 
Modified: 2021-01-23 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) A race condition happens when threads depend on instructions happening with coincidental timing for success. When instructions are not executed with appropriate timing, one or more threads can get stuck waiting on a response that never comes.

To wrap up this season on how apps work, I’m going to try answering a question I had on my mind as I was still new to computers: where do my secrets get stored? If I don’t want them to be stored, what are my options?

I will answer that *from an app’s perspective* in this issue.

## Why would I want to keep secrets from my users?

You just wrote an app. Your app syncs data to a cloud database ([Issue 90]({filename}/season07/issue090/issue090.md))). But the cloud database has many other app developers using it as well—how would it know it is you and not some other malicious hacker? It recognises you via a **shared secret**: a token or an API key that you can see after you log in to your dashboard on their website.

After your users install the app, every request sent by your app to the cloud database has to be authenticated using this *shared secret*. That means you are going to have to get this shared secret onto the app somehow. But this has to happen without the user being able to see it or access it, otherwise a savvy user could use that key to gain access to your cloud database.

## Storing secrets on the web

The code that is loaded by the user’s browser runs under their control, so putting the shared secret anywhere in that code is a bad idea. Any savvy user who knows how to view the script’s source can potentially find it!

A much safer option is to store the secret with the code that runs on *your server*. But not in the server’s source code! If you are most developers, you would be using some kind of version control system ([Issue 19]({filename}/season02/issue019/issue019.md))) that maintains a copy of your source code and all its changes. If you are using Github or some other public platform for this, you have to be very careful that the shared secret is not visible (or otherwise guessable) just by reading the source code.

For a simple shared secret, such as a short string of characters, app developers usually use **environment variables**. These are pieces of information that are kept in memory only, accessible by the app, and are set by the operating system whenever the app starts up. The server where you run your code will let you configure the environment variables that your app needs, keeping them out of sight of the users.

## Storing secrets in a mobile app

Mobile apps are supported by a host of services provided by the operating system (OS), typically managed by Google or Apple. They each offer a way for you to store a shared secret with the OS. Your app can use this shared secret from the OS to encrypt information so that other apps are not able to access it. When your app starts up, it requests the secret from the OS, and uses it to decrypt the secret again.

## Storing secrets in a laptop app

If you are developing a laptop app that does not rely on a connection to your server (i.e. a “standalone” app), your options are somewhat more limited. Since all your app code and resources will be in the user’s machine and thus accessible to the user, your best bet is to find some way to obfuscate it and hope no one finds it easily.

This is one reason why so many apps require an online connection: it is much easier to hide secrets on a machine you own and control! With a server connection, you can require the app to retrieve the secret from the server, and delete the temporary copy of the secret after use.

## Storing passwords

If your users log in with an email and password (which is almost every online service ever), you don‘t actually store their passwords; that is terrible security practice, even if you do it in a database! A nifty piece of software technology, known as a **hash function**, takes that password (regardless of length) and turns it into a unique[^1] **hash** with a fixed number of characters.

[^1]: In practice, there is a very low chance that two different passwords may end up giving the same hash. This technology is still being improved!

Examples of hashes:

```
661c425549bc70b98e908325b8c64f82
056cd6eb540ace37e64572c64c778d45
239b1ddbb45caf82408cb89f13816185
```

What you do, then, is to store the password *hash* instead of the password. When a user sends a username and password, you hash their attempted password, compare it with the stored hash, and see if they are the same.

The hashes are designed to be difficult to reverse. The state-of-the-art algorithm used today can generate hashes that would take millions of years to reverse using hardware currently available. But there are techniques that can reverse hashes of some older algorithms in as little as 30 minutes, so if you are a developer, please find out which one to use!

**Issue summary:**

Shared secrets allow secured access to resources, such as databases or other services. These shared secrets are typically kept on a server controlled by the app developer. For mobile apps, they are usually stored with the operating system, inaccessible to other apps.

Phew, we had enough issues here to cover the main parts. And I managed to answer one of the sometime-in-the-future questions! Actually, I also answered another one on software installation earlier, in issues [99]({filename}/season08/issue099/issue099.md)) and [100]({filename}/season08/issue100/issue100.md)), so I’m going to go ahead and strike it off.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 105: Operating Systems

This wraps up another season of Layman’s Guide on how apps work. Next season, I am going to zoom out and look at the environment that apps operate in: the operating system. Yep, I’m going to tackle the most complex pieces of software ever to be written, and try to explain them in terms that laypeople can understand 😅

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- ~~involved in installing a piece of software? [Issue 48]~~
- How do apps know where a file starts and ends? [Issue 49]
- ~~a password hash? [Issue 63]~~
- a driver file and why do I need one? [Issue 98]
