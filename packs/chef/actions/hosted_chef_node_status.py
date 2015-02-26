import arrow
from lib.hosted_chef_action import HostedChefBaseAction

__all__ = [
    'NodesStatusAction'
]


class NodesStatusAction(HostedChefBaseAction):
    def run(self):
        expiry = arrow.now('-00:30')
        node_status = []
        for n_id in self.nodes:
            node = self.node(n_id)
            last_checked_in = arrow.get(node['ohai_time'])
            status = 'unhealthy' if last_checked_in > expiry else 'healthy'
            pretty_time = last_checked_in.humanize()
            node_status.append({
                'node': node['hostname'],
                'os': node['platform'],
                'status': status,
                'last checkin': pretty_time,
             })

        return node_status
