from lib.hosted_chef_action import HostedChefBaseAction

__all__ = [
    'ListEnvironmentsAction'
]


class ListEnvironmentsAction(HostedChefBaseAction):
    def run(self):
        environments = self.environments.keys()
        return environments
