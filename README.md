# Strange Autoblog

##What ihttps://github.com/veggiedefender/strange-autoblog/issuess this?

A script based on [this comic](http://www.teamfortress.com/macupdate/comic/). Specifically, this panel:

![heavy holding a auto-blogging minigun](http://i.imgur.com/c96PPOT.jpg)

It will post to a tumblr blog at the end of your TF2 session detailing the current number of kills on the strange weapon of your choosing. 
Originally, it was intended to post after every kill, but due to limitations of the Steam API, it can only update the number of kills after closing the game.
If you found a way around this, please submit a pull request.

##Cool, but how do I use this?

I can understand not wanting to read my messy, undocumented code.

###Get tumblr OAuth credentials

You'll need to register an app [here](https://www.tumblr.com/oauth/register) and get your keys [here](https://api.tumblr.com/console/calls/user/info)

Fill out the relevant info in this block of code: `client = pytumblr.TumblrRestClient(...)` as well as the URL of the blog 

###Pull up your steam URL. 

Get your custom steam url and give it to the `url` variable. Mine looks like `url=veggiedefender` since [this](http://steamcommunity.com/id/veggiedefender/) is my steam profile.

###Do you want to use milestones?

In addition to updating your blog with your kill count, you also have the option of updating it every time your weapon passes a [milestone](https://wiki.teamfortress.com/wiki/Strange#Ranks)

Change `useMilestones` to `True` if you want it, or leave it at `False` if you don't.

###Install the requirements

`pip install -r requirements.txt`

###Run `strange-autoblog.py` every time you start up TF2. 

The first time you run it, you'll be asked some questions to set some stuff up.
