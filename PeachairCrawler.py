# -*- coding: utf-8 -*-

import re
import requests

from bs4 import BeautifulSoup
from connection import r, url_peach, db_peach


# For crawling 'a href='
def find_a(tags):
    return tags.name == 'a' and tags.has_attr('href')


class PeachairCrawler(object):
    def __init__(self):
        pass

    # Crawl link from Peachair Homepage
    def Crawl_link(self):
        res = requests.get(url_peach)
        content = res.text
        soup = BeautifulSoup(content, 'html.parser')

        # Find out the site belonged to spacials' section
        for a in soup.find_all(find_a):
            # double check for whether a is link or not
            if a['href'][:4] == 'http':
                match = re.search(r'specials/\w*', a['href'])
                if match is None:
                    continue
                else:
                    # if link is not db, there is new promotion
                    if self.Check_link(a['href']):
                        self.Notice_system(a)

                    # For test
                    else:
                        print 'No update'

    def Check_link(self, link):
        dbs = r.lrange(db_peach, 0, -1)

        # Use for the first time
        # If DB is empty
        if len(dbs) == 0:
            r.lpush(db_peach, str(link))
            return True

        # Check the link whether is in DB or not
        else:
            if link not in dbs:
                r.lpush(db_peach, str(link))
                # Maintain 10 items in DB
                # This is for more than one new promotion
                r.ltrim(db_peach, 0, 9)
                return True
            else:
                return False

    def Notice_system(self, link):
        print 'PeachairCrawler found new promotions!!'
        print 'link: ' + link['href']
        print 'title: ' + link.get_text().encode('utf-8')
