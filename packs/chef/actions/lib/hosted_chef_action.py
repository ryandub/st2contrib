import chef

from st2actions.runners.pythonrunner import Action

__all__ = [
    'HostedChefBaseAction'
]


class HostedChefBaseAction(Action):

    def __init__(self, config):
        super(HostedChefBaseAction, self).__init__(config)
        self.provider_config = self.config.get('hosted_chef', None)
        if not self.provider_config:
            raise ValueError(('Invalid credentials set name "hosted_chef". '
                              'Please make sure that credentials set '
                              'with this name is defined in the config'))

        self.chefapi = self._get_chefapi()
        self.nodes = self._get_nodes()
        self.roles = self._get_roles()
        self.environments = self._get_environments()

    def _get_chefapi(self):
        url = "%s/organizations/%s" % (self.provider_config['url'],
                                       self.provider_config['org'])
        key = self.provider_config['key']
        client = self.provider_config['user']
        chefapi = chef.ChefAPI(url, chef.rsa.Key(key), client)
        return chefapi

    def _get_nodes(self):
        nodes = chef.Node.list(api=self.chefapi)
        return nodes

    def _get_roles(self):
        roles = chef.Role.list(api=self.chefapi)
        return roles

    def _get_environments(self):
        environments = chef.Environment.list(api=self.chefapi)
        return environments

    def node(self, node_id):
        _node = chef.Node(node_id, api=self.chefapi)
        return _node

    def environment(self, env):
        env = chef.Environment(env, api=self.chefapi)
        return env

    def search(self, scope, query):
        search = chef.Search(scope, query, api=self.chefapi)
        return search
