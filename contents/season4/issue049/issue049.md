**Previously:** A video container can hold one or more audio, video, or text data streams. To encode or decode a data stream, you need to have the necessary codec installed. Most video runs at 25 or 30 fps, with high-quality video going up to 60 fps. You can use a program like MediaInfo to help you decipher the streams inside a video container file.

Images, audio, video, and more … we are so used to thinking of them as different kinds of files. But within the computer’s binary world, how does it tell that one file is a different type from another? In the human world, if you ran across a bunch of unlabelled boxes of various types and sizes, you would have no way of telling what is in each box. And you know this is a terrible way to move house—you would have to at least label the boxes by colour, by room, or by type of contents.

You would also have encountered this if you bought anything online. Your packages arrive with a shipping label, which is a quick and convenient way for the shipping companies to identify the package, type of contents, origin, and destination.

The box labels, and the shipping labels, tell us _about_ the contents, but not the contents itself. We refer to such data as **metadata**. Metadata is data about data.

For a computer to be able to handle so many files without inspecting them individually, it must also have metadata about each of these files.

# The file header

Files generally have a file header. The GIF file format begins with a header (“GIF87a” or “GIF89a”), so anytime a piece of software (e.g. an image editor) starts to read a file header and detects that label, it knows it’s dealing with a GIF file and not a JPG file.

When the software opens a GIF file, and before it has read anything beyond this header signature (that’s what the [GIF file specification](https://buttondown.email/laymansguide/archive/lmg-s2-issue-23-specifications-in-software/) calls the above label), it doesn’t know anything about this GIF file. Before doing anything else, it will at least need to know the width and height of this image, and in the case of GIF, some information about its colour palette (which can vary from GIF to GIF). All this information is stored within the file header, and the software will have to know how to read it from the header.

If for any reason you wish to start writing software that can edit GIF files, you can find out its [detailed specifications](https://www.w3.org/Graphics/GIF/spec-gif87.txt) online. This is because when Compuserve came up with the format in the early days of the internet, they meant it to be widely used. Companies who design a file format to be used internally and not for public use will come up with **proprietary** file formats, which are inscrutable to most people. Anyone coming across such a file would have no idea how to open it.

If you want to figure out such a file format, you would have to **reverse-engineer** it, like [this guy on StackExchange](https://reverseengineering.stackexchange.com/questions/261/how-to-reverse-engineer-a-proprietary-data-file-format-e-g-smartboard-notebook). Since typical engineering means starting with a blueprint and coming up with a product, reverse-engineering means starting with the product and trying to figure out its blueprint. Here’s Julia Evans having a go at [reverse-engineering the Notability file format](https://jvns.ca/blog/2018/03/31/reverse-engineering-notability-format/).

Another example: The MP3 file format is simpler (although not easier to decode). Audio data is organised into frames, each frame having its own header followed by data. What about the artist name, record label, genre, date of release, and other information that comes with the file? All that is stored within the ID3 portion of the file metadata.

![MP3 file structure showing internal structure](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season4/issue049/issue049_01.png)<br />
<small>The MP3 file structure<br />
Image from [Wikipedia](https://en.wikipedia.org/wiki/MP3#/media/File:Mp3filestructure.svg)</small>

# File extension

That seems like an awfully complicated way for operating systems to detect what type of files they have. They would have to open each file individually, even if just to read the header, and then figure out which complicated set of patterns the header matches. When you open a folder, save a file, or download something from the internet, the computer seems to do that detection much faster.

That’s because when speed is a concern, software will often attempt to detect the filetype simply by detecting the **file extension**. File extensions are the ending characters in the filename, after the period (“.”). A file named sound.mp3 has a .mp3 file extension, and one named image.gif has a .gif file extension. That’s a much faster way to detect a whole bunch of filetypes, it’s quick-and-dirty, and it mostly works.

That also means you can spoof a lot of software into thinking you have a zip file when you in fact have an .epub ebook file. This is a pretty common way to unpack files that use the zip archive format to pack their files! So if you write software that absolutely needs to be sure it has the right filetype, you should double-check the file header instead of jumping to assumptions from the file extension alone.

## What about the internet?

Guessing from file extensions might work in a computer, but on the internet it’s the Wild West. Images sent as data packets over the internet do not come with filenames; notice how some apps (e.g. WhatsApp) rename your image with a different name when you upload or download them? And on some web platforms, especially those that handle huge volumes of images, the filenames are just semi-random characters.

That is why we rely on what are known as **MIME types**. MIME stands for **M**ultipurpose **I**nternet **M**ail **E**xtension, and yes there is an RFC for it, [RFC6838](https://tools.ietf.org/html/rfc6838). This is a much more standardised way of declaring what type of file you have. [The exhaustive list](https://www.iana.org/assignments/media-types/media-types.xhtml#examples) of MIME types, maintained by IANA (whom we first met in [Issue 27](https://buttondown.email/laymansguide/archive/lmg-s3-issue-27-what-is-an-ip-address/)), has MIME types for application files, audio, font, image, messages, model, multipart formats, text, and video.

If you plan to come up with a file format that is intended to be used widely, you can [apply for it to be included](https://www.iana.org/form/media-types) in the list.

## MIME types and HTTP headers

Remember this HTTP header from Issue 8?

![An HTTP request header](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season1/issue008/issue008_01.png)

See that label in the third row, with the Content-Type label, “application/json”? That’s the MIME type for the [JSON data format](https://buttondown.email/laymansguide/archive/lmg-issue-5-what-is-json/). When the server returns data, my browser (the client) has no idea what format it is. It might be nicely formatted HTML meant for human consumption, but it might also be plain text, JSON data (like in this case), XML, or any of the various data formats that people use. Declaring the MIME type properly makes life easier for the browser to know what to do with the data.

**Issue summary:** A file consists of data, preceded by a file header which describes the data. Software (including operating systems) detect the kind of data contained in a file by 1) glancing at the file extension, 2) looking at its declared MIME type (if any), and 3) checking the file header, in order of difficulty and accuracy.

I almost started writing a long post about filesystems, but stopped myself in time. I hoped with this issue to continue emphasising the theme of data encapsulation: data locked in shells upon shells upon shells of metadata. I’ll be back to describing other types of data again for the rest of the issue, but I thought file headers would be good to introduce at this point.

After this season I won’t be digging into complex data types, but when I move on to operating systems I’ll cycle back to filesystems and what you need to know about them. Before I get to that season, though, here’s something for you to ponder: if all data is ultimately binary, how would an app know where one file ends and where another starts? Does the file header for mydocument.doc start at this 0, or another 0, or actually at this 1?

-----

## What I’ll be covering next

**Next issue:** Complex file formats and the Document

Two issues ago, I just talked about video formats, which include multiple types of data: video, audio, and even text (subtitles).

Next issue, we’ll pick up where we left off to look at another format that includes multiple data types: the document.

See you again next week, next issue.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- HTML? [Issue 38]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
