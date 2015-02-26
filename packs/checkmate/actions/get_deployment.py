from lib.action import CheckmateBaseAction

__all__ = [
    'GetDeploymentAction'
]


class GetDeploymentAction(CheckmateBaseAction):

    def run(self, deployment_id):
        return self.get_deployment(deployment_id)
