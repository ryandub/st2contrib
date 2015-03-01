import json

from lib.action import CheckmateBaseAction

__all__ = [
    'GetDeploymentAction'
]


class GetDeploymentAction(CheckmateBaseAction):

    def run(self, deployment_id):
        return json.dumps(self.get_deployment(deployment_id))
