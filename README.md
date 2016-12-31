# Crawling_timer
---
This is crawler on websited; [Jinair](http://www.jinair.com/), [Peach](http://www.flypeach.com/pc/kr)It
It's wirtten for **Python 2.7.2** and used **Redis** for a database.

Abstract
---
This is cyclical crawler worked by **Timer.py**.

Description
---
**Timer.py** : For the variable's value called **key**, crawler can be worked every 5 mins. In this case, crawler worked every 30 secs for 1 min.
**connection.py** : In this file, you can handle server address, port, urls where you want to run crawling, and database name.
**JinairCrawler.py** : Crawling data on [Jinair](http://www.jinair.com/)'s main homepage.
**PeachairCrawler.py** : Crawling data on [Peach](http://www.flypeach.com/pc/kr)air's main homepage.
