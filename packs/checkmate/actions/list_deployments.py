import json

from lib.action import CheckmateBaseAction

__all__ = [
    'ListDeploymentsAction'
]


class ListDeploymentsAction(CheckmateBaseAction):

    def run(self, **query):
        return json.dumps(self.list_deployments(**query))
