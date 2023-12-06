[**Previously:**](https://buttondown.email/laymansguide/archive/) The OS takes care of booting up, login and user management, window management, memory allocation, storage interfaces, background services, peripheral management, and much more. Access to these services, where allowed, is provided in the form of software libraries that developers can use.

So far, what we understand about storage is that apps send data to an operating system (OS), which then stores it on storage devices (such as hard disks, solid state disks, etc) for later retrieval. And in [Issues 99](https://buttondown.email/laymansguide/archive/lmg-s8-issue-99-where-does-all-the-app-data-go-a/) & [100](https://buttondown.email/laymansguide/archive/lmg-s8-issue-100-where-does-all-the-app-data-go-a/), I explained that eventually everything gets stored as a file.

What exactly is a file?

## Files in operating systems

Let’s start from what we know about files. When we open File Explorer in Windows and open any folder (aka **directory**), we see a bunch of things with colourful icons, that we know of as files. And we also see things with folder icons that we know as folders (or directories).

They also have additional details displayed alongside them, such as the date/time (henceforth referred to as datetime) it was created, the last datetime it was modified, and the last datetime it was accessed. You might also get additional information, such as what type of file it is, its size, the user who owns that file, etc—in other words, the **metadata** of the file. That’s a fancy word to refer to data (datetime, filetype, size, …) *about* the data (the files).

Now, a brief introduction to the hardware, where the actual files get stored.

## Introducing storage

When you buy a hard drive (or solid state drive) and connect it up to your computer (or laptop), the computer does not have fine-grained control over every bit of storage. Instead, the hard drive gets presented as a huge volume of space, like a warehouse.

This volume is organised into **sectors** (these days, a modern hard drive sector is 4KiB), which are the smallest unit of storage on a hard disk. If you have to store 1KiB of data, it will still take up an entire sector; the rest of the space is filled with zeroes. This is similar to the way a warehouse is managed by pallets, and not by single cardboard boxes. If your shipment does not fill the entire pallet, the rest of the space is “wasted”.

Each sector has an address (yes, just like memory!). To store data on the hard disk, the OS has to “tell” the hard disk a) what data to store, and b) the address at which to store the data.

The hard drive itself does not inherently have any system for managing your files or folders; it can’t tell you where `draft1.docx` is stored, nor tell you what the size is. It only takes care of storing data at addresses, and retrieving data from addresses!

## Managing storage

And this is where the operating system comes in. An operating system installing itself is like a company occupying a warehouse. You’ve got to impose some kind of order on the space!

In an operating system, this job is delegated to the **file system**, a sort of facility director who manages the storage space. Windows uses [NT File System](https://en.wikipedia.org/wiki/NTFS) (**NTFS**) for its own space, MacOS uses [High Performance File System](https://en.wikipedia.org/wiki/High_Performance_File_System) (**HPFS**), while portable storage devices (e.g. USB drives) often use [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table) (FAT).

An operating system that is not “aware” of other filesystems will not be able to read storage devices formatted with those filesystems. This is why you can’t just take out a disk from a Mac system and expect it to open in Windows when plugged in. Windows can read HPFS disks, but cannot write data to them. Both OSes can handle FAT (phew!), which is why it is possible to pass files from a Windows user to a Mac user with a portable flash disk.

## How filesystems work

Intuitively, we might imagine that the metadata for each file gets stored with its data. This is like storing the shipment details of each package with the package itself. But when you need to find a particular shipment in the warehouse, you can’t be checking every single rack!

Instead, you would store shipment records in a master file, usually in some kind of separate office, which would list the shipment details alongside the location of the cargo (e.g. by rack number and level). The equivalent of this master file on a filesystem is the **file table**.

In NTFS, this is the Master File Table (MFT). The MFT lists all the files on the disk (by their full path, e.g. `C:\Windows\system32\notepad.exe`), along with its metadata. This makes it easy for Windows to show you the data quickly when you open any folder in File Explorer; it can get all this data from the MFT easily!

Sounds peachy. What can go wrong with this picture?

**Issue summary:** A hard disk is organised into sectors, which are the smallest unit of storage. The OS’s filesystem determines how and where to store each file on the hard disk. The filesystem manages the file metadata in a file table, separate from the actual contents of the file.

## What I’ll be covering next

**Next issue:** [LMG S9] Issue 107: The challenges of storage

This is where I talk about all the ways we make life difficult for computers, but easier for ourselves. Like unplugging USB drives before removing them safely …

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- ~~How do apps know where a file starts and ends? [Issue 49]~~
- a driver file and why do I need one? [Issue 98]
- why does computer memory exist when apps can read directly from the hard disk? [Issue 105]
