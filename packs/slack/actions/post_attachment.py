import json
import httplib

import requests

from st2actions.runners.pythonrunner import Action

__all__ = [
    'PostAttachmentAction'
]


class PostAttachmentAction(Action):
    def run(self, message, fallback, username=None, icon_emoji=None,
            channel=None, pretext=None, title=None, title_link=None,
            color=None):
        body = {}
        config = self.config['post_attachment_action']
        username = username if username else config['username']
        icon_emoji = icon_emoji if icon_emoji else config.get('icon_emoji', None)
        body['username'] = username
        body['icon_emoji'] = icon_emoji
        #body['text'] = message

        attachments = {
            'text': message,
            'fallback': fallback,
            'pretext': pretext,
            'title': title,
            'title_link': title_link,
            'color': color,
        }
        attachments = [dict((k, v) for k, v in attachments.iteritems() if v)]
        self.logger.info(attachments)
        body['attachments'] = attachments
        if channel is not None:
            body['channel'] = channel
        self.logger.info(body)

        data = 'payload=%s' % json.dumps(body)
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.post(url=config['webhook_url'],
                                 headers=headers, data=data)

        if response.status_code == httplib.OK:
            self.logger.info('Message successfully posted')
        else:
            self.logger.exception('Failed to post message: %s' % (response.text))

        return True
