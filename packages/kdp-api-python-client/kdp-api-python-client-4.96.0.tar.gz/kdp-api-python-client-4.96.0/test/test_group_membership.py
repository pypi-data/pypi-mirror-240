"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification. <p><b>By default this api documentation targets the koverse production server at 'api.app.koverse.com' You can provide the hostname of your koverse instance to this documentation page via the 'host' query param.</p> <p><b>For example providing host - https://documentation.koverse.com/api?host=api.myHost.com, will update requests to target the provided host.</b></p> <p><b>Authentication request example with provided host - https://api.myHost.com/authentication</b></p>  # noqa: E501

    The version of the OpenAPI document: 4.96.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kdp_api
from kdp_api.model.group import Group
from kdp_api.model.user import User
globals()['Group'] = Group
globals()['User'] = User
from kdp_api.model.group_membership import GroupMembership


class TestGroupMembership(unittest.TestCase):
    """GroupMembership unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupMembership(self):
        """Test GroupMembership"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GroupMembership()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
