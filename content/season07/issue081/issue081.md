Title: Issue 81: Data Normalisation
Date: 2020-07-25 08:00
Tags: 
Category: Season 07
Slug: issue081
Author: J S Ng
Summary: 
Modified: 2020-07-25 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) An index is a separate table containing key terms in the database (usually names, IDs, or some other key identifier), alongside the row numbers where they are found. An index greatly speeds up row lookups, but slows down the writing of new rows.

In this post, I will use CSV format to describe data, although if you have followed this season from the start you would be aware that in a database, this data would not be in text form. Nonetheless, at this point it would be represented similarly.

If we were constructing a database of blog posts from multiple authors of a blog, we might organise the post data like this:

```
id,author,title,content
1,knowitall,Why the world is falling apart,blahblahblah…
2,knowitall,Make the world great again,blahblahblah…
3,whatsgoingon,Why have things come to this,blahblahblah…
```

Later, when the authors start to add avatars and other information to their profile, the table might grow:

```
id,author,avatarURL,about,title,content
1,knowitall,http://avatars.me/knowitall.jpg,I know everything!,Why the world is falling apart,blahblahblah…
2,knowitall,http://avatars.me/knowitall.jpg,I know everything!,Make the world great again,blahblahblah…
3,whatsgoingon,http://avatars.me/whatsgoingon.jpg,Curious about the world,Why have things come to this,blahblahblah…
```

And when we start to add post tags:

```
id,author,avatarURL,about,title,content,tags
1,knowitall,http://avatars.me/knowitall.jpg,I know everything!,Why the world is falling apart,blahblahblah…,daily+apocalypse
2,knowitall,http://avatars.me/knowitall.jpg,I know everything!,Make the world great again,blahblahblah…,daily+ambition
3,whatsgoingon,http://avatars.me/whatsgoingon.jpg,Curious about the world,Why have things come to this,blahblahblah…,essay+apocalypse
```

What problems are we going to run into with a table like this?

## Suboptimal table forms

Even with constant-width tables and pre-determined data types, plus speeding up lookups with indexes, we will run into some issues as the number of posts grows:

1. **Duplication of data**  
   The avatar URL and About description (for the author) are repeated in each post. In a real blog, where these are often longer and you might have more contact information about each author (such as contact info), the amount of duplicated data is simply wasteful.
2. **Difficult data extraction**  
   Notice that the tags are all jammed up into one column. How would we search for all posts with the "apocalypse" tag?  
   We would have to retrieve each row one by one, split up the tag strings, and check if "apocalypse" is in there … that’s really slow!

## Data normalisation: making data atomic

When data is really complex, it makes sense to split it up and make it **atomic**. When data is atomic, it means that it has been broken down to the lowest level of detail; typically this would mean individual records that avoid duplication.

For instance, we might have an `Author` table:

```
ID,name,avatarURL,about
1,knowitall,http://avatars.me/knowitall.jpg,I know everything!
2,whatsgoingon,http://avatars.me/whatsgoingon.jpg,Curious about the world
…
```

And a `Posts` table:

```
ID,authorID,title,content
1,1,Why the world is falling apart,blahblahblah…
2,1,Make the world great again,blahblahblah…
3,2,Why have things come to this,blahblahblah…
…
```

What to do with the `Tags`? Often a database designer will create a `Tags` table like this:

```
ID,tag
1,daily
2,apocalypse
3,ambition
4,essay
…
```

and a `PostTags` table like this:

```
postID,tagID
1,1
1,2
2,1
2,3
3,2
3,4
…
```

This process of splitting up a complex data set into atomic, related data fields is known as **data normalisation**. A data set that is not normalised will make it difficult to do lookups efficiently as new needs arise later.

## Advantages of data normalisation

The first advantage you can see above is that retrieving author-only data, post-only data, etc is now much faster. We don’t have to pull up a whole lot of other unrelated information, incurring unnecessary data transfer overhead.

The second advantage you can see is that entities—authors, posts, tags—are now referred to by an ID. An ID is usually a number, which is represented more compactly in a computer in binary form as compared to a name or title in text form (Issue 79). This allows our program to carry out any processing on relationships between these entities much more quickly (e.g. “how many posts does this author have?” “How many posts have this tag?”), with lower data transfer overhead.

## Disadvantages: greater complexity

The disadvantage is that pulling data together to render a blog post on a webpage now involves looking up three different tables and joining the data together. Each query is going to involve multiple lookups and joins, and is going to require many lines of code … if each programming language is going to come up with its own way of writing these lookups and joins, and each new database format also comes up with its own commands, very soon we would have a huge unmaintainable mess of syntax and commands to learn!

So programmers and database designers came together and came up with a *new language* to do lookups and joins: Structured Query Language, or **SQL**. This is the reason why today you can write SQL queries that will work on a Microsoft SQL (MSSQL), PostGreSQL, MySQL, or MariaDB database; they all support SQL!

**Issue summary:** Putting all data into one table results in unnecessary duplication of data. Making data atomic by splitting it up into multiple tables makes the data easier to work with, but requires multiple lookups and joins to get the required data. A standard database language, SQL, makes it possible to write queries that are supported by multiple databases.

I am jumping ahead of myself a little here; I’ll only talk about SQL a couple of issues later. Before I go into what SQL does, there are two features our program does not yet support: allowing multiple users to read and write data, and setting access permissions on data.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 82: Multiplayer databases

> “The action can’t be completed because the file is open. Close the file and try again.”

How often have you run into this error on Windows?

This makes it difficult for multiple users to work on a file at the same time. How do databases work around this? Find out in the next issue!

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
