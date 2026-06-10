Title: Issue 168: Search engines
Date: 2022-04-16 08:00
Tags: 
Category: Season 13
Slug: issue168
Author: J S Ng
Summary: A search engine uses bots to build up a database of URLs and their contents. The search engine uses various algorithms to determine the most relevant results for a search request.
Modified: 2022-04-16 08:00

**Previously:** Fragmentation is likely a contributor of system slowdown, particularly for mobile devices: the database used by most mobile apps tend to store data in many small chunks rather than fewer big chunks, which slows down data search operations. The most effective measure for improving device responsiveness is usually to clear the app cache, so the app does not attempt to read previous data from storage.

Last issue, we shed a little light on the mystery of why phone and laptop systems slow down over time—apparently the way a file database works is to blame?

This week, we switch topics, to look at something we definitely take for granted: search engines!

## What is a search engine?

Forgive me if you think I am belabouring the obvious. There is the user definition, which is something like “a search box that answers my questions”. Then there is the developer definition which is more like “an indexed database of URLs, descriptions, and ranks”. Let’s unpack that.

## Indexing and arachnids

Another obvious point: at the point when you submit your search query, there is no way the search engine could have trawled the entire internet so quickly to give you the results. It must have know about these pages beforehand ... but how?

Search engines run “bots”, also know as web spiders, or web crawlers. These are programs that retrieve pages, makes a note of the content (text, images, links, …) on that page, determine keywords for that page, and then follows the links to other pages and repeats the process. Like following the links of a (very messy) web![^1]

[^1]: Yep, we all know spiders don’t actually do this.

When we “search the internet”, we are really searching the database that has been built up by these bots.

## Ranking results

So there’s a huge database … how does the search engine determine which are the most relevant results?

Google’s PageRank algorithm is by now well known for disrupting the old directory-based method of organising information, and built for Larry Page and Sergey Brin a sizable empire. This is one way of determining how important/useful a page is: by seeing how many other pages link to it. There are other ways, but this is a layman’s newsletter and I don’t want to dive into a technical analysis and comparison of different ranking algorithms 😬

Instead, consider that there are by now many different algorithms for determining the relevance of database entries for each search, even within Google itself. A search engine is essentially a way to access this database, use one or more appropriate algorithms to determine the most relevant results, and return them to the user.

**Issue summary:** A search engine uses bots to build up a database of URLs and their contents. The search engine uses various algorithms to determine the most relevant results for a search request.

I know ... nobody really cares *how* a search engine works. We just want to know *why* it's not giving us the results we want!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 169: Search engine optimisation

I am not a consultant for search engine optimisation (SEO), but we can look at some of the ways people attempt to “game the system” and exploit features of the algorithms that search engines use. More next week!
