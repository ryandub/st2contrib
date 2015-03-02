import json

from st2actions.runners.pythonrunner import Action

__all__ = [
    'ShowDeploymentSlackFormatAction'
]

COLORS = {
    "ok": "#2ecc71",
    "error": "#c0392b",
    "warning": "#f39c12",
    "processing": "#2980b9",
    "disabled": "#95a5a6"
}

ICONS = {
    "linux": ("http://icons.iconarchive.com/icons/tatice/operating-systems/"
              "256/Linux-icon.png"),
    "loadbalancer": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0"
                     "e3a1f.r87.cf1.rackcdn.com/"
                     "cloud-load-balancers-icon.png"),
    "lb": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0"
           "e3a1f.r87.cf1.rackcdn.com/"
           "cloud-load-balancers-icon.png"),
    "data": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0e3a"
             "1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "database": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0e3a"
                 "1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "session-cache": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f"
                      "0e3a1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "shared-storage": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0"
                       "f0e3a1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "object-cache": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0e"
                     "3a1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "page-cache": ("http://ddf912383141a8d7bbe4-e053e711fc85de3290f121ef0f0e3a"
                   "1f.r87.cf1.rackcdn.com/cloud-databases-icon.png"),
    "magento": ("http://design2themes.com/images/magento.png"),
    "magento-worker": ("http://design2themes.com/images/magento.png"),
    "unknown": ("https://cdn3.iconfinder.com/data/icons/supermario/PNG/Quest"
                "ion Block.png")
}


def status_to_color(status):
    if status in ["NEW", "ONLINE", "ACTIVE"]:
        return COLORS["ok"]
    if status in ["ERROR", "DELETED", "DELETING", "OFFLINE"]:
        return COLORS["error"]
    if status in ["BUILD", "CONFIGURE"]:
        return COLORS["processing"]
    return COLORS["disabled"]


def service_to_icon(type):
    if type in ICONS:
        return ICONS.get(type)
    return ICONS['unknown']


def resources_to_slack_attachments(resources):
    """Resources is the full JSON object in a Checkmate deployment"""
    data = []
    for resource_id, resource_data in resources.iteritems():
        if 'status' in resource_data and 'type' in resource_data:
            text = []
            text.append('Type: %s' % resource_data.get('type'))

            if 'instance' in resource_data:
                if resource_data['instance'].get('id'):
                    text.append('ID: %s' % resource_data['instance'].get(
                        'id'))
                if resource_data['instance'].get('host_region'):
                    text.append('Region: %s' %
                                resource_data['instance'].get('host_region'))
                elif resource_data.get('desired-state'):
                    dstate = resource_data.get('desired-state')
                    if dstate.get('region'):
                        text.append('Region: %s' % dstate.get('region'))
            if 'status' in resource_data:
                text.append('Status: %s' % resource_data.get('status'))

            name = resource_data.get("dns-name", 'Unknown Name')

            text = '\n'.join(text)

            data.append({
                "color": status_to_color(resource_data.get("status")),
                "author_name": name,
                "author_icon": service_to_icon(resource_data.get('service')),
                "text": text
            })
    return data


class ShowDeploymentSlackFormatAction(Action):
    def run(self, deployment):
        """Deployment is the full JSON object of a Checkmate deployment."""
        deployment = json.loads(deployment)
        slack_attachments = resources_to_slack_attachments(
            deployment.get("resources"))

        return json.dumps(slack_attachments)
