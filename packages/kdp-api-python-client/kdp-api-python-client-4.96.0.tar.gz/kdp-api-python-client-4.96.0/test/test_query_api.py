"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification. <p><b>By default this api documentation targets the koverse production server at 'api.app.koverse.com' You can provide the hostname of your koverse instance to this documentation page via the 'host' query param.</p> <p><b>For example providing host - https://documentation.koverse.com/api?host=api.myHost.com, will update requests to target the provided host.</b></p> <p><b>Authentication request example with provided host - https://api.myHost.com/authentication</b></p>  # noqa: E501

    The version of the OpenAPI document: 4.96.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kdp_api
from kdp_api.api.query_api import QueryApi  # noqa: E501


class TestQueryApi(unittest.TestCase):
    """QueryApi unit test stubs"""

    def setUp(self):
        self.api = QueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_lucene_query(self):
        """Test case for post_lucene_query

        Query a dataset using the lucene query syntax  # noqa: E501
        """
        pass

    def test_post_lucene_query_document(self):
        """Test case for post_lucene_query_document

        Query document for a dataset using the lucene query syntax  # noqa: E501
        """
        pass

    def test_post_query(self):
        """Test case for post_query

        Query a dataset  # noqa: E501
        """
        pass

    def test_post_query_summary(self):
        """Test case for post_query_summary

        Query all datasets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
