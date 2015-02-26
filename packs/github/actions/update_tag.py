from lib.base import BaseGithubAction
import re

__all__ = [
    'UpdateTagAction'
]


class UpdateTagAction(BaseGithubAction):
    def run(self, user, repo, tag, object=None):
        if object is None:
            object = 'master'

        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        if not re.match(u"[a-fA-F0-9]{40}", object):
            branch = repo.get_branch(object)
            object = branch.commit.sha
        tagobj = repo.get_git_ref('tags/%s' % tag)
        tagobj.edit(object)

        return tagobj.object.sha
