[**Previously:**](https://buttondown.email/laymansguide/archive/) Relational databases are designed to maintain a well-structured set of data tables through constraint rules. This makes them very useful for preventing accidental inconsistencies in data, but make any changes to the data schema difficult to implement. Changing from one schema to another involves downtime and a migration.

One problem I keep running into with Excel is when I *think* the data has a consistent structure, but halfway through I realise that it actually doesn’t: sometimes I might have two students with different categories of accomplishments, and that requires a big change in the way I design the columns.

## Document databases: a collection of fields and values

Document databases bypass this problem by not enforcing a strict schema on the data. That is not to say you can’t; it is *optional* and up to you to enforce.

These documents are not the ones we have in mind; they are simply bits of data grouped together. Each bit of data is described by a field. For example, I might start out defining a student document this way:

```
{
  name: "Harry Potter",
  school: "Hogwarts School of Witchcraft and Wizardry",
  characteristics: "lightning-shaped scar on forehead"
}
```

I can add more fields later, if I wish:

```
{
  ...
  mother: Lily Potter,
  father: James Potter,
  ...
}
```

But what makes document databases truly document-oriented is the way they can be nested. Suppose I want to expand a bit more on this student’s education, to include the years of study. I could expand each entry in the `school` field to include that:

```
{
  name: "Harry Potter",
  school: {
    name: "Hogwarts School of Witchcraft and Wizardry",
    start: "1991",
    end: "1997"
  }
  characteristics: "lightning-shaped scar on forehead"
}
```

Yup, now I’ve just expanded the value of the `school` field into ... another document! This document has a `name` field, a `start` field, and an `end` field. and I can do this just about any place I want.

I can also group multiple values under a field:

```
{
  ...
  characteristics: ["wears glasses", "lightning-shaped scar on forehead"]
}
```

I can also group multiple *documents* under a field. It’s documents all the way down!

## Collections: the only way to organise documents

While relational databases have tables for organising rows, document databases have collections for organising documents.

Each collection can contain multiple documents. There is no constraint on what kind of documents each collection can contain.

I could have a collection for teachers, one for students, one for subjects, one for classes, etc, with each as a document.

## What can I do with a document database?

Just about ... anything? If you can think of a way to organise the data as documents, you can put it into a document database.

A document database lets you find documents based on its fields. I can look up all documents which have a `name` field, or check that the word "Harry" is in the `name` field. I could look for students who enrolled in the year "1991" or later, or more specifically students who enrolled in "Hogwarts School of Witchcraft and Wizardry" in "1991" or later.

## Drawbacks

Since this is not a relational database, you don’t have the protection of foreign keys and other features that stop you from making the data inconsistent—there’s no concept of enforced consistency here! You’ll have to write those rules into your app when it accesses the document database; the database won’t enforce them for you.

## Advantages

Data organised as documents tends to be more self-contained. Since the database does not enforce consistency, it has less to worry about when edits or changes are made to the database. In a distributed document database, we thus sacrifice some consistency.

The advantage this provides is that when the distributed document database suffers a network outage that partitions it into multiple subclusters ([Issue 86]()), the database can continue to operate. Over time, each subcluster will become less and less consistent, since changes in each subcluster are not synchronised to other subclusters.

Once the network issue is resolved and the subclusters are synchronised again, these changes can be merged (with rules for resolving conflicts) subsequently. The database remains operational throughout the ordeal, just with some desynchronisation.

**Issue summary:** Document databases organise data into documents, each containing a number of field-value pairs. each value can itself be a document, and multiple values/documents can be grouped under a field. Document databases do not enforce data consistency across documents, so those rules need to be managed by the application which is using the database. This allows document databases to continue operating even when partitioned, at the cost of some consistency.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 89: Graph Databases

Okay, relational and document databases were easy enough. They are more easily mapped to spreadsheets and file/folder hierarchies, respectively.

But now we go up the abstraction ladder, and get to more abstract ideas of data. In a social network, the user profile is usually the least significant part of the account; what often matters most is how this account is linked to other accounts (followers and following). The study of such interlinked objects is known in mathematics as **graph theory** (nope, not the kind of graphs we are so used to in reports). This is where terms like “social graph”, the representation of your social network on Facebook or Twitter, comes from.

What is the most intuitive way to represent, store, and modify this kind of graph data? Using a graph database, of course.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
