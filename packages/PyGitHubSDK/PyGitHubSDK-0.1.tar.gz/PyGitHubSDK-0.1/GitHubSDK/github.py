from GitHubSDK.requester import Requester
import requests
from operator import itemgetter
from GitHubSDK.user import User
from GitHubSDK.organization import Organization


DEFUALT_BASE_URL = "https://api.github.com"
DEFUALT_USER_AGENT = "gitHubSDK/Python"

class GitHub:

    def __init__(
            self,
            base_url=DEFUALT_BASE_URL,
            login_or_token=None,
            password=None,
            user_agent=DEFUALT_USER_AGENT
    ):
        self.base_url = base_url
        if password is not None:
            self.username = login_or_token
        elif login_or_token is not None:
            self.token = login_or_token
        self.password = password
        self.user_agent = user_agent
        self.auth = requests.auth.HTTPBasicAuth(login_or_token, password)
        self.authHeader = {"Authorization": f"token {self.token}"}

        params = dict(
            auth=self.auth,
            user_agent=self.user_agent,
        )
        self.__requester = Requester(
            base_url=self.base_url,
            auth_header=self.authHeader,
            **params
        )

    def get__repr__(self, params):
        """
        Converts the object to a nicely printable string.
        """

        def format_params(params):
            items = list(params.items())
            for k, v in sorted(items, key=itemgetter(0), reverse=True):
                if isinstance(v, bytes):
                    v = v.decode("utf-8")
                if isinstance(v, str):
                    v = f'"{v}"'
                yield f"{k}={v}"

        return "{class_name}({params})".format(
            class_name=self.__class__.__name__,
            params=", ".join(list(format_params(params))),
        )

    def get_user(self, user):
        data = self.__requester.get(f"/users/{user}")
        json_data = data.json()
        print(json_data)
        return User(self.__requester, attributes=json_data)

    def get_authenticated_user(self):
        data = self.__requester.get("/user")
        return data

    def get_orgs(self, organization):
        data = self.__requester.get(f"/orgs/{organization}")
        json_data = data.json()
        return Organization(self.__requester, attributes=json_data)
