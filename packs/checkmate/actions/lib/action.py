
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

    def list_deployments(self):

        path = "/%s/deployments" % self.checkmateclient.tenant
        return self.checkmateclient.get(path).json()['results']


