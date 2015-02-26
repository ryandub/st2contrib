from st2actions.runners.pythonrunner import Action

__all__ = [
    'ListDeploymentsSlackFormatAction'
]


def status_to_color(status):
    if status in ['NEW', 'ONLINE', 'ACTIVE']:
        return 'good'
    if status in ['ERROR', 'DELETED', 'DELETING', 'OFFLINE']:
        return 'danger'
    if status in ['BUILD', 'CONFIGURE']:
        return '#3366FF'
    return '#996633'


class ListDeploymentsSlackFormatAction(Action):
    def run(self, deployments):
        slack_attachments = []
        for deployment_id, deployment in deployments.iteritems():
            slack_attachments.append({
                'color': status_to_color(deployment['status']),
                'author_name': deployment['id'],
                'author_icon': (
                    "http://ddf912383141a8d7bbe4-e053e711fc85de3290f12"
                    "1ef0f0e3a1f.r87.cf1.rackcdn.com/deployments-logo.png"),
                'text': deployment['blueprint']['description'],
            })
        return slack_attachments
