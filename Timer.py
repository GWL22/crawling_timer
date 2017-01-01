# -*- coding: utf-8 -*-

import datetime
import threading

from JinairCrawler import JinairCrawler
from PeachairCrawler import PeachairCrawler


jin_crawl = JinairCrawler()
peach_crawl = PeachairCrawler()

start_time = datetime.datetime.now()

# Every Period minutes, work
period = 1
# Decide when will you finish.
# in this case, parameter is minutes for test
fin = 2


def functimer(period, fin):
    deadline = start_time + datetime.timedelta(minutes=fin)

    jin_crawl.Crawl_link()
    peach_crawl.Crawl_link()
    # For the test, print time
    print 'start:' + str(datetime.datetime.now())
    print 'Finish:' + str(deadline)
    ########
    timer = threading.Timer(period, functimer, args=[period, fin])

    if datetime.datetime.now() > deadline:
        print 'it\'s done'
        timer.cancel()
    else:
        timer.start()

functimer(period*60, fin)
