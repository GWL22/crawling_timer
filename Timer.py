# -*- coding: utf-8 -*-

import datetime
import threading

from JinairCrawler import JinairCrawler
from PeachairCrawler import PeachairCrawler


jin_crawl = JinairCrawler()
peach_crawl = PeachairCrawler()

start_time = datetime.datetime.now()

key = 60


class Timer(object):
    def __init__(self, key):
        self.key = key

    # For the test, count used
    def functimer(self):
        jin_crawl.Crawl_link()
        peach_crawl.Crawl_link()
        # For the test, print time
        print str(datetime.datetime.now())
        ########
        timer = threading.Timer(30, self.functimer())

        if datetime.datetime.now() > self.deadline():
            print 'it\'s done'
            timer.cancel()
        else:
            timer.start()

    def deadline(self):
        # For the test, use seconds as interval
        deadline = start_time + datetime.timedelta(seconds=self.key)
        print deadline
        return deadline

crawler = Timer(key)
crawler.functimer()
