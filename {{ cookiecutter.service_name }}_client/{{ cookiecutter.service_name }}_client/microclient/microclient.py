import json

import requests


class MicroClientException(Exception):
    """
    micro client exception
    """


class MicroClient:
    def __init__(self, base_url: str, access_token: str = None) -> str:
        self.base_url = base_url

        # prepare session   
        self._s = requests.Session()
        self.access_token = access_token

    @property
    def access_token(self) -> str:
        """
        get the access token

        :return: access token
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, value: str):
        """
        set the access token and prepare session's header
        for all following calls
        """
        self._access_token = value
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}",
            "Content-Type": "application/json"
        })

    def get_token(self, username: str, password: str) -> str:
        """
        get bearer token that is required for all following requests

        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :return: token
        :rtype: str
        """
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        data = {
            "username": username,
            "password": password
        }

        # post request
        r = self._s.post(
            url=f"{self.base_url}/token", 
            data=data, 
            headers=headers
        )

        if "access_token" not in r.json():
            # access token could not be obtained
            raise MicroClientException(
                f"could not obtain the access token: {r.json()}"
            )
        
        # get access token from response
        return r.json()["access_token"]

    def get_all(self) -> list:
        """
        returns a list of all {{ cookiecutter.item_name }}s
        """
        r = self._s.get(
            url=f"{self.base_url}/{{ cookiecutter.item_name }}s/",
        )

        return r.json()

    def get(self, id: str) -> dict:
        """
        returns a {{ cookiecutter.item_name }} by given ID
        """
        r = self._s.get(
            url=f"{self.base_url}/{{ cookiecutter.item_name }}s/{id}/",
        )

        return r.json()

    def delete(self, id: str) -> dict:
        """
        delete {{ cookiecutter.item_name }} by given ID
        """
        r = self._s.delete(
            url=f"{self.base_url}/{{ cookiecutter.item_name }}s/{id}/",
        )

        return r.json()

    def create(self, id: str, name: str) -> dict:
        """
        create {{ cookiecutter.item_name }}
        """
        data = json.dumps({
            "id": id,
            "name": name
        })

        r = self._s.post(
            url=f"{self.base_url}/{{ cookiecutter.item_name }}s/",
            data=data
        )

        return r.json()

    def update(self, id: str, name: str) -> dict:
        """
        update {{ cookiecutter.item_name }} by given ID
        """
        data = json.dumps({
            "id": id,
            "name": name
        })

        r = self._s.patch(
            url=f"{self.base_url}/{{ cookiecutter.item_name }}s/{id}/",
            data=data
        )

        return r.json()
