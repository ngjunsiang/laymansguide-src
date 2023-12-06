Title: Issue 111: Copying, moving, and deleting files
Date: 2021-03-13 08:00
Tags: 
Category: Season 9
Slug: issue111
Author: J S Ng
Summary: 
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Filesystem journals are a record of changes made to the disk, so as to enable those changes to be rolled back, or to be completed properly in case of sudden interruption.

Okay, that’s enough of a look at the nitty-gritty of moving data around. In this issue, let’s turn our attention to the file table, where interesting things happen as well.

## What happens when we copy a file?

A copy of the data is made, and moved to an available location (series of sectors) on the disk, and a new file table record is created. No magic yet.

## What happens when we move a file?

Okay, this is slightly more complex, but not difficult.

First of all, if we are moving the data within the same disk ... do we really need to move the data? In layman terms, when we “move” a file, we are not actually changing its physical location in the disk. We are basically updating a file so that its stated location, which used to be something like `C:\Users\myusername\Desktop\video.mp4`, will become `C:\Users\myusername\Videos\video.mp4`. This is information *about* the data, and is not stored with the data—it is actually stored in the file table!

So when we “move” a file within the same disk region (i.e. within the warehouse, in our earlier analogy), we are actually just updating the file table record, without copying or writing any of its contents. This is why it can seem so amazingly fast to “move” a multi-gigabyte file.

But if we are “moving” the data to a different disk, or to a different region on the same disk (e.g. moving something from the `C:\` region to the `D:\` region), it is like moving cargo from one warehouse to another. Each warehouse keeps its own file table, so we can’t merely update the file table and keep the contents on the same pallet on the rack. The cargo needs to be moved to a different warehouse, and the file table record copied over as well. For data, this means the contents are copied to the new location, the file table is updated, and if both happen without error, the original contents and file table record are deleted.

## What happens when we delete a file?

Ah, fun times. Okay, so I suppose most of you keep your computers on the default setting, where pressing the `Delete` key doesn’t actually delete a file irretrievably, but simply puts it in the Recycle Bin.

And when you are deleting a lot of files ... you notice this can take a long time. Obviously the contents are still around (so that you can still restore them), but the file table records are now *hidden* from the user, so that they appear to be deleted. If you are deleting 100,000 files, that is 100,000 different file table records to update.

You can, of course, change this setting (and I won’t teach you how to do that here, but it’s just a Google search away). If you disable Recycle Bin, or use the `Shift+Delete` hotkey combination to force a permanent deletion, something different happens instead. Intuitively, it seems like the OS should actually clear out the (digital) space previously occupied by the file contents. But this offers no advantage; to change a `1` to a `0`, you have to *write* a 0 to it; there is no *erasing* in the world of storage!

The faster way is to simply tell the filesystem that this file no longer exists, and the space it used to take up can now be overwritten. And that is done ... by simply deleting the file table record. This is a simpler operation than updating, which is why permanent deletes are so much faster than Recycle-Bin deletes.

This is also why, if you accidentally permanently deleted a file, you still have a chance of recovering it with file recovery software! The recovery software ignores the file table, and instead scans the entire disk for its actual contents, trying to see if there are any valid fragments of files left. If the space has not been overwritten by anything else, you just might be lucky enough to recover its contents. The chances of this decrease as you use the disk and write over parts of the disk which contained the file data, so this has to be done as soon as possible.

**Issue summary:** Moving a file (within the same disk region) merely updates its file table record, and this happens really quickly. Copying a file, or moving it to a different disk/region, involves copying the contents and then updating the file table record, and is considerably slower. Deleting a file only requires that its file table record be removed, and is a very fast operation (if it does not involve the Recycle Bin).

I’ve been waiting a long time to explain this, and can finally get it out on screen. Phew!

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 112: Bootstrapping into existence

Now I can move on to something closer to the hardware, and talk about what happens when the power button is pressed.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- a driver file and why do I need one? [Issue 98]
