import feedparser
from .gig import *

feed = feedparser.parse('https://detroit.craigslist.org/search/ggg?format=rss')
print (feed)
entries = []
def getEntries():
    for entry in feed['entries']:
        gig = Gig(entry['title'], entry['summary'], entry['link'])
        entries.append(gig)
    # entr = entry['summary'] + " " + entry['title']
    # entries.append(entr)
    print("ENTRIES:\t", entries)
    return entries
    #     print (key+"\n")
