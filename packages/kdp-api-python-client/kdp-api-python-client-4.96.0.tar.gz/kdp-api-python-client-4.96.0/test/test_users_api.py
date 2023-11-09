"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification. <p><b>By default this api documentation targets the koverse production server at 'api.app.koverse.com' You can provide the hostname of your koverse instance to this documentation page via the 'host' query param.</p> <p><b>For example providing host - https://documentation.koverse.com/api?host=api.myHost.com, will update requests to target the provided host.</b></p> <p><b>Authentication request example with provided host - https://api.myHost.com/authentication</b></p>  # noqa: E501

    The version of the OpenAPI document: 4.96.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kdp_api
from kdp_api.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_id(self):
        """Test case for delete_users_id

        Removes the user by given id  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Retrieves a list of users  # noqa: E501
        """
        pass

    def test_get_users_id(self):
        """Test case for get_users_id

        Retrieves a user with the given id from the users service.  # noqa: E501
        """
        pass

    def test_patch_users_id(self):
        """Test case for patch_users_id

        Updates the resource by id for the fields provided  # noqa: E501
        """
        pass

    def test_post_user(self):
        """Test case for post_user

        Create a user  # noqa: E501
        """
        pass

    def test_put_users_id(self):
        """Test case for put_users_id

        Updates a user with given id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
