import json
from lib.hosted_chef_action import HostedChefBaseAction
from lib import utils

__all__ = [
    'UpdateEnvironmentAction'
]


class UpdateEnvironmentAction(HostedChefBaseAction):
    def run(self, environment, update):
        update = json.loads(update)
        query = 'chef_environment:%s' % environment
        results = self.search('node', query)
        data = results.data
        for result in data['rows']:
            node = self.node(result['name'])
            attributes = node.normal.to_dict()
            merged = utils.updatedict(attributes, update)
            node.normal = merged
            node.save()

        return True
