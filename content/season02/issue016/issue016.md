Title: Issue 16: Shell scripts and automation
Date: 2019-03-30 08:00
Tags: 
Category: Season 2
Slug: issue016
Author: J S Ng
Summary: 
Modified: 

So you just got back from a trip with lots of photos in your camera. You take the SD card out from the camera, put it in your laptop, open up the photos … and realise they all have the wrong white balance set.

Or if you’re like me, you spend the better part of an afternoon using your camera to ‘scan’ a textbook for later reference. That means you now have over 300 photos to crop separately (left and right pages), adjust levels (to make the image more like it was done with a scanner), and do other minor corrections.

You know your way around Photoshop (or GIMP), but no way you are going to do that by hand for a week or so—we’ve all got lives to get on with! But you spend half an hour googling, and can’t find any tools that can help you to get the job done quickly. (Okay, there’s XnView, but let’s just pretend that doesn’t exist for the purpose of this issue.)

You have just discovered the need for computerised batch processing.

## Converting an image in the command line

Once you have found a command line program to help you edit an image (such as [imagemagick](https://imagemagick.org)), you can do that scanning adjustment with a command like:

`convert DCIM0100.JPG -colorspace LinearGray -crop 1260x1800+160+240 -level 64,160 page001.png`

We just covered command lines in the previous issue, and you don’t need to be able to reproduce this command, but I hope you are seeing [the patterns mentioned in the last issue]() here. The program `convert` is being called with 3 options:

- `-colorspace LinearGray` converts the image to grayscale (you can probably just set this in the camera beforehand, but no harm being sure)
- `-crop 1260x1800+160+240` crops the image to a size of 1260x1800 starting 160 pixels from the left and 240 pixels from the bottom.
- `level 64,160` basically increases the contrast of the image, making the text blacker, and the page whiter.

The documentation for Imagemagick’s `convert` command [is available online](https://imagemagick.org/script/command-line-options.php), and I will get round to discussing image formats in a future season. This is as far as we’ll talk about images for now.

Great. Here’s a command that can open DCIM0100.JPG, do those operations to the image, and save it to the file page001.png. (I pre-pad numbers with 0 because many file browsers are still terrible at sorting `2` before `10`, but can sort `02` before `10` just fine.)

Do I have to copy-paste this command 300 times into the terminal while editing the filename each time? Of course not, that’s why we have computers in the first place.

## Making a batch file/shell script

A batch file (Windows) or **shell script** (Linux/Mac) is simply a file with a list of commands that the terminal will execute when the file/script is invoked. They can be one line, ten lines, a hundred lines, or more. They can be simple, or incredibly complex. They can simply start an application with a different set of options, or help you to update all the packages on your computer periodically and handle simple errors. If you opened the three links from the last issue, you would have seen some examples of what these scripts can do.

So how would I put that command into a shell script so that it can do the above for *all* the images in a folder?

There are a number of things we need to figure out first:

1. How do we want to number the final output files? I’m just going to go with page001.png, page002.png, etc to keep things simple, but you can customise the filename in all kinds of ways.
2. The script needs a way to get the names of the original images as well.

My go-to terminal is `bash`, one of the default terminals in Linux. You may sometimes see terminals referred to as CLIs (**c**ommand **l**ine **i**nterfaces), as opposed to GUIs (**g**raphical **u**ser **i**nterfaces), but this can be done in Windows Command Prompt, Powershell, zsh, Mac Terminal, and just about any CLI that supports scripts. Each CLI has its own syntax and format of commands that will need to be learnt, but in this day and age it is not difficult to find help for that online.

In bash, this script would look like:
```
n=1
for file in *.JPG
do
  outputname=page$(printf %03d $n).png
  convert $file -colorspace LinearGray -crop 1260x1800+160+240 -level 64,160 $outputname.png
  n = n+1
done
```

I promised not to make this newsletter technical, and I said this wouldn’t be a howto, but this is as far as I can go without programming. I’ll step you through what each part does:

## Simple Bash programming

```
for file in *.JPG
do
  [command]
done
```
Bash checks the current folder for files ending with .JPG. (Why is it written as \*.JPG? We’ll revisit that in a future issue.) For each file found, it passes the filename to [command] and carries out the command. This command is able to access the filename using the name `$file`.  

```
n=1
...
n = n+1
```
This is how I am creating a number counter that I can use to number the final output files sequentially. Mathematically this makes no sense (how can `n` be equal to `n+1`?), but in programming, `n = n+1` means “add 1 to the value of `n`, and assign the new value to `n`.”

```
outputname=page$(printf %03d $n).png
```
`printf` is a program that creates lines of text, and it can help format text in all kinds of useful ways. `%03d` describes the format I want: a **3**-digit **d**ecimal number, pre-padded with **0**s. `printf %03d $n` changes `1` to `001`, and will do this for each value of `n`. So `page$(printf %03d $n).png` helps me craft the filename `page001.png` and I can refer to it using the name `$outputname`.

Putting everything together …
```
n=1
for file in *.JPG
do
  outputname=page$(printf %03d $n).png
  convert $file -colorspace LinearGray -crop 1260x1800+160+240 -level 64,160 $outputname.png
  n = n+1
done
```
Name a counter, `$n`, and set its value as 1. For each `$file` ending with .JPG, calculate the result of `printf %03d $n`, insert it into `page$(printf %03d $n).png`, and name the result as `$outputname`. Carry out the conversion on `$file`, and save the result to `$outputname`. Increase the value of `$n` by 1.

## Scripting: talking to a really really really dumb thing

Was that exhausting to read? I bet. If you had to ask a simpleton to do something, you know you need to be explicit: “Go to the market, stall number #01-23, and buy two packs of chili paste, the orange kind with the circular symbol, 200g. Also buy 100g of dried shrimp. Put the chili paste packs into one plastic bag, and the shrimp in another plastic bag. If they can’t do that for any reason, write down what the stall owner says, and call me. If the stall is closed, come home.”

Programming is like that. A good programmer can take a difficult task, break it down into steps so simple that even a computer can understand, and figure out how to write the repetitive parts to make them easier to say.

**Issue summary:** Everybody has a simpleton in their pocket, and maybe one at home on the desk. These simpletons are able to run sets of instructions that they are carrying. You can give them more sets of instructions, often obtained through a Store. Some of the really good instruction sets will cost some money, though. And almost none of them will get the simpleton to do exactly what you want.

The only way to do that is to learn how to write the instructions yourself. The ability to do so is what we call Programming.

A shell script is just a set of commands that a simpleton can carry out.

-----

Phew, this issue sure took a while! I knew I was going to have to write some code, and explain it for laypeople, and it wasn’t going to be enjoyable. I’m glad it’s over and I hope I won’t have to do that again in the later issues of this season. I’m still figuring out how to do it more simply.

Do let me know how you find this format? I don’t explain things line by line, but rather part by part, as that makes more sense to me. I also try to start from simple commands, and build them up into more complex cases. But doing that will result in a tutorial-length issue, so I compress where I can. If there’s anything I can do to make it easier for you, drop me an email :)

We took a short detour from looking at what sysadmins do, to see what a shell script is like. Lots of things that happen in a computer can be automated this way. But it has its limitations. Next issue, we’ll look at how programmers help each other make their jobs easier by writing programming libraries.

## What I’ll be covering next

**Next two issues:** Libraries, Frameworks

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those ‘\r\n’s in the HTTP request packet [Issue 12]?
