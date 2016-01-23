#Made by veggiedefender
#Contact me if you have any issues
#/u/veggiedefender on reddit
#/id/veggiedefender on steam

import requests
import re
import pytumblr
import time

client = pytumblr.TumblrRestClient(                                                                     
    'consumer key',#get this stuff at https://www.tumblr.com/oauth/register
    'consumer secret',#and here https://api.tumblr.com/console/calls/user/info
    'oauth token',
    'oauth secret',
)

p = re.compile(ur'\d+')
url = "YOUR CUSTOM URL GOES HERE"


def getID(r, item):
    itemID = r["rgInventory"][item]["classid"] + "_" + r["rgInventory"][item]["instanceid"]
    return itemID

def getStranges(r, url):
    stranges = []
    for item in r["rgInventory"]:
        if r["rgDescriptions"][getID(r, item)]["tags"][0]["name"] == "Strange":
            stranges.append(item)
    return stranges

with open("id.txt", "a+") as f:
    blogName = f.readline().rstrip()
    targetID = f.readline().rstrip()
r = requests.get("https://steamcommunity.com/id/%s/inventory/json/440/2" % url).json()
if targetID == "":
    print "Getting Inventory..."
    
    stranges = getStranges(r, url)
    
    print "%s Stranges Found:" % len(stranges)
    
    for i in range(len(stranges)):
        name = r["rgDescriptions"][getID(r, stranges[i])]["market_name"]
        kills = int(re.findall(p, r["rgDescriptions"][getID(r, stranges[i])]["type"])[0])
        print "[%s] %s - %s kills" % (i, name, kills)
    
    targetID = stranges[int(raw_input("Which strange do you want to track? "))]
    blogName = raw_input("What blog do you want to post to (probably case sensitive)? ")
    with open("id.txt", "a+") as f:
        f.write(blogName + "\n")
        f.write(targetID)

target = getID(r, targetID)
prev = int(re.findall(p, r["rgDescriptions"][target]["type"])[0])
name = r["rgDescriptions"][target]["market_name"]
print "Press ctrl-C to stop."
while True:
    try:
        r = requests.get("https://steamcommunity.com/id/%s/inventory/json/440/2" % url).json()
        target = getID(r, targetID)
        kills = int(re.findall(p, r["rgDescriptions"][target]["type"])[0])
        if kills > prev:
            bodyText = "I've killed %s people with my %s!" % (kills, name)
            client.create_text(blogName, state="published", slug=str(kills), title=str(kills), body=bodyText)
        prev = kills
    except ValueError:
        print "Steam may be down."
    time.sleep(60)