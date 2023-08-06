from GitHubSDK.base import GitHubBase
from GitHubSDK.repository import Repository
from GitHubSDK.userkey import UserKey

DEFAULT_USER_URL = "/users/"


class User(GitHubBase):

    def __init__(self, requester, attributes):
        super().__init__(requester, attributes)
        self._bio = attributes['bio']
        self._company = attributes['company']
        self._created_at = attributes['created_at']
        self._email = attributes['email']
        self._events_url = attributes['events_url']
        self._followers = attributes['followers']
        self._id = attributes['id']
        self._location = attributes['location']
        self._login = attributes['login']
        self._name = attributes['name']
        self._organizations_url = attributes['organizations_url']
        self._public_repos = attributes['public_repos']
        self._repos_url = attributes['repos_url']
        self._type = attributes['type']
        self._updated_at = attributes['updated_at']
        self._url = attributes['url']

    def __repr__(self):
        return self.get__repr__({"login": self._login})

    def __repr_html(self):
        return self.__repr_html()

    @property
    def bio(self):
        """
        :type: integer
        """
        return self._bio

    @property
    def company(self):
        """
        :type: string
        """
        return self._company

    @property
    def contributions(self):
        """
        :type: integer
        """
        return self._contributions

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._created_at

    @property
    def email(self):
        """
        :type: string
        """
        return self._email

    @property
    def events_url(self):
        """
        :type: string
        """
        return self._events_url

    @property
    def followers(self):
        """
        :type: integer
        """
        return self._followers

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

    @property
    def location(self):
        """
        :type: string
        """
        return self._location

    @property
    def login(self):
        """
        :type: string
        """
        return self._login

    @property
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def organizations_url(self):
        """
        :type: string
        """
        return self._organizations_url

    @property
    def owned_private_repos(self):
        """
        :type: integer
        """
        return self._owned_private_repos

    @property
    def public_repos(self):
        """
        :type: integer
        """
        return self._public_repos

    @property
    def repos_url(self):
        """
        :type: string
        """
        return self._repos_url

    @property
    def role(self):
        """
        :type: string
        """
        return self._role

    @property
    def type(self):
        """
        :type: string
        """
        return self._type

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._updated_at

    @property
    def url(self):
        """
        :type: string
        """
        return self._url

    def get_results(self, url):
        data = self.requester.request("get", f"{self.url}/{url}")
        json_data = data.json()
        return json_data

    def get_orgs(self):
        data = self.get_results("orgs")
        return data

    def get_keys(self):
        data = self.get_results("keys")
        keys_list = []
        if data and isinstance(data, list):
            for key in data:
                keys_list.append(UserKey(self.requester, attributes=key))
        return keys_list

    def get_repos(self):
        data = self.get_results("repos")
        repo_list = []
        if data and isinstance(data, list):
            for repo in data:
                repo_list.append(Repository(self.requester, attributes=repo))
        return repo_list

    def create_repo(
            self,
            token,
            name,
            description,
    ):

        post_parameters = {
            "headers": {
                "name": name,
                "description": description,
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.inertia-preview+json",
            }
        }
        data = self.requester.post("/user/repos", **post_parameters)

        return data.json()

