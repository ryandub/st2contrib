from lib.base import BaseGithubAction

__all__ = [
    'AddTagAction'
]


class AddTagAction(BaseGithubAction):
    def run(self, user, repo, tag, message, object, type):

        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        tagobj = repo.create_git_tag(tag, message, object, type)
        ref = repo.create_git_ref(('refs/tags/%s' % tag), tagobj.sha)

        return ref.object.sha
