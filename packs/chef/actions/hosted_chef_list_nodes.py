from lib.hosted_chef_action import HostedChefBaseAction

__all__ = [
    'ListNodesAction'
]


class ListNodesAction(HostedChefBaseAction):
    def run(self):
        nodes = self.nodes.keys()
        return nodes
