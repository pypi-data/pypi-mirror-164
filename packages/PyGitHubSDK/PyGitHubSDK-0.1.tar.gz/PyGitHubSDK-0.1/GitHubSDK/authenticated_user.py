from GitHubSDK.base import GitHubBase


class AuthenticatedUser(GitHubBase):
    def __init__(self, requester, attritbutes):
        super().__init__(requester, attritbutes)
        self._avatar_url = attritbutes['avatar_url']
        self._bio = attritbutes['bio']
        self._blog = attritbutes['blog']
        self._company = attritbutes['company']
        self._created_at = attritbutes['created_at']
        self._email = attritbutes['email']
        self._followers = attritbutes['followers']
        self._following = attritbutes['following']
        self._id = attritbutes['id']
        self._login = attritbutes['login']
        self._name = attritbutes['name']
        self._organizations_url = attritbutes['organizations_url']
        self._owned_private_repos = attritbutes['owned_private_repos']
        self._public_repos = attritbutes['public_repos']
        self._repos_url = attritbutes['repos_url']
        self._subscriptions_url = attritbutes['subscriptions_url']
        self._type = attritbutes['type']
        self._updated_at = attritbutes['updated_at ']
        self._url = attritbutes['url']

    def __repr__(self):
        return self.get__repr__({"login": self._login})

    @property
    def avatar_url(self):
        """
        :type: string
        """
        return self._avatar_url

    @property
    def bio(self):
        """
        :type: string
        """
        return self._bio

    @property
    def blog(self):
        """
        :type: string
        """
        return self._blog

    @property
    def company(self):
        """
        :type: string
        """
        return self._company

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
    def followers(self):
        """
        :type: integer
        """
        return self._followers

    @property
    def following(self):
        """
        :type: integer
        """
        return self._following

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

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
    def subscriptions_url(self):
        """
        :type: string
        """
        return self._subscriptions_url

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