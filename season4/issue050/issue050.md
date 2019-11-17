**Previously:** A file consists of data, preceded by a file header which describes the data. Software (including operating systems) detect the kind of data contained in a file by 1) glancing at the file extension, 2) looking at its declared MIME type (if any), and 3) checking the file header.

I took a small detour in Issue 49 to talk about how files are stored and how the operating system identifies them. This issue, let’s pick up where we left off in Issue 48 about complex data types, and encapsulated data (data in a shell of metadata in a shell of metadata …)

Video files can contain contain multiple data streams: video, audio, and text. That makes them a pretty complex type of file in which we can embed other types of data. But they are not the only complex file type. We deal with them every time we create a new Microsoft Office document, be it in Word, Powerpoint, or Excel. You can embed images, videos, fonts, and even stranger objects in Microsoft Word. How does a simple DOCX or PPTX document keep it all together?

We are going to dig into a webpage document and a Word document and see what it looks like in there.

## Webpage: An HTML document

It may be 2019 now, where URLs can end with all kinds of extensions like `.aspx` and `.php` and even no extension, but a decade or two ago they almost always ended in `.html`. That’s because I mentioned back in [Issue 3](https://buttondown.email/laymansguide/archive/lmg-issue-3-what-is-all-this-clutter/) that the basic format of any web document is HTML. I apologise for leaving that acronym untranslated up till now.

HTML stands for **H**yper**t**ext **M**arkup **L**anguage. We’ve seen this word “Hypertext” before, when I explained the Hypertext Transfer Protocol (HTTP, [Issue 7](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/)), the set of rules that our web browsers use to request Hypertext Markup Language documents. See a link now?

HTML is not a programming language. You can’t write code and tell a computer to make different decisions just by writing HTML. You can create a button using HTML, but you cant use HTML to tell the computer to send your credit card details to another server on the Internet when you click that button. And that is why we refer to it by another term: a markup language.

## HTML Markup tags

This is (a snippet of) the previous issue, as an HTML file:

![Snippet of HTML from Issue 49](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_01.png?raw=true)<br />
<small>Issue 49 as an HTML file</small>

Thank goodness we have syntax highlighting, which should make it easier to notice all the little tags that start with an open angled bracket `<` and closed angled bracket `>`. These are called HTML tags, and they signify the start and end of segments in the document.

- `<html>` starts the document, `</html>` ends it.
- `<head></head>` contains information about the page: the page title (which will appear in the title bar of your web browser), the styles to apply to the document are within
 - `<style type="text/css">…</style>`, which I have hidden here and will show later.
- `<body class="app">…</body>` contains the main part of the document, which is what we will see.
- `<h1>` and `<h3>` signify different levels of headers, which can all be formatted separately.
- `<div>` (for "division") is a generic container, within which you can images or other text.
- `<p>…</p>` (for paragraph) indicates to a web browser that the context is to be treated like a text paragraph.
- `<strong>…</strong>` indicates that it is to be formatted in strong fashion (which is usually treated as bold text … but you can change that in the styles section in the `<head>`).

What are those `class="…"` attributes in the tags? The web browser creates a content element for each tag, and styles it according to the predefined style class in the document, defined inside `<style>…</style>`. This is what that section looks like when expanded:

![Styles for the Issue 49 HTML file](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_02.png?raw=true)<br />
<small>Element styles for Issue 49</small>

I don’t need to explain the specifications for you to notice that `<h1>`, `<h2>`, `<h3>` etc all have a slightly different style defined for them. `.app` is a little different; it starts with a period (`.`) and is applied to everything that has the `class="app"` attribute (*psst* … that’s the `<body>` element from the earlier image!).

Yet at the same time, there are also other styles defined for `<body>…</body>`. The browser has rules for how it chooses which styles override which. Those rules are like the bible for web programmers and web designers, which thankfully we are not (\*waves to any web folks in this mailing list\*).

Okay, just two more tags to illustrate embedding other content:

![Another part of the Issue 49 HTML file showing the <a> tag](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_03.png?raw=true)

The `<a>` tag (for "anchor"; don’t ask) is used to define links (those clickable things in a webpage) and the place it links to is defined as a `href="…"` attribute.

![Another part of the Issue 49 HTML file showing the <img> tag](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_04.png?raw=true)

The `<img>` tag (for "image") is used to insert images. Rollover text, which appears when you put the mouse cursor over the image without clicking, is defined in the `alt="…"` attribute, while the URL of the image is defined in the `src="…"` attribute.

(Embedding an image in a webpage is also possible, but I don’t want to go into depth here because I would have to explain many more concepts before that.)

## Word document: An XML document

I probably didn’t need to explain so much in an issue that’s not Introduction to HTML, but I think it will help make the next part easier to grasp.

Last issue I said this:

> That also means you can spoof a lot of software into thinking you have a zip file when you in fact have an .epub ebook file. This is a pretty common way to unpack files that use the zip archive format to pack their files!

Suppose we do that with a DOCX file … heck, lets convert Issue 49 into a DOCX, rename it to a `.zip` file and see what happens.

![Issue 49 DOCX file opened as a .zip file](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_05.png?raw=true)

![WHOA cat meme](https://i.imgflip.com/2i7zhl.jpg)

Don’t run! Most of it is unimportantly technical, we’ll just jump right into the interesting part which is `document.xml`, so take a deep breath …

![document.xml](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue050/issue050_06.png?raw=true)<br />
<small>document.xml</small>

Okay, ouch. That’s a different tag language, called e**X**tensible **M**arkup **L**anguage (XML). Interestingly enough, each of those tags starts with `w:`, followed by some familiar phrases: `body`, `p`, and others that are not so familiar.

But look, there’s also "Heading1" and "Heading3"! Other than the fact that the tags look completely different, it still uses tags in similar fashion.

## Documents are just another kind of complex file

So, that’s a Word document demystified. When you save a Word document, it just converts whatever you were working on into tags, like this, and zips it all up into a zip file. And any other program that knows how to read these XML files and edit them correctly can then open and edit a DOCX file too.

**Issue summary:** An HTML file contains markup tags that tell the browser how to interpret and format the text within the tags. Other document formats usually use tags in a similar way. These tags constitute a markup language that any app can use to mark up its own text too.

Okay, I hope I’ve demystified webpages, text documents, and just about any place where you see formatted text *just a little bit*. Just about any place where you see formatting being done to text, there’s some kind of markup language working in the background. Of course, its often going to be much more complicated and messy than a little newsletter, but that is why we get computers to handle it.

-----

## What I’ll be covering next

**Next issue:** PDFs Part 1

I’ll round up Season 4 with two issues on everyone’s favourite hated format: PDFs. I think a lot of the reasons people love PDF are spot on, and were how PDFs were sort of intended to be used. And a lot of the reasons people hate PDF occur in cases that PDF was never meant to be used for. They still ended up being used because no better format came along to serve that purpose. More on this in Issue 51.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- ~~HTML? [Issue 38]~~
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
