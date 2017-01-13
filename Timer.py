# -*- coding: utf-8 -*-

import datetime
import threading

from JinairCrawler import JinairCrawler
from PeachairCrawler import PeachairCrawler
from alarm_in_slack import alarm_fin

jin_crawl = JinairCrawler()
peach_crawl = PeachairCrawler()

start_time = datetime.datetime.now()

# Every Period minutes, work
period = 1
# Decide when will you finish.
fin = 2


def functimer(period, fin):
    deadline = start_time + datetime.timedelta(minutes=fin)

    jin_crawl.Crawl_link()
    peach_crawl.Crawl_link()

    print 'Crawler start: ' + str(datetime.datetime.now())

    timer = threading.Timer(period, functimer, args=[period, fin])

    if datetime.datetime.now() > deadline:
        timer.cancel()
        alarm_fin(deadline)
    else:
        timer.start()

functimer(period*60, fin)
