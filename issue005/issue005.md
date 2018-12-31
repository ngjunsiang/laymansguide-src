Say you want to send some data to another app. Let’s say it’s an annotation from Hypothes.is:

![Screenshot of a Hypothes.is highlight page](https://github.com/ngjunsiang/laymansguide/blob/master/issue005/issue005_01.png?raw=true)
A highlight in Hypothes.is, to illustrate the<br/>
various bits of info that must be sent. 

What data is included in this annotation?

– Date (and time) that the annotation was created
– user who created the annotation (that’s me!)
– The URL of the page that the annotation was made on (that’s [on NYT](https://www.nytimes.com/2017/10/18/magazine/when-the-revolution-came-for-amy-cuddy.html))
– A link to the URL of the annotation (the [permalink](https://hypothes.is/a/4mN0juVuEeipmD-559uHoQ) you can use to bring someone straight to your annotation)
– Permissions: is this annotation visible to public or only to certain groups?

Besides the above, there is also some information my app may need to make things easier:
– A unique id for the annotation so that I can refer to it again. That's the jumbled text you see in the URL, “4mN0juVuEeipmD-559uHoQ”
– Whether there were any replies to the annotation (the picture above shows an annotation and a reply to it)
– Document title
– Tags, usually used for organising lots of annotations

How is the data from the API going to tell you which bits are which?

It could do it with a bulleted list like I used above. But what if there were multiple replies and I need sub-bullets? How do I differentiate data that is a simple list `[a,b,c]` vs a mapping of values `{"name": a, "date": b, "user": c}`?

XML, which you saw in the previous issue, is one way to do it. JSON ([https://www.json.org/](https://www.json.org/)) is another way. The JSON way minimises the number of extra text you need to structure the data nicely. This is a big deal when you are sending data over the internet, for billions of users.

XML, with its XML tags, often balloons in data size (see [this example](https://www.xml.com/pub/a/2004/12/15/deviant.html) where an Excel spreadsheet was exported to both XML [840MB!] and CSV [34MB]). Each bit of data that is sent has a cost with it; no doubt if you have a mobile data plan you will know what I mean. In software engineering, we have a term to describe this, borrowed from business: we say that it has **immense overhead**.

What? You mean processing XML requires money? Of course! Think about it:
– Visually, it takes longer to read and skim through XML, which takes up precious time for software engineers
– More data needs to be sent for an XML packet than for, say, a JSON packet, which either takes more time on a connection or costs more for services that charge per unit of data
– It requires more computing resources to process more data: all that data needs to be copied to the processor for processing, which means that it takes marginally longer to process the same data in XML vs other formats, all else being equal. And processing time is precious, even if hardware is cheap; there is just so much other data to process!

Amid other competing standards, JSON won out and became a de facto standard for applications to exchange data. Which makes things a little easier for everyone: when we can agree on one de facto standard, everyone knows they gotta make things that support it. So it’s really easy to find something that can help me process JSON.

![Data from the Hypothes.is API, JSON](https://github.com/ngjunsiang/laymansguide/blob/master/issue005/issue005_02.png?raw=true)
The same annotation, in JSON format

Issue summary: JSON is the de facto data format for sending data over the web. Almost everything you use that was updated significantly in the last 5 years is probably using JSON-formatted data in some way.

Next issue: How do you use an API (to send/receive JSON)?
