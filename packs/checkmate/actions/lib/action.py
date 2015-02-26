
from pawn import client

from st2actions.runners.pythonrunner import Action

__all__ = [
    'CheckmateBaseAction'
]


class CheckmateBaseAction(Action):

    def __init__(self, config):
        super(CheckmateBaseAction, self).__init__(config)
        self.checkmateclient = client.CheckmateClient()
        tenant_creds = config.get('tenant_credentials') or {}
        if tenant_creds:
            if all(k in tenant_creds for k in ('apikey', 'username')):
                self.checkmateclient.authenticate(
                    username=tenant_creds['username'],
                    apikey=tenant_creds['apikey'])

    @property
    def version(self):
        return self.checkmateclient.server_version()

    def list_deployments(self, limit=5, offset=0, status='UP', **query):

        status = status or 'UP'
        limit = limit if limit <= 5 else 5
        return self.checkmateclient.list_deployments(
                limit=limit, offset=offset, status=status, **query)

    def get_deployment(self, deployment_id):

        return self.checkmateclient.get_deployment(deployment_id)


