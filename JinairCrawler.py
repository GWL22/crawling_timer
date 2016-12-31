# -*- coding: utf-8 -*-

import requests
import re

from bs4 import BeautifulSoup
from connection import r, url_jin, db_jin


# For crawling 'a href='
def find_a(tags):
    return tags.name == 'a' and tags.has_attr('href')


class JinairCrawler(object):
    def __init__(self):
        pass

    # Crawl links from jinair main homepage
    def Crawl_link(self):
        res = requests.get(url_jin)
        content = res.text
        soup = BeautifulSoup(content, 'html.parser')
        promotion = soup.find('div', attrs={'id': 'tabEvent'})
        promotion_link = promotion.find_all('a')
        promotion_date = promotion.find_all('span', attrs={'class': 'date'})
        for link, date in zip(promotion_link, promotion_date):
            if self.Check_link(link):
                self.Notice_system(link, date)

            # For test
            else:
                print 'No update'

    # Check DB and link
    def Check_link(self, link):
        dbs = r.lrange(db_jin, 0, -1)
        link = str(link['href'])

        # Use for the first time
        # If DB is empty
        if len(dbs) == 0:
            r.lpush(db_jin, link)
            return True

        # Check the link whether is in DB or not
        else:
            if link not in dbs:
                r.lpush(db_jin, link)
                # Maintain 5 items in DB
                # This is for more than one new promotion
                r.ltrim(db_jin, 0, 5)
                return True
            else:
                return False

    def Notice_system(self, link, date):
        title = link.get_text().encode('utf-8')
        date = date.get_text()
        print 'JinairCrawler found new promotions!!'
        print 'title: ' + title
        print 'date: ' + date
        print 'link: ' + 'http://www.jinair.com/' + link['href']
