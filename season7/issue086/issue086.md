[**Previously:**](https://buttondown.email/laymansguide/archive/) Forms that naïvely inject user-submitted data into a SQL query template may end up sending valid SQL commands to the database, with disastrous consequences.

So far, we have been assuming that the database runs from a single computer, and all its data is stored on one as well. What happens when it outgrows this single computer?

We could add more disk space, more memory, more cores on the processor; this is called **vertical scaling**/**scaling up** (because we are increasing the performance of the computer, which usually *feels* like pushing up the performance bar on the vertical axis of a graph).

Or we could spread that database over two or more computers. And keep them constantly synchronised. This is called **horizontal scaling**/**scaling out** (because we are adding more computers, which is usually depicted as adding more units on a horizontal axis).

We can only take vertical scaling so far; at some point we will have the most powerful server possible and it still won’t be enough. So if we are expecting massive growth, that means we will need a **distributed database**.

## Wait, who actually expects a database to not have to store *a lot* of information?

There are tiny databases out there!

These are often used in places where the task is not expected to grow beyond a single PC. For example, the database that stores your WhatsApp messages on your mobile phone, or a tiny database that stores records from a remote standalone sensor. These databases are designed to be extremely efficient at handling small amounts of data, to use very little memory, and/or to ensure that data is always written securely.

## Okay, fine. Back to distributed databases

Buying more computers to run a server is similar to hiring more employees to do the company’s work. The good: you now have more help. The bad: you now have to talk to them! Regularly!

In distributed databases, there are three factors that are impossible to achieve together in full:

- **C**onsistency — reading the same data multiple times should not give us different results
- **A**vailability — we should get a response from the database quickly
- **P**artition tolerance — If network disruptions or software/hardware failures break communication, the system should still continue to operate

This is known as the **CAP theorem**: you can only really prioritise two out of the three factors.

## Consistency and Availability

The database we have been examining so far in Season 7 are known as relational databases, which handle data in the form of tables. When implemented as a distributed database, they often prioritise consistency and availability.

How does that work? When our distributed database is being hit with 100,000s of requests per second, more than one computer can handle, we need multiple computers to serve these requests. These computers had better be synchronised (to achieve consistency) so that the request will always return the same response from any of those computers.

One way to achieve this is to have a Single Source of Truth: perhaps we design it so that only one “leader” computer handles edits/changes to the database, which then get sent to all the other “follower” computers. (This assumption that reading data occurs much more frequently than writing/changing data holds up for most use cases.) What happens if the “leader” computer goes down—our distributed database go from a leader-follower system to a partitioned bunch of followers? No writes can happen, the system is no longer operational.

(There are multiple theorems on how to design this system to automatically/manually select a new leader, but I won’t go into that here. The fundamental problem of ensuring consistency and availability in such cases remains.)

## When a partition happens

So it comes down to this: when communication failure happens in a scenario like the above, we have to choose.

If we need a workaround to ensure that updates on one computer still reaches all the computers so that the data is consistent, that is going to be slow — we lose availability.

If we want to achieve availability, we could have each computer just return or update the data it has, then worry about synchronisation later — we lose consistency.

If you find yourself in the position of having to choose a distributed database, it would be immensely helpful to know upfront which 2 factors you want to prioritise!

## Examples

**Consistency and Availability**: Bank databases fall in this category. Financial transactions must be accurate, and people need to quickly know whether they were successful. So we have to live with these databases requiring regular maintenance (usually late at night) to minimise the risk of partitioning failure.

**Partitioning and Consistency**: Authentication systems are relied upon to ensure that data is only accessed by people who are authorised to do so, and cannot afford to go down for long periods of time. This requires that permissions be properly synchronised across all computers, so consistency is key. These two factors are more important than ensuring a speedy response.

**Partitioning and Availability**: Essential services, such as Google Maps, have to remain operational even with (recoverable) failures, and still have to respond in a reasonable amount of time (otherwise real-time navigation would fail). Roads do not change often, so it is okay if the info we are getting is slightly out of date; we might occasionally get a slower route or find ourselves at a business whose operating hours are not updated in Google Maps, but these are not critical failures.

The CAP theorem does not say we can never have the third factor! It means we have to pick 2 factors to prioritise, and live with the lower performance of the third.

**Issue summary:** To increase the performance of a distributed database, we can scale up/scale vertically by increasing the computers’ performance, or scale out/scale horizontally by adding more computers. Distributed databases can only prioritise two of the following three factors: consistency, availability, partitioning (CAP theorem).

This actually ran longer than I expected; the examples were an unplanned addition that I think helps to clarify use cases for each combination.

## What I’ll be covering next

**Next issue:** [LMG S7] Issue 87: Relational Databases

I’ll spend the next 3 issues talking about 3 major types of databases in use today. This isn’t strictly layman content, but I suspect in some non-technical conversations these terms may pop up. More importantly, I think the 3 major types cover 3 different concepts of data, and I hope that elaborating on these in a little bit more detail will help to develop a more nuanced way of thinking about data.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]
