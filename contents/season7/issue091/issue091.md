[**Previously:**](https://buttondown.email/laymansguide/archive/) A URI (Uniform Resource Identifier) is required to connect to a database. This URI can be provided by a hosting service provider that runs your own database for you, or by a cloud service provider that runs your database on their platform.

So you’re running up against the limits of a spreadsheet and want to do more with the data inside it. Databases sound cool and kind of like what you want right now. But writing a whole app and setting up the database yourself, or even getting someone else to do it and checking their work ... it all sounds like so much.

What to do?

## Airtable

[Airtable](https://airtable.com/) is a database-like platform that lets you set up Bases (similar to databases), which can contain different tables for your data. You can specify a specific data type for each table, limit entries to a list of options, and even create lookups (match the value here with a column in another table, and return data from another column in the same row).

Just as databases don’t have a single canonical view, and everything depends on queries, Airtable also lets you create different views of your data. You can set it up as a list, a gallery, a job status board, and filter it as you like.

Interestingly, Airtable also dynamically generates an API for each of your bases, so that apps you create have a way to retrieve, modify, or delete data from the database. That saves you a lot of trouble having to set up your own database, for simple needs.

## Smartsheet

[Smartsheet](https://www.smartsheet.com/platform) is another platform that lets you create sheets with different views. Unlike Airtable, is leans more heavily towards workplace workflows, with built-in task management features and integration with many services. If you are already using one or more of these services, Smartsheet could be a way to store information for collaboration.

## Knack

[Knack](https://www.knack.com/tour) is yet another database-as-a-platform, which also allows you to craft queries to extract the data you need. It has an interesting feature that lets you specify how tables relate to each other (e.g. Contact connects with _one_ Company, Company connects with _many_ contacts) to improve queries.

Knack also lets you create simple apps with limited access to the data, for employee or customer use. If you mainly need internal apps for disseminating or allowing field access to data, this is probably a simpler option than hiring an app programmer/company.

## Zoho Creator

[Zoho Creator](https://www.zoho.com/creator/) is a database platform that is more focused on app-building (or so it appears). The database just comes bundled as part of the deal. Another option for corporate operations-focused apps.

**Issue summary:** Depending on what you need a database for, there may be online database platforms that can manage and automate much of the work for you. Airtable, Smartsheet, Knack, and Zoho Creator are just 4 of many options that offer an easier way to set up and input your data, then access them through apps or other means.

The best thing about these cloud services is that you probably don’t need to learn SQL or other advanced query languages to use them. A passing familiarity with spreadsheets, and time to sit down and watch tutorial videos, is probably sufficient to get started.

## What I’ll be covering next

**Next issue:** [LMG S8] Issue 92: All about apps

I’ve spent a whole season talking about data ([Season 4, Issue 40](https://buttondown.email/laymansguide/archive/lmg-s4-issue-40-bits-and-bytes/) to [Issue 52](https://buttondown.email/laymansguide/archive/lmg-s4-issue-52-pdfs-part-2-text-and-images/)), then detoured to talking about computers, and the internet, and now back to databases. I think that’s plenty of foundation to finally move on to something more familiar: apps.

What exactly are apps and what do they do? What are they like under the surface? What makes them tick?

This and more in Season 8 ... which will start after a two-week hiatus. It has been really fun putting finger to keyboard and watching everything come together, but I noticed the quality of recent issues has been sliding more than I’d like. I’m going to take a little break to reconsolidate, recuperate, and think about the next couple of seasons.

See you next issue!

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
