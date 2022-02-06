[**Previously:**](https://buttondown.email/laymansguide/archive/) Linux software is distributed through Linux distros. The maintainers of distros maintain repositories of software that have been tested with the distro. Most users will access software in the distro’s repositories through a program called a package manager. So users have full control over when updates and new software should be installed.

Once your laptop hits the magical 1-year window, it somehow seems to … get slower. And slower. Everything takes just a fraction longer. What used to happen near-instantaneously now seems to take a split-second pause. The loading spinner animation feels like it plays just a little longer. And it just gets worse from there with age.

Google search results have a number of things to say about why it happens:

## Programs starting up when booting

This is primarily an issue when you are booting up your laptop ([Issue 112](https://buttondown.email/laymansguide/archive/lmg-s9-issue-112-bootstrapping-into-existence/)) and logging in. Once you log in to your operating system (OS), your OS will run the startup programs (which you can disable), so if you are trying to use your laptop right after logging in, this may cause some slowdown.

If your laptop is still slow about 10 minutes after OS login, this is probably not the cause.

## Programs running in background

You can check this easily: open Task Manager (in Windows), and see if CPU, Memory, or Disk are significantly high. You can click on those columns to put the highest-usage processes at the top. Often it is some kind of antivirus or malware scanner that is hitting the disk and causing things to be slow. Wait for these programs to finish (if legitimate), then see if your computer still feels slow.

## Insufficient memory

This is easy to check in Task Manager too. On the performance charts on the right, see if memory usage is near 100%. If it is, try closing some applications until usage drops below 100%, and see if system performance improves after a few minutes.

## Malware

Malware that slows down your laptop usually does so by taking up a lot of CPU time, or using a lot of memory. You can test this using the above tip too.

If your computer fan is spinning noisily even though CPU/Memory/Disk are low, it’s either malware that is smart enough to hide itself, or blocked computer vent (which is causing your CPU fan to be ineffective). These are easy checks to make too.

## OS updates

Just update your OS. Most of the time this does not fix system slowness.

## Disk full

Open My Computer (in Windows), which should show how full your system partition is. If it is below 80% full, this probably isn’t the issue, regardless of whether your system is on a hard disk or solid state disk (SSD, see [Issue 119](https://buttondown.email/laymansguide/archive/lmg-s10-issue-119-solid-state-disks-an-upgrade/)).

## File fragmentation

You can run Drive Optimizer on your system partition. Yes, there is a lot of discussion about how defragmenting an SSD is bad; fortunately Drive Optimizer is pretty smart about this and will only carry out defragmentation on hard disks; the option is called Optimize if your system partition is on a solid state disk.

This usually helps a little, especially if the hard disk is quite badly fragmented. If it is only lightly fragmented, or if you are using a solid state disk, this usually won’t resolve any slowdown.

----------

These are some quick ways to check on the validity of these myths about the causes of system slowdown. In many cases they do help! But there seems to be this general malaise that affects even the most cared-for and most well-maintained laptop, after an operating system has been used for years without a reinstall.

**Issue summary:** There are easy and quick ways to check the validity of the most common advice for resolving system slowdown. But it still seems to happen even after these tips have been tried.

Knowing what we know, this far into this layman’s guide, I’ll look into some other possible causes next issue!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 166: Causes of system slowdown
