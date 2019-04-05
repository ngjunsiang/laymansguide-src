Last issue, I introduced libraries, which are basically magic spells. You call them, they do advanced magic in the background, and return magical results to your code. Or they simplify complicated code, wrapping them up into functions that are easy to call.

All that is cool, but even with that magical aid, working on some projects can be complicated in *different* ways. For example, if you are working on a web app (or website), you can end up with folders everywhere, and all kinds of HTML and CSS and javascript files.

## Web app folder structure example

In a simple app, you *might* start off with files like this:

```
project
|   app.py
|   config.py
|   error.log
|   README.md
|
└───templates
|   |   error.html
|   |   main.html
|   |   settings.html
|   |   index.html
|   |   login.html
|
└───static
|   |   styles.css
|   |   app.js
```

You have app.py which is the web app’s main logic, config.py which contains its settings, an error log you can check to figure out what’s wrong, and a README file for any new members of the team.

Then you have the template files, which contain the code that determines how the page looks. You have your basic splash page (index.html), the login page, the main app view, the user settings view, and a simple error view. These templates have sections that the app can fill in with the relevant information once it is retrieved from a [backend](https://buttondown.email/laymansguide/archive/90aed74c-f7e7-47bb-94ba-f3c3e057e51e).

Finally, you have files which are used in exactly the same way by each page. `styles.css` describes the colours, margins and styling of all the page elements to make them look consistent, while `app.js` contains javascript code that is meant to be run in the user’s browser (for animations, simple utilities, and so on).

## Web app features

Of course, the above files do not just sit around looking pretty. They contain code that does things. app.py will need code that takes a [request](https://buttondown.email/laymansguide/archive/a6941efd-86bf-4fd8-92c9-009fe14a8c2a) and figures out what do do with it. If a [client](https://buttondown.email/laymansguide/archive/b36f0f43-e8f5-402d-8c6a-c2a28f5ff556) sends a request for `/api/annotations/bjPc2xyLTS6Gcu2WW2xtlg`, `app.py` needs to know how to digest that request, pull the relevant information from the backend of database, filter it into a presentable format, and then send it back as a [response](https://buttondown.email/laymansguide/archive/386cead6-8565-499a-9960-5a30ab291e5b) to the client.

A professional web app developer is likely going to be writing similar code, over and over again, different content but similar logic for different customers … surely there’s a more efficient way to do this?

## Web frameworks

If you are at all concerned with efficiency and productivity at work, you would no doubt have templates prepared for all kinds of situations: boilerplate email replies, forms, documents, all prepared and just waiting for some information to be filled in before they are ready.

It’s the same with app development! If a developer specialises in, say, retail apps, it takes some work but they can definitely put together a customisable set of files for any client that needs the usual online commerce setup.

A web framework makes all this easier by providing many of these standard pieces of code, and allowing a developer to just focus on the core parts of the app that change from project to project.

## Web frameworks tend to be language-specific

Since web frameworks involve code, it should surprise you little that they tend to be written for a specific programming language. Some examples:

- Python web frameworks: [Django](https://www.djangoproject.com/), [Flask](http://flask.pocoo.org/), [Bottle](https://bottlepy.org/docs/dev/), …
- Ruby web frameworks: [Hanami](https://hanamirb.org/), [Sinatra](http://www.sinatrarb.com/), [Scorched](http://scorchedrb.com/), …
- NodeJS web frameworks: [Express.js](https://expressjs.com/), [Sails.js](https://sailsjs.com/), [Meteor](https://www.meteor.com/), …

Whichever one you pick, it should make your job easier than doing everything from scratch.

**Issue summary:** While libraries make it easier to do the same thing in a programming language, a framework makes it easier to make a particular kind of app. Like libraries, frameworks are usually specific to a particular programming language, and can’t be used in another programming language.

<hr/>

I have greatly simplified the idea of frameworks here, likely to the consternation of developers everywhere. The only thing I will say in my defense is: at least your potential customers now have a better idea of what you are doing for them!

Speaking of developers, we’re now getting deeper into the kind of work that developers do. Some work alone, but they usually work in teams. How does a development team build projects like this without getting in each others’ way, overwriting each others’ changes, and drawing boundary lines on the floor with marker? What do they use to ensure that everyone knows what is going on?

Next issue is going to be really interesting!

## What I’ll be covering next

**Next issue:** How do developers avoid code conflict? On version control and more

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those '\r\n's in the HTTP request packet [Issue 12,17]?
