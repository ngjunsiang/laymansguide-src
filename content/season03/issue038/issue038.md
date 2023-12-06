Title: Issue 38: Loading a web page
Date: 2019-09-14 08:00
Tags: 
Category: Season 3
Slug: lmg-s3-issue-38-loading-a-web-page
Author: J S Ng
Summary: 

**Previously:** Data packets hop from server to server. The more hops a packet must undergo, the longer the latency. The slower the servers along the route, the longer the latency as well.

Last issue, I showed the route taken by data packets being sent to google.com, and to baidu.com. We don’t know what is in those data packets (yet), so in this issue I want to show you just how many requests/responses are involved in loading a webpage. I’ll be doing so using a tool that is available in Chrome and Firefox, which you might have accidentally opened before when you pressed some unknown hotkey combination, and wondered if you broke your browser. This tool is called **Developer Tools**, and it opens any time you right-click something in a webpage and then click 'Inspect Element', or if you press the `Ctrl-Alt-I` hotkey. It shows you what the backend of a webpage looks like, and today we’ll look at one of its features.

## Loading a Github webpage

The Github repository where I keep my laymansguide files can be viewed on a webpage, and it looks like this:


![Github page for laymansguide]({attach}/season3/issue038/issue038_01.png)<br />
<small>Github page for laymansguide</small>


Loading this page with the Network tab of Developer Tools open produces this report:


![Developer Tools showing network activity while loading a Github page]({attach}/season3/issue038/issue038_02.png)<br />
<small>Developer Tools, Network view</small>


This is a summary of the network activity that is happening while the page is loading. The top ribbon, showing time in milliseconds (ms) and a series of horizontal lines, is what is known as a _waterfall chart_. (You can also see this chart in the rightmost column below the ribbon.)

Each line represents the loading of a resource—anything that the page requests while it is loading. Lines stacked on top of each other represent resources that are being loaded simultaneously (ideal), while lines joined end-to-end represent resources that are being loaded in tandem, one after the other (not ideal).

The resource list below it shows the resources that were loaded. You see that all kinds of files are needed: documents, stylesheets, scripts, image files (svg, gif, jpeg, png, webp), icons (.ico), and more. The vertical blue line represents the point where the web browser has loaded and processed the main document (first item in the resource list). The vertical red line represents the point where the webpage is considered to be loaded (able to display its main content), while secondary resources are still loading in the background.

Why can’t they all be loaded simultaneously to save time? Sit down and I’ll tell you a story …

## Timeline of a loading webpage

In the beginning was The Void. And then:

1. `laymansguide` loads (0–673 ms), because a request was sent for it when I asked my web browser to load `https://github.com/ngjunsiang/laymansguide`. This is the first resource in the list.
2. `laymansguide` is a webpage, an HTML (HyperText Markup Language) file, which I will explain in a future issue. Inside, it contains lines like these, isolated here for your reading pleasure:

```
<link rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-2e9090135c22aad5f56c2f72dcba7880.css" />
<link rel="stylesheet" href="https://github.githubassets.com/assets/github-cbb49d8cd46cbc8c522a95d52b21ab53.css" />
<img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">
<include-fragment class="my-2"><img alt="Loading" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="32" height="32" /></include-fragment>
<img class="avatar" src="https://avatars3.githubusercontent.com/u/45561895?s=40&amp;v=4">
[...]
```

Lines like these in the document are interpreted by the web browser. They tell the browser that more resources are needed, and where they need to be loaded from (either through the `"href="` addresses or the `"src="` addresses). The web browser then sends more requests for these files. That is why you only see them loading **after** the document has loaded: my web browser has to receive and process the document first to know where to retrieve these files.

The stylesheets (files that end in `.css`) tell the document how to style elements in the page. I won’t elaborate on that in detail here, perhaps in a different season of laymansguide.

The images are … well, images. More on them in a future season about data types.

The scripts, ah, that’s something to go into. While stylesheets and images are just information to be inserted into the page, scripts are actually code, usually Javascript code.

This code does animations, calculation of time conversions, and many other things, including loading more resources. I’m not going to paste the whole script here, I don’t want to chase my readers away … okay, maybe just a couple of lines. The last script file that is loaded, `github-bootstrap-747cdfeb.js`, is a companion script file for the Bootstrap[^1] framework that Github uses to simplify their webpage code. It has the following lines:

[^1]: [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) is a [front-end]({filename}/season2/issue014/issue014.md)) [framework]({filename}/season2/issue018/issue018.md)) that makes it easy to create webpages. By loading a standard Bootstrap stylesheet and (optionally) a Bootstrap script, any front-end developer can add common elements (e.g. popovers, navigation bars, tooltips, cards, …) with fewer lines of code than if they wrote it from scratch.

```
[...]
const e = function(e) {const t = document.createElement("img");
                       return t.className = "emoji"}(this);
e.src = this.getAttribute("fallback-src") || "",this.appendChild(e)
[...]
```

This creates an `img` element named `e`, styles it according to the style class `emoji`, then associates it with the address retrieved from `fallback-src`, and finally it gets appended to another element in the page through the function `appendChild`. That’s right, this code inserts emojis, so the `laymansguide` document has to retrieve those emoji image files first. Before this script plays, the page won’t even know that those emojis are necessary.

And now we come to the last part of the waterfall, where additional resources requested by scripts and other things are loaded. It’s not worth going through them in detail, we won’t learn much more from that. So let’s summarise.

**Issue summary:** When a webpage document loads (Stage 1), it is processed by the web browser, which then
loads other requested resources, such as stylesheets, images, and scripts (Stage 2). Scripts and other interactive code may then request more resources (data fetches, images, icons, data, etc) which are then loaded subsequently (Stage 3, 4, 5, …).

-----

**Bonus content:** I tried this with the Baidu homepage, which looks like this:


![Baidu homepage]({attach}/season3/issue038/issue038_03.png)<br />
<small>Baidu homepage</small>


and the network activity from loading it:


![Developer Tools showing network activity while loading Baidu homepage]({attach}/season3/issue038/issue038_04.png)<br />
<small>Developer Tools, Network view</small>


It takes slightly longer (about 400 ms longer) to load, but most of that time is from loading a single `gif`. I wont examine the elements here, in the season on the internet cloud, I’ll explain more what some of these elements do.

So far, we have identified 3 sources of latency:

1. DNS resolving ([Issue 29]({filename}/season3/issue029/issue029.md))), which translates the domain names in the requests to IP addresses that we can request data from,
2. Data packet routing ([Issue 37]({filename}/season3/issue037/issue037.md))), which adds to latency with each hop through yet another gateway,
3. Webpage loading (this issue), where documents or scripts that are loaded may request yet more resources.

All of these layers of information gathering can add up to a few seconds of latency—a big turnoff for folks who have come to expect near-instantaneous response from apps. And often, our pages don’t appear to take that long to load, do they?

In the next issue, the season finale, I’ll explain one common trick for making anything appear faster: it is called **caching**.

## What I’ll be covering next

**Next issue:** What are caches? What is caching?

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n’s in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML [Issue 38]
