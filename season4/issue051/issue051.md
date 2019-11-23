**Previously:** An HTML file contains markup tags that tell the browser how to interpret and format the text within the tags. Other document formats usually use tags in a similar way. These tags constitute a markup language that any app can use to mark up its own text too.

If you were old enough (or perhaps lucky enough) to remember the old days of document layout, you may remember a time when such software was non-existent. You typed the text using a typewriter, being *very careful* to do a carriage return and line break where the pictures were supposed to go. Then you *literally* cut the pictures and pasted them in. Not the right size? You’re outta luck.

And then computers came along. But in the days of dot matrix printers, which printed on paper with those holey tearaway strips on both sides, it was the same process, just digital. You still printed only text, and added the pictures later.

## The early days of publishing

If you were working for a professional publisher, you formatted text by inserting **control codes** (including the formatting commands mentioned in [Issue 41](https://buttondown.email/laymansguide/archive/lmg-s4-issue-41-ascii-the-typewriter-digitised/)) using a special keyboard. But computers back then weren’t powerful enough to show you the effects of that formatting instantaneously. You would just see the formatting code on the display and have to imagine how it looks like in your head. Which is easy to do, after many years of experience.

![Formatting codes revealed in WordPerfect 5.1](https://github.com/ngjunsiang/laymansguide/blob/master/season5/issue051/issue051_01.png?raw=true)<br />
<small>WordPerfect 5.1 (1986), with formatting codes revealed<br />
From [Anthology](https://anthology.hypotheses.org/254)</small>

And then desktop publishing software arrived on the scene in the mid-1980s, when Aldus released PageMaker. You could see *how the pages actually looked*! This feature was called What You See Is What You Get, or **WYSIWYG**. PageMaker was quickly overshadowed by QuarkXpress, which had extensions (whoa!), and Aldus languished and got bought over by Adobe in late 1994. Yup, *that* Adobe. And then Adobe released InDesign in 1999.

## Publishing vs word processing

Why didn’t I mention Microsoft Word, even though it was first released much earlier, back in 1989? That’s because Word is a **word processor**, not a **page layout application**. A word processor is focused on helping you to produce reports with nice formatting, but still primarily text-based. You wouldn’t design a professional magazine in Microsoft Word; it doesn’t give you enough fine-grained control over positioning of the various elements. For that you need a proper page layout application, like InDesign.

I just mentioned fine-grained control. That’s something you are going to hear a lot in the world of graphic design. Designers and publishers want control, lots of it. They not only want to control where things go on the page (down to sub-millimetre precision), they even want to control exactly how the colour looks.

Going into more detail here would betray my principle of writing for the layperson, but I think it is important to present this perspective because it explains the need for a format many of us love and hate: the PDF format.

## Ensuring print fidelity: the Postscript language

When you design something on the screen, how do you know that it will look *exactly the same* when printed? Short answer: you won’t, unless you have a markup language that is understood the same way by both the desktop software and your printer. That language is called **Postscript**, and it can handle text, images, shapes, and additional info (or metadata, i.e. data about data) that comes with them.

But people soon wanted to include even more things in their documents: forms, videos, 3D artwork, … many of which Postscript did not support natively. And that’s where PDF shines.

## PDF: the standard for compatible fidelity

Today, it is easy to take for granted that when I create a DOCX document in Word on my iPad and upload it to Google Drive, it should open on my laptop and look the same. To an accurate enough degree, anyway.

But two decades ago, such compatibility was still a dream. You could not take for granted that a complex document format produced on one software would open correctly (if it even opens) on another piece of software, or even the same software written for a different machine (think of Word for Windows, Mac, and other OSes).

Needless to say, this was incredibly frustrating for industry. If you were running an ad campaign and your ad agency is trying to send poster designs to you but you each use different software in your workflow … well, how is that going to happen? Or what if two different government departments are trying to collaborate on a form that citizens will use to file taxes?

A lot of engineering and coordination went into ensuring that PDF would work everywhere (universal compatibility), and display exactly the same way on every device (visual fidelity), and that is why it is a gold standard for the printing and publishing industry. If you want to ensure your T-shirt design will appear **exactly**[^1] the way you want, send it as a PDF file, not as an image file. Have your magazine cover all set up with the fonts, sizes, colours, and everything else absolutely correct?[^2] Send it to the printers as a PDF file.

[^1]: This is harder than it appears; for one, you have to ensure you get the image size and resolution correct, or the printer will have to modify it for you.

[^2]: Again, this is harder than it appears; the way to specify the exact colour you want is not something a layperson would know.

There is just one issue with PDF: because of the way it was designed to *display correctly*, editing it is a big pain compared to text-based formats like DOCX or even HTML. I’ll explain why in the next issue.

**Issue summary:** PDF is the gold standard for universal compatibility (supported by most software and platforms) and visual fidelity (displays exactly the same way). When you need things to appear on a different device in exactly the same way you created it, without having to install additional software, use PDF.

I am *sooo* glad I don’t have to go into technical detail here. PDF is an incredibly, amazingly, mind-blowingly complex specification. All the words written about it would fill tomes. I am not surprised that Adobe charged so much for the initial versions of Adobe Reader and Acrobat; the immense amount of work that went into it would have made that price feel justified. (But luckily for all of us, more enterprising minds prevailed.)

I hope this issue sheds some light on the uses of PDF. We don’t get taught these things by our parents, in school, or anywhere really; the only folks who know this are usually publishing industry professionals. But with more and more programs being able to handle and produce PDF files, if we hope to continue enjoying its benefits and avoiding the consequences of using it inappropriately, then it is time that such knowledge became more commonplace.

**For more:** [Pretty Darn Fascinating: The story of the PDF, the portable document format that’s become one of the internet’s defining information formats.](https://tedium.co/2018/02/27/pdf-file-format-history/)

-----

## What I’ll be covering next

**Next issue:** PDFs Part 2

Next issue, I’ll try to explain why PDF files are the idiosyncratic beasts you hate to edit. While still avoiding technical jargon as much as I can.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
