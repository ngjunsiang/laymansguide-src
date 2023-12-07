Title: Issue 89: Graph Databases
Date: 2020-09-26 08:00
Tags: 
Category: Season 7
Slug: issue089
Author: J S Ng
Summary: 
Modified: 2020-09-26 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Document databases organise data into documents, each containing a number of field-value pairs. each value can itself be a document, and multiple values/documents can be grouped under a field. Document databases do not enforce data consistency across documents, so those rules need to be managed by the application which is using the database. This allows document databases to continue operating even when partitioned, at the cost of some consistency.

In the past two issues, I laid out how relational databases primarily focus on the **relations** between tables, while document databases primarily focus on organising data into **documents**. I’ll look at one more application today.

If I’m trying to start a new social media platform today, I would have to store posts and user account data into a database. Which type of database should I use?

I could use a relational database, but joining multiple tables to get a chain of posts, Twitter-style, could get ugly and involve lots of lookups … that is going to be one laggy service at scale!

I could use a document database, but it would involve retrieving each post one at a time, searching to find posts which are linked to it, and then checking which posts are linked to those posts … that is too many searches!

Maybe I’m approaching this wrong. I don’t need to relate many different types of tables or retrieve self-contained documents here. I am actually trying to store a humongous, densely linked network of data—a graph!

## What?

Okay, stay with me here, I know you are thinking of a horizontal and a vertical axis, and axis labels and bars and lines and—that’s not the kind of graph I am talking about.

> “In mathematics, graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects.”  
> — [Graph theory (Wikipedia)](https://en.wikipedia.org/wiki/Graph_theory)

That’s what I’m talking about. And it looks like this:

<figure>
    ![Wikipedia multilingual network graph, showing circles representing languages, and arrows between pairs of circles, representing editors who edited both languages.]({attach}/season07/issue089/issue089_01.png)
    <figcaption>This network graph shows the co-editing patterns on Wikipedia. The size of the arrows indicate the number of Wikipedia editors for one language edition of Wikipedia, who also edited another language edition.<br />Source: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Wikipedia_multilingual_network_graph_July_2013.svg)</figcaption>    
</figure>

Okay, phew.

## Graph databases: a network of relationships

So if I’m going to make a social media platform that can retrieve chains of posts, how would a graph database make it easier?

A graph database will still need to have some data for the users and posts:

```
personA:User {name:"Alice"}
personB:User {name:"Bob"}
...
post001:Post {tags:"...", contents:"..."}
post002:Post {tags:"...", contents:"..."}
...
```

But the heart of the graph database is the data that stores the relationships between those users and posts:

```
(personA)-[:SAYS_TO {message:"..."}]->(personB)
(personB)-[:SAYS_TO {message:"..."}]->(personA)
...
```

If I want to lookup a conversation between Alice and Bob, I can search for `SAYS_TO` relationships with Alice and Bob at either end of the relationship arrow (`-->`), and sort the results in chronological order.

## Graph databases put relationships first

What about posts and comments? For social media, we can treat them as the same type of data (`Post`), but link them with relationships:

```
(personA)-[:WROTE {datetime:"..."}]->(post001)
(personB)-[:WROTE {datetime:"..."}]->(post003)
(personC)-[:WROTE {datetime:"..."}]->(post005)
(personD)-[:WROTE {datetime:"..."}]->(post007)
(personA)-[:WROTE {datetime:"..."}]->(post011)
(personB)-[:WROTE {datetime:"..."}]->(post013)
(personA)-[:WROTE {datetime:"..."}]->(post017)
...
(post003)-[:REPLY_TO {datetime:"..."}]->(post001)
(post005)-[:REPLY_TO {datetime:"..."}]->(post003)
(post007)-[:REPLY_TO {datetime:"..."}]->(post003)
(post011)-[:REPLY_TO {datetime:"..."}]->(post005)
(post013)-[:REPLY_TO {datetime:"..."}]->(post011)
(post017)-[:REPLY_TO {datetime:"..."}]->(post013)
...
```

Because the relationships contain only the bare minimum data for figuring out the network, they are quick to search through. I don’t have to load the names, post tags, post contents, and other irrelevant detail.

Although I would still have to retrieve `post001`, check for replies, check those replies for replies, and so on, this is much faster with relationships between labels. A graph database optimises for this type of lookup.

Once I have figured out which users and posts are involved in this chain, I can then retrieve their information in a subsequent query. I won’t even need to load all the information at a go, since the app user is not going to see the contents of later posts until they scroll.

**Issue summary:** Graph databases treat the details of things as secondary, and optimise for managing the network of relationships. A graph database can quickly look up how things are related to each other, and return the results.

So there you go, three types of databases in three weeks. I picked these three because they’re the least technical to give an overview of (in my opinion), and are three different ways of thinking about data that I think you are likely to encounter.

There are, of course, other types of databases: key-value stores (used heavily in web browsers), wide column databases, search databases (very similar to document-based), … but beyond this point the differences are primarily technical, and not really suitable for this newsletter.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 90: Using a database

I’ve been cracking my head trying to come up with 2 more topics to round up this season on databases. I suppose most layfolks would (hopefully) never ever have to start or run their own database. But it could be helpful to know what is needed to get a database up and running, and the most common ways of getting access to one. Expect a short issue next week.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
