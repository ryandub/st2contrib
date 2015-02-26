import time
from lib.hosted_chef_action import HostedChefBaseAction

__all__ = [
    'NodesStatusAction'
]


class NodesStatusAction(HostedChefBaseAction):
    def run(self):
        nodes = self.nodes.keys()
        now = int(time.time())
        node_status = []
        for n in nodes:
            last_checked_in = n.attributes['ohai_time']
            os = n.attributes['platform']
            pretty_time = time.strftime("%Y-%m-%d %H:%M:%S", last_checked_in)

            if now - last_checked_in > 1800:
                status = 'unhealthy'
            else:
                status = 'healthy'

            node_status.append({
                'name': n,
                'os': os,
                'environment': environment,
                'status': status,
                'last checkin': pretty_time,
            })

        return node_status
