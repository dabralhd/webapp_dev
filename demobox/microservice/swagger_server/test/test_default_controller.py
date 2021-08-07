# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.app_creation_result import AppCreationResult  # noqa: E501
from swagger_server.models.app_manager_error import AppManagerError  # noqa: E501
from swagger_server.models.app_target import AppTarget  # noqa: E501
from swagger_server.models.app_type import AppType  # noqa: E501
from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.set_env_result import SetEnvResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create(self):
        """Test case for create

        crete a new application instance
        """
        query_string = [('app_name', 'app_name_example'),
                        ('user_uuid', 'user_uuid_example'),
                        ('app_type', AppType()),
                        ('app_target', AppTarget()),
                        ('board_name', 'board_name_example')]
        data = dict(dnn_model_name='dnn_model_name_example',
                    app_code='app_code_example')
        response = self.client.open(
            '/appmgr/create',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve(self):
        """Test case for retrieve

        set execution environment and executes a given application
        """
        query_string = [('app_uuid', 'app_uuid_example'),
                        ('user_uuid', 'user_uuid_example')]
        response = self.client.open(
            '/appmgr/execute',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_0(self):
        """Test case for retrieve_0

        retrieve metadata about an application
        """
        query_string = [('app_uuid', 'app_uuid_example'),
                        ('user_uuid', 'user_uuid_example')]
        response = self.client.open(
            '/appmgr/retrieve',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_setenv(self):
        """Test case for setenv

        set execution environment
        """
        query_string = [('app_uuid', 'app_uuid_example')]
        response = self.client.open(
            '/appmgr/setenv',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
