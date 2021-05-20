# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cube_ai_analyze_result import CubeAIAnalyzeResult  # noqa: E501
from swagger_server.models.cube_ai_error import CubeAIError  # noqa: E501
from swagger_server.models.cube_ai_generate_result import CubeAIGenerateResult  # noqa: E501
from swagger_server.models.cube_ai_validate_result import CubeAIValidateResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_analyze(self):
        """Test case for analyze

        Analyze Input Model
        """
        query_string = [('allocate_inputs', true),
                        ('allocate_outputs', true),
                        ('compression', 56),
                        ('name', 'name_example'),
                        ('split_weights', true)]
        data = dict(deep_learning_model='deep_learning_model_example',
                    quantize='quantize_example')
        response = self.client.open(
            '/stredai/analyze',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generate(self):
        """Test case for generate

        Generate Input Model
        """
        query_string = [('address', 'address_example'),
                        ('allocate_inputs', true),
                        ('allocate_outputs', true),
                        ('binary', true),
                        ('compression', 56),
                        ('copy_weights_at', 'copy_weights_at_example'),
                        ('full_binary_uuid', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                        ('generate_fota', true),
                        ('name', 'name_example'),
                        ('split_weights', true),
                        ('generate_full_binary', true),
                        ('return_full_binary_only', true)]
        data = dict(deep_learning_model='deep_learning_model_example',
                    quantize='quantize_example')
        response = self.client.open(
            '/stredai/generate',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate(self):
        """Test case for validate

        Validate Input Model
        """
        query_string = [('allocate_inputs', true),
                        ('allocate_outputs', true),
                        ('batches', 56),
                        ('classifier', true),
                        ('compression', 56),
                        ('name', 'name_example'),
                        ('split_weights', true),
                        ('validate_batch_mode', 'validate_batch_mode_example')]
        data = dict(deep_learning_model='deep_learning_model_example',
                    quantize='quantize_example',
                    valinput='valinput_example',
                    valoutput='valoutput_example')
        response = self.client.open(
            '/stredai/validate',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
