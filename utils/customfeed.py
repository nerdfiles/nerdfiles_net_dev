#!/usr/bin/env python
"""
This script downloads, sorts, and merges 
entries from different RSS feeds
and writes the output to a local file.
The result is a custom feed containing
all the specified ones.
"""

__version__="0.1"
__author__ ="Eubolist <eubolist@gmail.com>"

#####################################
# Define your custom variables here:#
TARGET_FILE = '/var/www/example.rss'#
RSS_FEEDS = ["https://kippt.com/nerdfiles/important/feed"]
# Optional parameters:              #
TITLE=""                            #
LINK=""                             #
ICON=""                             #
DESCRIPTION=""                      #
####End of user defined options######
#####################################

import feedparser
import Future

if not TITLE: TITLE = "Kippt Important! Feed"
if not LINK: LINK = "http://ezrss.it/search/index.php"
if not ICON: ICON = "http://ezrss.it/images/ezrssit.png"
if not DESCRIPTION: DESCRIPTION = "Personalized RSS Feed created with customfeed.py V0.1"

def main():
    """
    Downloads, sorts, and merges all specified feeds
    and writes the output to a file.
    """
    hit_list = RSS_FEEDS
    # pull down all feeds
    future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
    # block until they are all in
    feeds = [future_obj() for future_obj in future_calls]

    entries = []
    for feed in feeds:
        entries.extend( feed[ "items" ] )
    
    sorted_entries = sorted(entries, key=lambda entry: entry["updated_parsed"], reverse=True)
    
    f = open(TARGET_FILE, 'w')
    buffer = """<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
            <channel>
                    <title>%s</title>
                    <link>%s</link>
                    <image>
                            <title>%s</title>
                            <url>%s</url>
                            <link>%s</link>
                    </image>
                    <description>%s</description>
    """ % (TITLE,LINK,TITLE,ICON,LINK,DESCRIPTION)
    f.write(buffer)
    f.flush()
    for x in sorted_entries:
        ### Workaround if comments are missing
        if not "comments" in x: x["comments"]=u'No comments available'
        ###
        buffer = """		<item>
    			<title><![CDATA[%s]]></title>
    			<link>%s</link>
	    		<category domain="%s"><![CDATA[%s]]></category>
		    	<pubDate>%s</pubDate>
			    <description><![CDATA[%s]]></description>
    			<enclosure url="%s" length="%s" type="%s" />
	    		<comments>%s</comments>
		    	<guid>%s</guid>
		    </item>
        """ % (x["title"], x["link"], x["tags"][0]["scheme"], x["tags"][0]["term"],\
        x["updated"], x["summary"], x["enclosures"][0]["href"], \
        x["enclosures"][0]["length"], x["enclosures"][0]["type"], x["comments"], x["id"])
        f.write(buffer)
        f.flush
    buffer="	</channel>\n</rss>" 
    f.write(buffer)
    f.close()
    
if __name__ == "__main__":
    main()
