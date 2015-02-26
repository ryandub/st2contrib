from lib.base import BaseGithubAction

__all__ = [
    'UpdateTagAction'
]


class UpdateTagAction(BaseGithubAction):
    def run(self, user, repo, tag, object='master'):

        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        if not object.matches("[a-fA-F0-9]{40}"):
            branch = repo.get_branch(object)
            object = branch.commit.sha
        tagobj = repo.get_git_ref('tags/%' % tag)
        ref = tagobj.edit(object)

        return ref.object.sha
