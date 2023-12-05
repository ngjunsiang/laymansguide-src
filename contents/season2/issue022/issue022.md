Last week I introduced forking and merging, which are how developers ensure that they don't override other peoples’ work. They fork a repository to create their own copy, make the changes required to introduce the feature they want, and then merge it back with the main repository when it is ready, for the repository owner to review.

Two weeks ago I introduced the idea of testing, which in programming means writing more code that checks your code so that it is producing the correct output when you give it a certain input.

By now your idea of a developers’ workflow might look something like this:

1. Fork a repository (which creates a **branch**).
2. Make changes to code on that branch.
3. Test the code on that branch.
4. If the tests pass, send a pull request to the repository owner to merge this branch with the main branch.


![A commit on Github]({attach}issue022_01.png)
<small>Git branching. From [Atlassian’s git branch tutorial](https://www.atlassian.com/git/tutorials/using-branches).</small>


You can imagine that steps 2 and 3, the bread and butter of developers everywhere, is really tedious. Write code, test fails. Edit code, test fails again. On and on and on.

So engineers automate this part. Git (from Issue 19) can run little bits of code (called a **hook**) when a commit is made to carry out this testing. So this lets developers set up repositories in a way that tests every single commit (or series of commits)). The above process now looks like:

1. Fork a repository (which creates a **branch**).
2a. Make changes to code on that branch.
2b. Git tests the code on that branch and reports the result.
3. If the tests pass, send a pull request to the repository owner to merge this branch with the main branch.

One step less! But the part that developers dread is usually merging, which is where the code conflicts occur …

## Merge conflicts


![A commit on Github]({attach}issue022_01.png)
<small>Git merging. From [Atlassian’s git merge tutorial](https://www.atlassian.com/git/tutorials/using-branches/git-merge).</small>


Most development teams organise their work into (at least) 3 types of branches:

1. `master`, which is usually production code that is actually being run on the servers.
2. `dev`, for code in development that the team is working on.
3. `feature`, for code forked from development which a developer or smaller team is editing

While Alice is working on a `feature` branch, Bob is working on his `feature` branch as well, and Charmaine is merging her change to the `dev` branch. Charmaine’s changes might cause problems with Alice’s code. Alice is not going to know about this until she tries to merge her branchc with `dev`! So her work process now looks like:

1. Fork a repository (which creates a **branch**).
2a. Make changes to code on that branch.
2b. A git hook tests the code on that branch and reports the result.
2c. Pull any changes in the parent branch (automatically or manually) to keep the code current.
3. If the tests pass, send a pull request to the repository owner to merge this branch with the main branch.

This means that on top of just testing her code, Alice (and Bob and Charmaine) need to pull in changes from `dev` whenever it is updated, to ensure that her own changes still work with the latest copy of `dev` branch. This can be automated with git hooks (those little bits of code mentioned earlier), but the mental stress from having the code change under you can be pretty draining.

Big features, in particular, suffer from problems like this because they involve many code changes that accumulate and affect many parts of `dev`. So some teams have taken to using a process called **Continuous Integration**.

## Continuous Integration

In a nutshell, continuous integration means to keep your code changes as small as possible, and merge your changes into the parent branch as often as possible, instead of letting them pile up to be released in one day.

Its main advantage is that it allows the process of making a change to be really short. Which then allows these changes to be merged as soon as possible, and be updated to other developers’ branches as soon as possible, so that the latest updates are synchronised to the team, and nobody is working in the dark with an unsynced copy of the base code.

**Issue summary:** Continuous Integration means merging changes back to the main branch as often as possible. This means keeping code changes as small as possible, and using automated testing to speed up the development process.

-----

When I first learnt about continuous integration, I thought this was something every organisation should know about! Have you had colleagues who tend to do things in the dark, and nobody really knew what they were doing and they seemed to be out of sync with the team? Yeah, continuous integration and help with that.

Understandably, nobody wants to spend more time in meetings and on communication that is otherwise necessary. But in workplaces where the team shares a common repository (like a shared network folder, or Dropbox folder, or Google Drive folder, …), why not try to automate some of the updates which are done by hand?

One example: I don’t like it when events are added to a calendar and I only find out much later. So I used [IFTTT](https://ifttt.com/), a web service that lets me set up automated processes, to send myself a Telegram message whenever an event is added to a calendar.

In a team, automating such updates means somebody is not wasting time typing out these updates to the team. What can your team automate today so that it is easier for everyone to be in sync?

## What I’ll be covering next

**Next issue:** Specifications: how developers know what to work on (finally!)

**Sometime in the future:** What is:

- booting up? [Issue 15]
~~- a specification? [Issue 6,8]~~
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n's in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
