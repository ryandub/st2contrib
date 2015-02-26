from lib.hosted_chef_action import HostedChefBaseAction

__all__ = [
    'ListNodesEnvironmentAction'
]


class ListNodesEnvironmentAction(HostedChefBaseAction):
    def run(self, name):
        nodes = []
        raw_nodes = self.search('node', 'chef_environment:%s' % name)
        for node in raw_nodes.data['rows']:
            nodes.append(node['name'])
        return nodes
