YOu would think that the first challenge in writing an app is learning the programming language. In my case, there was an even more fundamental challenge to overcome first: how to get my data.

We don’t think about who actually owns the data you upload onto the internet until it is too late. You access your photos by logging in to Instagram, your tweets by logging in to Twitter, and everything else by logging in to something else. Until one of more of these services break down or you get tired of them and you want out, you would never even think about the fact that you often can’t get all this data out except by manually opening each and everyone one of them and saving them to your disk. But I will need some way to get my data out from Hypothes.is, or my app is not going to happen …

“Well, maybe if I learn programming and figure out a way for an app to load these pages and save them automatically, it could go a lot faster.” It certainly can; this method is called page scraping (more on this possibly in a future issue; but not now). But it means your app will have to deal with HTML data, like this:

![Snippet of the Instapaper page source, in HTML](https://github.com/ngjunsiang/laymansguide/blob/master/issue003/issue003_01.png?raw=true)
Instapaper page source. That’s HTML.

Whoa. I may have intentionally formatted it to make it look more dense, but I mean no deceit; in fact, this is closer to what your app has to deal with than nicely formatted code (which will have you tearing your hair out when you have to strip out all the newlines and spaces and tabs from it).

Instapaper’s Notes page is actually not complex; visually it looks like this (I have cropped the sidebar since that didn’t appear in the code chunk above):

![Screenshot of my Instapaper notes page](https://github.com/ngjunsiang/laymansguide/blob/master/issue003/issue003_02.png?raw=true)
Instapaper notes page. Sidebars have been cropped off.

What are all those things (they’re called HTML tags) doing in the page source? They tell the browser how to format the text, usually to appeal to internet users. But when all you want is the raw data, these tags are annoying and tedious to sort through and remove.

Isn’t there an easier way to just get only the data? Why yes; it is known as an Application Programming Interface, or API.

Next issue: What is an API?
