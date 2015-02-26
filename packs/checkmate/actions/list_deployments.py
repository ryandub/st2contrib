from lib.action import CheckmateBaseAction

__all__ = [
    'ListDeploymentsAction'
]


class ListDeploymentsAction(CheckmateBaseAction):

    def run(self, **query):
        return self.list_deployments(**query)
