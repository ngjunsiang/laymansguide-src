Previously: Data packets hop from server to server. The more hops a packet must undergo, the longer the latency. The slower the servers along the route, the longer the latency as well.

Last issue, I showed the route taken by data packets being sent to google.com, and to baidu.com. We don’t know what is in those data packets (yet), so in this issue I want to show you just how many requests/responses are involved in loading a webpage. I’ll be doing so using a tool that is available in Chrome and Firefox, which you might have accidentally opened before when you pressed some unknown hotkey combination, and wondered if you broke your browser. This tool is called Developer Tools, and it opens any time you right-click something in a webpage and then click 'Inspect Element', or if you press the Ctrl-Alt-I hotkey. It shows you what the backend of a webpage looks like, and today we’ll look at one of its features.

## Loading a Github webpage

The Github repository where I keep my laymansguide files can be viewed on a webpage, and it looks like this:

<span style="text-align:center">
![Github page for laymansguide](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue038/issue038_01.png?raw=true)<br />
Github page for laymansguide
</span>

Loading this page with the Network tab of Developer Tools open produces this report:

<span style="text-align:center">
![Developer Tools showing network activity while loading a Github page](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue038/issue038_01.png?raw=true)<br />
Developer Tools, Network view
</span>

This is a summary of the network activity that is happening while the page is loading. The top ribbon, showing time in milliseconds (ms) and a series of horizontal lines, is what is known as a waterfall chart. Each line represents the loading of a resource—anything that the page requests while it is loading. Lines stacked on top of each other represent resources that are being loaded simultaneously (ideal), while lines joined end-to-end represent resources that are being loaded in tandem, one after the other (not ideal).

The resource list below it shows the resources that were loaded. You see that all kinds of files are needed: documents, stylesheets, scripts, image files (svg, gif, jpeg, png, webp), icons (.ico), and more.

Why can’t they all be loaded simultaneously to save time? Sit down and I’ll tell you a story …

## Timeline of a loading webpage

In the beginning was Void. And then:

1. `laymansguide` loads (0–673 ms), because a request was sent for it when I asked my web browser to load `https://github.com/ngjunsiang/laymansguide`. This is the first resource in the list.
2. `laymansguide` is a webpage, an HTML (HyperText Markup Language) file, which I will explain in a future issue. In the resource Inside, it contains lines like these, isolated here for your reading pleasure:

```
<link rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-2e9090135c22aad5f56c2f72dcba7880.css" />
<link rel="stylesheet" href="https://github.githubassets.com/assets/github-cbb49d8cd46cbc8c522a95d52b21ab53.css" />
<img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">
<include-fragment class="my-2"><img alt="Loading" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="32" height="32" /></include-fragment>
<img alt="@ngjunsiang" class="avatar" src="https://avatars3.githubusercontent.com/u/45561895?s=40&amp;v=4" height="20" width="20">
[...]
```

Lines like these in the document are interpreted by the web browser. They tell the browser that more resources are needed, and where they need to be loaded from (either through the `"href="` addresses or the `"src="` addresses). The web browser then sends more requests for these files. That is why you only see them loading **after** the document has loaded: my web browser has to receive and process the document first to know where to retrieve these files.

The stylesheets (files that end in .css) tell the document how to style elements in the page. I won’t elaborate on that in detail here, perhaps in a different season of laymansguide.

The images are … well, images. More on them in a future season about data types.

The scripts, ah, that’s something to go into. Unlike stylesheets are images which are just information to be inserted into the page, scripts here are actually code, usually Javascript code. This code does anomations, calculation of time conversions, and many other things, including loading more resources. I’m not going to paste that here, I don’t want to chase my readers away … okay, maybe just a couple of lines. The last script that is loaded, `github-bootstrap-747cdfeb.js`, is a companion script file for the Bootstrap\* framework that Github uses to simplify their webpage code. It has the following lines:

```
[...]
const e = function(e) {const t = document.createElement("img");
                       return t.className = "emoji"}(this);
e.src = this.getAttribute("fallback-src") || "",this.appendChild(e)
[...]
```

This creates an `img` element named `e`, styles it according to the style class `emoji`, then associates it with the address retrieved from `fallback-src`, and finally it gets appended to another element in the page through the function `appendChild`. That’s right, this code inserts emojis, so the `laymansguide` document has to retrieve those emojis first. Before this script plays, the page won’t even know that those emojis are necessary.

And now we come to the last part of the waterfall, where additional resources requested by scripts and other things are loaded. It’s not worth going through them in detail, we won’t learn much more from that. So let’s summarise.

**Issue summary:** When a webpage document loads (Stage 1), it is processed by the web browser, which then
loads other requested resources, such as stylesheets, images, and scripts (Stage 2). Scripts and other interactive code may then request more resources (data fetches, images, icons, data, etc) which are then loaded subsequently (Stage 3, 4, 5, …).

<hr/>

So far, we have identified 3 sources of latency:
1. DNS resolving ([Issue 29]()), which translates the domain names in the requests to IP addresses that we can request data from,
2. Data packet routing([Issue 37]()), which adds to latency with each hop through yet another gateway, and
3. Webpage loading (this issue), where documents or scripts that are loaded may request yet more resources.

All of these layers of information gathering can add up to a few seconds of latency—a big turnoff for folks who have come to expect near-instantaneous response from apps. And often, our pages don’t appear to take that long to load, do they?

In the next issue, the last one for this season, I’ll explain one common trick for making anything appear faster: it is called **caching**.

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
