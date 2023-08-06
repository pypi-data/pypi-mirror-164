from GitHubSDK.base import GitHubBase


class Organization(GitHubBase):

    def __init__(self, requester, attributes):
        super().__init__(requester, attributes)
        self._blog = attributes["blog"]
        self._company = attributes['company']
        self._created_at = attributes['created_at']
        self._description = attributes['description']
        self._email = attributes['email']
        self._following = attributes['following']
        self._followers = attributes['followers']
        self._id = attributes['id']
        self._has_organization_projects = attributes['has_organization_projects']
        self._login = attributes['login']
        self._name = attributes['name']
        self._has_repository_projects = attributes['has_repository_projects']
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
    def blog(self):
        """
        :type: integer
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
    def description(self):
        """
        :type: string
        """
        return self._description

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
    def has_organization_projects(self):
        """
        :type: bool
        """
        return self._has_organization_projects

    @property
    def has_repository_projects(self):
        """
        :type: bool
        """
        return self._has_repository_projects

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
    def total_private_repos(self):
        """
        :type: integer
        """
        return self._total_private_repos


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

    def create_project(self, name, body):
        print(self.url+"/projects")
        post_parameters = dict(
            name=name,
            body=body
        )
        self.requester.request("post", f"{self.url}/projects", **post_parameters)
