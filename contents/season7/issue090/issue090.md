Title: Issue 90: Using a database
Date: 2020-10-03 08:00
Tags: 
Category: Season 7
Slug: lmg-s7-issue-90-using-a-database
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Graph databases treat the details of things as secondary, and optimise for managing the network of relationships. A graph database can quickly look up how things are related to each other, and return the results.

At some point in the past, getting a database meant talking to a consultant or contractor, who would then sit with you to understand your requirements, then set everything up for you without letting you touch any part of it. And that is probably for the benefit of you both. But today, for SMEs with some relevant expertise, it is actually possible to get your own database up and running very quickly.

## Setting up a database on a server

If you have admin rights to the workplace server (which can be both a blessing and a curse), you’ll have to find the setup instructions that came with the server software (or Google it online). I’m sorry, it is painful for layfolks (and even for many experienced database admins) and there just isn’t an easier way yet.

## Registering a database in the cloud

If you do not have admin rights to the workplace server, you usually ask your friendly server administrator to help you install the database and set up a web admin panel for you. They will give you a URL and login credentials for that web admin panel, and you configure the database through the database section of the admin panel.

If your company has decided to do away with organic IT support, your next bet is to outsource that help from cloud services. Each of the major cloud providers provide multiple database types for your perusal. Some app hosting services will also host a database for you (usually intended for app use, but who’s asking?).

**Relational databases**
- Amazon Relational Database Service
- Google Cloud SQL
- Microsoft Azure SQL Database

**Document databases** (You will see many of them referred to as NoSQL databases)
- Amazon DynamoDB
- Google Cloud Firestore (part of Firebase)
- Microsoft Azure Cosmos Database

**Graph databases**
- Amazon Neptune
- Microsoft Azure Cosmos also has an API ([Issue 4]({filename}/season1/issue004/issue004.md)) for graph databases

## Getting the database identifier

After you have successfully registered a database (of any type), you will be given a connection URI (Uniform Resource Identifier), which is a fancy way of saying “URL to identify your database uniquely”. It can be a simple line of text, like:

`mongodb://mongodb0.example.com:27017`

which identifies your database as a `mongodb` (document) database running on the server at `mongodb0.example.com` on port `27017`. (I covered server hostnames in [Issue 29]({filename}/season3/issue029/issue029.md) and port numbers in [Issue 33]({filename}/season3/issue033/issue033.md)).

or it can look like:

`postgres://myusername:myverylongwindedpasswordwhichisobviouslygeneratedbyacomputerandnotahuman@ec2-52-207-124-89.compute-1.amazonaws.com:5432/d77ila0heea1lk`

which identifies your database as a `postgres` (relational) database running on the server at `ec2-56-486-386-34.compute-5.amazonaws.com` on port `5432`, and your particular database is named `d77ila0heea1lk` (you can run multiple databases on a single server).

## Connecting to a database

This is where it gets a bit trickier.

If you are using another online service that integrates with your database, that service needs to know your URI and its associated information. The service will either ask your for your login/authentication credentials, hostname, and port separately, or ask for it in a single URI, or some mix of the two options.

If you are hiring your own developer (including possibly yourself), you will have to figure out which module you need to connect to the database.

For example, MongoDB in Python: `MongoClient('mongodb://mongodb0.example.com:27017')`

And for PostGreSQL in Python: `psycopg2.connect('postgres://myusername:myverylongwindedpasswordwhichisobviouslygeneratedbyacomputerandnotahuman@ec2-52-207-124-89.compute-1.amazonaws.com:5432/d77ila0heea1lk')`

**Note:** It is considered insecure to simply leave your login credentials in code like that. Please read up on best practices for importing sensitive information from more secure sources in your programming language of choice.

**Issue summary:** A URI (Uniform Resource Identifier) is required to connect to a database. This URI can be provided by a hosting service provider that runs your own database for you, or by a cloud service provider that runs your database on their platform.

Once you go through the painful process the first time, it gets easier. A lot of engineering work has been done to make this possible: connect to a database with one identifier. URIs are their own fascinating bit of information engineering, definitely not within the scope of _Layman’s Guide_. It is something to think about whenever you need to identify everything in your office or warehouse with a unique name (think barcode system or inventory/asset management).

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 91: Commercial database alternatives

What if we don’t want to do all of that? Next issue, to wrap up this season, I’ll give you some alternatives that sit somewhere between a full database solution, and a simple Excel/Google Sheets spreadsheet.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
