**Short version:** An Application Programming Interface (API) is a data browser for apps, a way for apps to talk to each other.

**Long version:** Imagine you're an app. You would rather have the data raw, without all the formatting that humans consider vital to their understanding.

If a human wanted to access my Hypothes.is profile page, they would access [https://hypothes.is/users/kureshii](https://hypothes.is/users/kureshii) and see a nicely formatted profile page.


![Screenshot of a Hypothes.is profile page](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season1/issue004/issue004_01.png)
<small>My Hypothe.is profile page. Yeah, you already saw this in Issue 2. </small>


If an app wanted a data-only view, it could access [https://hypothes.is/api/search?user=kureshii](https://hypothes.is/api/search?user=kureshii) and get the same data:


![Data from the Hypothes.is API, JSON](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season1/issue004/issue004_02.png)
<small>Raw data from the Hypothes.is API<br/>
(that’s Application Programming Interface)</small>


Cool, isn’t it? Looks very different from HTML, but still looks kinda … structured. Those \{curly brackets\} and \[square brackets\] look annoying though. How’re we ever going to work through those?

Luckily for us, this way of using curly and square brackets is pretty standardised these days. It is called JavaScript Object Notation (JSON for short). It was specified by Douglas Crockford in the early 2000s, presumably to make things easier for all of us, because it was meant to replace some competing formats, such as XML.


![Data from the Hypothes.is API, XML](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season1/issue004/issue004_03.png)<br />
<small>The same data, in XML format.<br />
(Those look like HTML tags, but they are XML tags. Don’t worry about the difference for now, I’ll write an issue about it when it matters.<br/>
Maybe when I move on to ebooks.)</small>



[![Video of Douglas pronouncing 'JSON'](https://img.youtube.com/vi/zhVdWQWKRqM/0.jpg)](https://www.youtube.com/watch?v=zhVdWQWKRqM)<br />
<small>How do you pronounce JSON? [Here’s a Youtube video](https://www.youtube.com/watch?v=zhVdWQWKRqM) of Douglas telling you he doesn’t care how you pronounce it (he pronounces it “jay-sun” like Jason, I pronounce it “jay-sawn”. Whatever.)</small>


By the way, I believe API is pronounced “ay-pee-aye”. Some people may pronounce it “ah-pee”, “ay-pee” or something. Try not to laugh.

Oops, I got sidetracked. So, Hypothes.is is really cool because they got an API that makes it easier for my app to get raw data. How do we use this API thing? And what is JSON anyway?

Next two issues: What is JSON? How do you use an API?

-----

Four issues in, and I’ve just introduced the first technical term: API. This is going to be a pattern for this newsletter: I’ll illustrate some examples that highlight a problem or issue, before I introduce the incumbent solution and the term people use to refer to it. One drawback to this approach is that the introduction can sometimes seem obtuse or confusing: “where is he going with this example?” If this should occur, the fault is mine for the poor writing.

How are the first four issues for you? Was it difficult grasping the examples and what they illustrate? Hit reply and let me know 📧 Even if you don’t think there’s anything to complain about, I would find it reassuring to know that the current format is okay.

—Jun Siang
