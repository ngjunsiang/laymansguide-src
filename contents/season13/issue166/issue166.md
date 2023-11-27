[**Previously:**](https://buttondown.email/laymansguide/archive/) There are easy and quick ways to check the validity of the most common advice for resolving system slowdown. But it still seems to happen even after these tips have been tried.

Last issue, I walked through common causes of system slowdown suggested by generic tech websites, and explained simple ways of checking if these are really the cause. Quite often, they are not, especially if you are the kind who is careful about internet usage and does regular system maintenance.

So what is going on?

## Caches, caches, and more caches

In [Issue 39](https://buttondown.email/laymansguide/archive/lmg-s3-issue-39-caches-and-caching/), I explained what caches are: places where you (temporarily) store the result of lookups, so you don’t have to keep performing the lookup again. In context, this referred to DNS lookups: operations that translate a domain name (such as `google.com`) to an IP address (such as `173.194.217.100`).

But caches are everywhere, not just in DNS.

### Examples

When you open any Microsoft Office application, it shows you your most recently accessed documents: that’s a cache! (The info has to be stored somewhere, right?).

[Windows caches your old installation files](https://www.thewindowsclub.com/windows-installer-folder-to-delete-or-not-to-delete-that-is-the-question) “just in case”.

Your browser definitely caches your browsing data (they are called “Temporary internet files”).

And most apps have a cache of some kind or other to hold data which they think you will want to access again soon.

These are generally harmless uses of caches, albeit possibly annoying (when Adobe Premiere caches video files that take up gigabytes of space …). Caches are predicated on the notion that access from a storage disk (on the same device), while slow, is still faster than its alternative (fetching the data from its source, over the internet or through a computationally expensive calculation).

## App caches: a short history

Before the internet went mainstream, a lot of software came on compact discs or diskettes. These were slow to spin up, slow to read, and slow to swap out. They were nonetheless necessary in the days when hard disks were still low on storage, and expensive.

As hard disks increased in capacity and decreased in price, it made sense to copy the information from these diskettes or compact discs into the hard disk, and subsequently access the data from disk. This process is what we know as **software installation** (bet you saw that one coming!).

These days, the disk-is-faster assumption is less true across a spectrum of uses. Especially when it comes to mobile devices.

## Mobile storage and internet

A quick note on mobile storage, which I unfortunately missed out on [Issue 119](https://buttondown.email/laymansguide/archive/lmg-s10-issue-119-solid-state-disks-an-upgrade/) on laptop and desktop solid-state disks (SSDs).

Mobile devices generally do not use the same kinds of SSDs that laptops use. Those are bulkier, use more power (not good for mobile battery life), and run hotter. Laptop SSDs use an interface called NVMe (which iPhones use as well), while most Android devices’ storage use an interface called UFS which is slower (but uses less energy).

At the same time, internet access on phones is speeding up. 4G/5G technology has increased throughput, while maintaining more or less the same latency. On the other hand, with the cloud becoming a staple of everyday life, tech companies have poured immense resources into increasing their servers’ responsiveness, resulting in lower latency for internet access.

Disk caching is no longer king.

## Caches on mobile devices

On Android, a tip not mentioned in the previous issue is to [clear the app cache](https://www.howtogeek.com/183004/why-android-phones-slow-down-over-time-and-how-to-speed-them-up/). For many apps, the app cache can grow to tens or hundreds of megabytes. As Android device storage slows down over time, the app cache gets slower and no longer serves to speed up the app. So clearing the cache regularly can help keep performance from degrading too much.

However, Android itself uses caches for system processes as well, and these are usually not accessible to the user. That means the only practical way for most users to clear this cache is usually to perform a factory reset.

**Issue summary:** Caches speed up app operations by storing temporary data on the device’s storage. This assumes that access to storage is much faster than access to the file’s original source. On Android, users can clear an app’s cache, but not the system cache.

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 167: Database fragmentation

This issue, I explained why caches no longer work as well as expected.

Next issue, let’s poke a little deeper: why does clearing the cache work?
