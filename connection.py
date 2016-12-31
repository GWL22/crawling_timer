# -*- coding: utf-8 -*-

# To oprimize text information, use Redis
import redis

# server, port should be used your server address
server = # add your sever address
port = # add your server port
r = redis.Redis(host=server, port=port)

# url is where you want to crwal
url_jin = 'http://www.jinair.com/default.aspx'
url_peach = 'http://www.flypeach.com/pc/kr'

# In the db below, promotion info will be saved
db_jin = 'Jinair'
db_peach = 'Peach'
