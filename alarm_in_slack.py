# -*- coding: utf-8 -*-

import json
import requests


# On slack, this code makes a notification to know there is new promotion
def alarm(link, title, flag):
    # Use my private channel, you can change this url on incoming-webhook on slackAPI
    slack_hook = 'https://hooks.slack.com/services/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'

    payload = {}
    # Bot name
    payload['username'] = 'Caspher'
    payload['icon_emoji'] = ':ghost:'
    payload['text'] = '{}\n{}\n{}'.format(flag, title, link)
    data = json.dumps(payload)
    requests.post(slack_hook, data=data)
