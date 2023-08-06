import json

from GitHubSDK.base import GitHubBase


class Repository(GitHubBase):

    def __init__(self, requester, attributes):
        super().__init__(requester, attributes)
        self._archived = attributes['archived']
        self._branches_url = attributes['branches_url']
        self._clone_url = attributes['clone_url']
        self._commits_url = attributes['commits_url']
        self._created_at = attributes['created_at']
        self._default_branch = attributes['default_branch']
        self._id = attributes['id']
        self._description = attributes['description']
        self._full_name = attributes['full_name']
        self._git_commits_url = attributes['git_commits_url']
        self._git_url = attributes['git_url']
        self._owner = attributes['owner']
        self._visibility = attributes['visibility']
        self._updated_at = attributes['updated_at']
        self._url = attributes['url']

    def __repr__(self):
        return self.get__repr__({"full_name": self.full_name})

    def __repr_html(self):
        return self.__repr_html()

    @property
    def allow_forking(self):
        """
        :type: string
        """
        return self._allow_forking

    @property
    def archived(self):
        """
        :type: string
        """
        return self._archived

    @property
    def branches_url(self):
        """
        :type: datetime.datetime
        """
        return self._branches_url

    @property
    def clone_url(self):
        """
        :type: string
        """
        return self._clone_url

    @property
    def commits_url(self):
        """
        :type: string
        """
        return self._commits_url

    @property
    def default_branch(self):
        """
        :type: integer
        """
        return self._default_branch

    @property
    def created_at(self):
        """
        :type: integer
        """
        return self._created_at

    @property
    def description(self):
        """
        :type: bool
        """
        return self._description

    @property
    def git_url(self):
        """
        :type: bool
        """
        return self._git_url

    @property
    def url(self):
        """
        :type: bool
        """
        return self._url

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

    @property
    def full_name(self):
        """
        :type: string
        """
        return self._full_name

    @property
    def git_commits_url(self):
        """
        :type: string
        """
        return self._git_commits_url

    @property
    def owner(self):
        """
        :type: User
        """
        return self._owner

    @property
    def repos_url(self):
        """
        :type: string
        """
        return self._repos_url

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._updated_at

    @property
    def visibility(self):
        """
         :type: string
        """
        return self._visibility

    def create_project(self, name, body):
        post_parameters = {
            "name": name,
            "body": body
        }
        params = dict(
            data=json.dumps(post_parameters)
        )
        self.requester.request("post", f"{self.url}/projects", **params)

    def create_file(
        self,
        path,
        message,
        content,
        branch=None,
        committer=None,
        author=None,
    ):
        put_parameters = {
            "message": message,
            "content": content,
        }

        if branch:
            put_parameters["branch"] = branch
        if author:
            put_parameters["author"] = author
        if committer:
            put_parameters["committer"] = committer
        params = dict(
            data=json.dumps(put_parameters)
        )

        data = self.requester.request(
            "PUT",
            f"{self.url}/contents/{path}",
            **params
        )

        return data

