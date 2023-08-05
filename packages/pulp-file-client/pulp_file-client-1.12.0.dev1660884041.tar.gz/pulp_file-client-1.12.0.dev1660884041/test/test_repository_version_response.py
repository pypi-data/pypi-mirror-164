# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.models.repository_version_response import RepositoryVersionResponse  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException

class TestRepositoryVersionResponse(unittest.TestCase):
    """RepositoryVersionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryVersionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_file.models.repository_version_response.RepositoryVersionResponse()  # noqa: E501
        if include_optional :
            return RepositoryVersionResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                number = 56, 
                repository = '0', 
                base_version = '0', 
                content_summary = null
            )
        else :
            return RepositoryVersionResponse(
        )

    def testRepositoryVersionResponse(self):
        """Test RepositoryVersionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
