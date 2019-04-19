Last issue, I introduced **version control**, the idea that you can set things up in a way that lets you see the **change history** of a document. This lets you undo changes which you later come to regret, and compare the document to a previous point in history. If you have a version control system (VCS) set up, you can commit changes to it and view a list of those changes later.

When one is just starting out in software development, one thing that often happens is this. You start writing code for an app-say, a todo list. You write code to set up a database, display a login and other stuff. You commit the changes to the code. You add core features: add/remove/update a todo item; commit. You come up with more ideas: subtasks, recurring items, tags, filters, and all that jazz. Commit, commit, commit. You now have a complete app with bells and whistles, but the code is a sprawling mess: when you finally test the app, there are strange bugs everywhere, the lists don't filter properly, and the database gets messier and messier.

Proper planning can make this more orderly to some extent, but it cannot eliminate one fact of programming: that there will always be bugs. And the only way to catch them is to test the app.

## Manual testing

The most straightforward way is, of course, to get a human to test the app. This gets tiring quickly, for obvious reasons. Asking a human to repeatedly carry out a set of procedures to make sure the app returns the correct data is tedious … which makes it perfect for automating!

If you are testing an app manually, it is human nature to not want to run 200 tests by hand. This leads to people trying to keep the number of tests small, which leads to some bugs not being caught, or they try to go as long as possible without testing, which leads to bugs piling up. Furthermore, manual testing is just slow.

Being able to speed up the testing rate, and have something else do the testing for you, eliminates these problems and lets you focus on writing code rather than typing inputs and checking outputs.

# Web testing

How exactly do you test a website? While there is no replacement (yet) for a human when it comes to judging look and feel, you can rely on software to get the functional parts tested. Software such as [Selenium](https://www.seleniumhq.org/) have a built-in browser that is able to [request webpages](https://buttondown.email/laymansguide/archive/a6941efd-86bf-4fd8-92c9-009fe14a8c2a) and check the webpage code to see if what is supposed to be there is actually there.

For example, after I perform a login, I should be in my Home screen, the main section should display a welcome, my avatar should be in the top right hand corner, etc. All of this can be tested for in the code.

# Test suites and automated testing

So after we have a bunch of tests, what happens? Write code, run the **test suite** (a collection of tests), check the result, and commit the code if the test passes. What happens when we have over 200 tests? Won’t that take a while?

Yeah it would, but why do you need to test parts of the app that haven’t changed? You can set up your testing so that the basic bits of code (units conversion, time conversion, data cleaning, …) have their own tests. Then the next layer, the main code (data management, login, setup, etc) each have their own tests. The complete app then has more tests. Each layer tests for bugs specific to its level.

Now you can just run the relevant tests when you change one small part of your code. Or not; you could set your tests up so that once you try to commit, the testing software detects which parts of the code has changed, runs tests for those parts, and only lets your commit through if it passes all the tests.

**Issue summary:** Testing is the only way to know your app really works. Tests can be set up for the different parts of your app, from the basic building blocks to the main code and finally even the interface, including web pages.

<hr/>

Yeah, almost nobody liked tests and exams in school, I know. But in software, testing is the only way to know your app *really* works, and not just because you say/think it does.

Tests are one of those things that beginning programmers tend to neglect until they learn their first hard lessons. I can see there are many ways to apply it outside of programming, particularly in areas where lots of vetting is needed—vetting really is just human testing, isn’t it? When vetting relies on clear rules and has an outcome that you know in advance, you can think of it as a test. Wouldn’t it be nice if parts of that could be automated, so that you can focus on applying human judgement?

Last issue, I realised that the issues were taking me 1.5 hrs to write, which I think means I am cramming too much content. I promised to keep each issue short and digestible; they are now back to being 1 hour of writing. Again, if you do actually prefer longer issues, drop me an email and let me know!

## What I’ll be covering next

**Next issue:** Multiplayer git, and how git stops people from wanting to kill each other

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those '\r\n's in the HTTP request packet [Issue 12,17]?
