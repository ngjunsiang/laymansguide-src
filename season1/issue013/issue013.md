Last issue I compared HTTPS and HTTP, and explained why you should use HTTPS as far as possible to keep your data secure.

## How would I know if I’m using HTTP or HTTPS?

Most web browsers now indicate whether you are using HTTP or HTTPS in the address bar.

</div>
![The difference between Chrome 67 and 68](https://github.com/ngjunsiang/laymansguide/blob/master/issue013/issue013_01.png?raw=true)
Since version 68, Google Chrome marks HTTP sites as insecure in the address bar
</div>

</div>
![Firefox address bar: HTTP](https://github.com/ngjunsiang/laymansguide/blob/master/issue013/issue013_02.png?raw=true)<br/>
![Firefox address bar: HTTPS](https://github.com/ngjunsiang/laymansguide/blob/master/issue013/issue013_03.png?raw=true)
Firefox uses a green lock icon in the address bar to indicate that you are using HTTPS to access the website
</div>

I can’t possibly keep you updated on how every single browser informs you that you are using HTTPS instead of HTTP, so here’s a guideline instead: look for a lock icon, a green instead of red icon, or something that says “secure” and not “insecure”.

If you are still not sure, click the green/lock icon for more information:

</div>
![Firefox connection information dialog](https://github.com/ngjunsiang/laymansguide/blob/master/issue013/issue013_04.png?raw=true)
Firefox displays additional information when you click on the lock icon. Other browsers do this as well.
</div>

## How do I actually use HTTPS?

**Short answer:** When you type a URL in the web browser, make sure you specify the HTTPS method (https://) in front.

**Long answer:** In 2018, when you type a URL in a web browser and go, most websites will direct you to their HTTPS site. Most sites won’t even let you access their HTTP webpage anymore; going to their HTTP webpage returns a 301 error (see Issue 8) forcing you to be redirected to their HTTPS webpage.

So as long as you see a green and/or lock icon in the address bar, you are already using HTTPS.

Issue summary: Most web browsers use a visual indicator, often a green or lock icon, to let you know that you are using an HTTPS connection. HTTPS is the default connection method for webpages these days and it is quite unlikely you will be able to access an HTTP site.

<hr/>

## End of file

I just finished another short issue arc about authentication and encryption! Phew, I hope it wasn’t too complicated.

Congrats: you have been reading this newsletter for a quarter of a year! I’m ending this issue set here, to give it a nice theme. Maybe I’ll name it “Ask and You Shall Receive”. Or maybe not. I’m not too good with names, reply and let me know if you have a cool one :)

Of course, this isn’t all there is to know about HTTP and HTTPS and APIs, but my purpose here is to help layfolks know the things they should know while getting around the internet, and I hope I’ve convinced more people that

1. APIs are really cool (I’ll likely touch on this again in future issue sets)
2. Wifi is really unsafe if you are using HTTP
3. You really should be using HTTPS as far as possible. You don’t need to worry about it too much, since you are likely already using it.

In the next issue set, I’ll talk a bit about how software developers do their jobs. Again, the issue set will only cover the basic ideas. There are some really cool ideas that I want you to know already exist and are being used, even if I won’t be getting into the technical detail.

If you have ideas for things you would like to have a basic explanation of, let me know in an email reply!

## What I’ll be covering next

**Next issue set:** How do developers do their job?

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those ‘\r\n’s in the HTTP request packet [Issue 12]?
