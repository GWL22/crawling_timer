# -*- coding: utf-8 -*-

import json
import requests
from connection import slack_hook


# On slack, this code makes a notification to know there is new promotion
def alarm(link, title, flag):
    payload = {}
    # Bot name
    payload['username'] = 'Caspher'
    payload['icon_emoji'] = ':ghost:'
    payload['text'] = '{}\n{}\n{}'.format(flag, title, link)
    data = json.dumps(payload)
    requests.post(slack_hook, data=data)


def alarm_fin(finish_time):
    payload = {}
    # Bot name
    payload['username'] = 'Caspher'
    payload['icon_emoji'] = ':ghost:'
    payload['text'] = 'Crawler is turned off at {}'.format(str(finish_time))
    data = json.dumps(payload)
    requests.post(slack_hook, data=data)
