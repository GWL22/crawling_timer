# Crawling_timer

This is a crawler on websites; [Jinair](http://www.jinair.com/), [Peach](http://www.flypeach.com/pc/kr)

It's wirtten for **Python 2.7.2** and used **Redis** for a database.

In addtion, Notification will be showed on slack.

Abstract
---
This is a cyclical crawler worked by **Timer.py** with slack notification system.

Description File
---
- **Timer.py** : For the variable's value called **fin*, crawler can be worked every 1 mins. In this case, crawler worked every minute for 2 mins.
- **connection.py** : In this file, you can handle server address, port, urls where you want to run crawling, and database name.
- **JinairCrawler.py** : Crawling data on [Jinair](http://www.jinair.com/)'s main homepage.
- **PeachairCrawler.py** : Crawling data on [Peachair](http://www.flypeach.com/pc/kr)'s main homepage.
- **alarm_in_slack.py** : This file is for notification(New promotion and Crawler turned off) on slack. Notification channel on slack can be controled by change of [slack_hook](https://fc-dss3.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks)
