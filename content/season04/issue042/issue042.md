Title: Issue 42: Unicode, computers go international
Date: 2019-10-15 22:22
Tags: 
Category: Season 4
Slug: issue042
Author: J S Ng
Summary: 
Modified: 2019-10-15 22:22

Title: Issue 42: Unicode, computers go international
Date: 2019-10-12 08:00
Tags: 
Category: Season 4
Slug: lmg-s4-issue-42-unicode-computers-go-international
Author: J S Ng
Summary: 

**Previously:** In ASCII encoding, text is stored as a 7-bit sequence. Text consists of letters, numbers, symbols, and control codes. Control codes instruct the computer how to format the text so that it looks the way we intended.

Last issue, I explained what ASCII is and what it does: it allows us to **encode** letters, numbers, symbols, and control codes into bits (0s and 1s) to be sent to another computer digitally, where it can be **decoded** by another computer.

That still does not explain accented characters (such as á), umlauts (like ö), and emojis. Where are those represented in ASCII? And what about glyphs (symbols) used in Greek, Cyrillic, Chinese, Japanese, and other languages?

## Again, some history

In short, other countries and cultures were not happy with ASCII. It did not allow them to communicate effectively in their own languages.

The first thing that happened was that the European Computer Manufacturers Association (ECMA) extended US-ASCII into ISO 8859-1. In ISO 8859-1, each character is represented by 8 bits. Let’s look at some numbers:

Characters needed minimally (lower- + upper-case, and numerals): 26+26+10 = 62  
Common symbols: 30  
7 bits can encode 2^7 = 128 different characters  
8 bits can encode 2^8 = 256 different characters

8 bits was enough to provide for a number of additional glyphs seen below. But very quickly it ran into limitations as well. 256 characters just aren’t enough!


<figure>
    ![ISO 8859-1](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Latin-1-infobox.svg/800px-Latin-1-infobox.svg.png)
    <figcaption>The ISO 8859-1 characters</figcaption>    
</figure>


## Encoding hell

Computer systems in these other countries soon came up with their own ways of representing the huge number of glyphs they needed. There were other ISO 8859-* encoding systems which I do not want to list. The Chinese had GB encoding on the mainland, Big5 in Taiwan, and numerous extensions on that. The Japanese used Shift-JIS.

It was encoding hell.

If you remember the internet circa the ’90s and early ’00s, the internet often had pages of what looked like gibberish. Because webpages then did not include information about their encoding, most of the time web browsers simply had to guess. If your page wasn’t encoded in ASCII (or ISO 8859-1), it was anybody’s guess what encoding you were using. You just tried each encoding until you got a page that makes sense!

That simply would not do.

## Origins of Unicode

In 1988, a bunch of engineers from Xerox and Apple started thinking about a universal encoding that can encompass all languages. The first volume of this encoding was published in 1991, with extensions added subsequently.

At that point, a Unicode character was represented using 16 bits (for a possible 65,536 characters!). In 1996, a method of extending the Unicode scheme was added, so that Unicode could easily represented over a million different characters!

## Unicode today

Today, the global significance of the internet has resulted in Unicode being the standard encoding on any interface a user interacts with.

If something you try to submit in a form (such as your name) or view on a page does not display properly, chances are the service you are interacting with has not updated itself with proper Unicode support yet. Write a support request to them and ask for it to be done!

One big reason for the increased support in Unicode is the space that was set aside for emoji … more evidence that war may drive the development of technology, but it is social factors that lead to its widespread adoption :)

## Cool things about Unicode

Aside from the fact that it could include encodings for just about any character in any language, here are some things about Unicode which _may not be entirely relevant_ for the layperson, but I think are good to know. Feel free to skip this section.

- Unicode is able to “craft” characters by combining multiple glyphs.
  - For instance, a&#773; is not represented with a single character, but can be printed through combining the 'a' glyph with the ◌̅  (Combining Overline) glyph.
- Unicode has an area set aside for alternate character representations.
  - For instance, “fl” is sometimes stylistically combined into an “ﬂ” ligature; there is room for this ligature in Unicode. (Try to select the ‘fl’s above if you can’t see the difference.)
  - Some high-quality fonts provide such alternate glyph representations, and with the right software (such as Adobe InDesign) you can make use of them.
  - Some languages (e.g. Arabic) actually require ligatures for combining adjacent glyphs, so this is a pretty big deal.
- With the right font type (i.e. [OpenType](https://en.wikipedia.org/wiki/OpenType)), you can actually include programmatic features though Unicode.
  - [FF Chartwell](https://typographica.org/typeface-reviews/chartwell/) is a font for creating mini-charts just by typing!
  - The font uses ligatures to turn numbers into a mini chart.
- Unicode has a "Private Use Area" that you can use for your own private purposes. You can insert symbols from this area for use in a webpage.
  - I have seen websites use this to create custom icons that can scale in size and change colour easily, just like text.

**Issue summary:** Unicode is an encoding format which is meant to support every language, ever. Most websites, apps, and interfaces support it today.

-----

That was really short, thank goodness. I’ve of course skipped over Unicode complexity, because the average layperson does not need to know that. But people need to know that it is possible, and actually _easy_, to represent different languages on the same page, and there is no excuse not to do so.

What’s really interesting is that it took 20 years or more for a format like Unicode to be conceptualised, born, and finally reach the mainstream. Many ideas in computing are like that. When you see something really novel hit the market, it has probably been brewing in somebody’s head for over a decade!

I think we’re as done with text as we need to be. I’ll start going into other types of data in the next issue, starting with colours and images.

## What I’ll be covering next

**Next issue:** Images, a tri-colour mosaic

Coming up: a highly compressed crash course in psychovisual theory, colour theory, and how an LCD screen works! All condensed into layperson language, of course.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- ~~Unicode? And what does it have to do with emoji? [Issue 8]~~
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML? [Issue 38]
- What is OpenType? And what are fonts anyway? [Issue 42]
