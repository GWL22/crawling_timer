# -*- coding: utf-8 -*-

import requests
import re

from bs4 import BeautifulSoup
from connection import r, url_jin, db_jin
# This is for another Notice_system, you can cancel it by annotating
from alarm_in_slack import alarm


# For crawling 'a href='
def find_a(tags):
    return tags.name == 'a' and tags.has_attr('href')


class JinairCrawler(object):
    def __init__(self):
        pass

    # Crawl links from jinair main homepage
    def Crawl_link(self):
        try:
            res = requests.get(url_jin)
            content = res.text
            soup = BeautifulSoup(content, 'html.parser')
            promotion = soup.find('div', attrs={'id': 'tabEvent'})
            promotion_link = promotion.find_all('a')
            promotion_date = promotion.find_all('span',
                                                attrs={'class': 'date'})
            for link, date in zip(promotion_link, promotion_date):
                if self.Check_link(link):
                    link, title, flag = self.Notice_system(link, date)
                    alarm(link, title, flag)

                else:
                    continue

        except Exception as e:
            print 'Jinair\'s Crawl_link' + ' ' + e

    # Check DB and link
    def Check_link(self, link):
        dbs = r.lrange(db_jin, 0, -1)
        link = str(link['href'])

        try:
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

        except Exception as e:
            print 'Jinair\'s DB' + ' ' + e

    def Notice_system(self, link, date):
        link_full = 'http://www.jinair.com' + link['href']
        title = link.get_text().encode('utf-8')
        flag = 'JinairCrawler'
        date = date.get_text()
        print 'JinairCrawler found new promotions!!'
        print 'title: ' + title
        print 'date: ' + date
        print 'link: ' + link_full
        return link_full, title, flag


if __name__ == '__main__':
    test = JinairCrawler()
    test.Crawl_link()
