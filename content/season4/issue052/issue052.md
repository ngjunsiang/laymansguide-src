Title: Issue 52: PDFs part 2 – Text and images
Date: 2019-12-21 08:00
Tags: 
Category: Season 4
Slug: lmg-s4-issue-52-pdfs-part-2-text-and-images
Author: J S Ng
Summary: 

**Previously:** PDF is the gold standard for universal compatibility (supported by most software and platforms) and visual fidelity (displays exactly the same way). When you need things to appear on a different device in exactly the same way you created it, without having to install additional software, use PDF.

I mentioned earlier that PDF is an incredibly complex and powerful format. You can do so much with it once you have digested the approximately 900 pages of [its format specification](https://www.adobe.com/devnet/pdf/pdf_reference.html), which are available for free. To support older versions of Acrobat and other readers, you may have to cross-reference [the reference manuals of older versions](https://mpdf.github.io/reference/pdf-files-adobe/pdf-reference.html). It’s not impossible, but I hope this helps you understand why many apps and services are reluctant to provide PDF support unless there are already libraries available for them to use in their own application. This is time-consuming stuff!

## Nope, I’m not going to read that.

Sure, that’s why I’m writing this newsletter :) Now if you flip to page 238 of the reference manual (I’m just kidding, don’t go download the reference manual now!) and look at Example 1, you see this:

```
This example illustrates the most straightforward use of a font. The text ABC is placed10 inches from the
bottom of the page and 4 inches from the left edge, using 12-point Helvetica.

BT
    /F13 12 Tf
    288 720 Td
    (ABC) Tj
ET

The five lines of this example perform these steps:

a) Begin a text object.
b) Set the font and font size to use, installing them as parameters in the text state. In this case, the font
resource identified by the name F13 specifies the font externally known as Helvetica.
c) Specify a starting position on the page, setting parameters in the text object.
d) Paint the glyphs for a string of characters at that position.
e) End the text object.
```

Remember when I showed you some markup languages in [Issue 50]({filename}/season4/issue050/issue050.md))? Here’s another one, but much more concise and much more specific: it lets you specify font and position for each string of characters. There are additional formatting codes for changing the colour, changing the text format to an outlined version, and making various other kinds of changes.

## How PDF documents display this text

In the reference manual, there is a long and complicated way of putting a text block into a PDF document and specifying the line spacing and character spacing and how to insert line breaks and all that, so that it appears nicely. In practice, it is rather difficult for developers to convert their own format used in their app into what the PDF format fully requires (see my point at the start of this issue about having PDF libraries available).

If it is done properly, copying text from a PDF document is rather easy, and you may on rare occasion have experienced this. Apps that do not use or do not have access to high-quality PDF libraries for their app may end up generating PDFs that simply display the text word by word, or line by line. If you’ve ever copied a paragraph of text from a PDF and had it appear in multiple lines instead of a single line, or with some word spaces missing, this could be the reason why.

## What about images?

Again, the one thing you need to remember is that PDF is concerned primarily with *how things look*, not with *what things are*. To display a JPG or GIF on a PDF, the app’s PDF library has to convert it from its compressed format into an array of pixels. The image’s pixel dimensions will seldom match those of the frame it must go into; often you may find yourself trying to fit an 800×600px image into a 400×300px space. The PDF encodes that stream of pixels, and you may not be able to get the original image back from that stream, especially after it has gone through some resizing and cropping.

## Why can’t I copy text from a scanned document?

Ah, a common question, and one I have been dying to answer.

When you scan a document, your scanner does not produce text; it produces an image. When the scanning software lets you save your scan as a PDF, it basically puts the image into a full-page PDF and calls it a day. There is no text content in the PDF at all!

If the software is a bit smarter, or if you have Adobe Acrobat, you might have access to **O**ptical **C**haracter **R**ecognition software (**OCR**). This is a feature in some apps that recognise text in images and recreates it for you. This feature lets the app check your scan for recognisable characters and produce a text stream from it. It can them put this text into an additional layer in the PDF, below the image.

It takes some additional trickery to ensure the text appears at exactly the same position where it was detected in the image (remember from above that the text position must be specified). If the PDF library gets the font size and positioning right, this *simulates* the experience of selecting text on the image and having it appear to be highlighted.

However, the state of OCR technology is such that you will often still get typos or missing/extra spaces in the text, so do be sure to check any text that you copy from a PDF!

**Issue summary:** PDF’s markup language is more concerned with how things appear on the page than with what they were originally. Once the PDF is generated, it is almost impossible to retrieve the original data from it. Scanned documents that are converted to PDF may have a text layer generated by OCR that lets detected text be copied from it.

… and Season 4’s a wrap! Phew, I hope Season 4 increased your understanding of how text, images, audio, and video are represented and stored in a computer, of how lossy and lossless compression work and why the former leads to a decrease in quality, of what a file is and how OSes tell them apart, and lastly of documents and other complex file types, and how they are put together.

-----

## What I’ll be covering next

**Next season:** The CPU - where it all happens

I was going to start Season 5 continuing where I last left off in Season 3. From networking I would have gone on to talk about the internet and its history, how it became the cloud, and how we had the advertising network we have today. But I realised that (1) I still need to do more research on some areas (particularly ad exchanges), and (2) Meltdown and Spectre are apparently not fully fixed yet.

If you remember, Meltdown and Spectre are the CPU vulnerabilities that can potentially allow attackers to access protected data in your computer’s memory. Most of us don’t have much on our computers that we need to worry about, but banks and other corporations that we rely on certainly do!

One year on, that vulnerability is still not fully fixed. Some people seem to be flabbergasted by the inability of the huge CPU companies (actually just mainly Intel) to figure this out. But once you understand what Meltdown and Spectre are and how they work, even at a layperson level, I think it is easier to see that there is no straightforward fix that will make everyone happy. With media outlets everywhere citing Moore’s Law uncritically and expecting performance to increase in accordance with it, I am disappointed that such a vulnerability had not been conceptualised earlier and prevented, but I am not surprised.

Security and privacy are the hot-button topics of the day, but there are many pundits and analysts talking with little idea of how they are implemented and why they are such a difficult challenge. With Season 5 I hope to lay out the basics of operating system security and CPU operation, and attempt to explain in simple terms how Meltdown and Spectre work and why they are so difficult to fix.

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
