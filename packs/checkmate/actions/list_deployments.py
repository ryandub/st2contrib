from lib.action import CheckmateBaseAction

__all__ = [
    'ListDeploymentsAction'
]


class ListDeploymentsAction(CheckmateBaseAction):
    def run(self):
        return self.list_deployments()
