# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CubeAIValidateResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, network_report: object=None, network_c_graph: object=None):  # noqa: E501
        """CubeAIValidateResult - a model defined in Swagger

        :param network_report: The network_report of this CubeAIValidateResult.  # noqa: E501
        :type network_report: object
        :param network_c_graph: The network_c_graph of this CubeAIValidateResult.  # noqa: E501
        :type network_c_graph: object
        """
        self.swagger_types = {
            'network_report': object,
            'network_c_graph': object
        }

        self.attribute_map = {
            'network_report': 'network_report',
            'network_c_graph': 'network_c_graph'
        }
        self._network_report = network_report
        self._network_c_graph = network_c_graph

    @classmethod
    def from_dict(cls, dikt) -> 'CubeAIValidateResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CubeAIValidateResult of this CubeAIValidateResult.  # noqa: E501
        :rtype: CubeAIValidateResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network_report(self) -> object:
        """Gets the network_report of this CubeAIValidateResult.


        :return: The network_report of this CubeAIValidateResult.
        :rtype: object
        """
        return self._network_report

    @network_report.setter
    def network_report(self, network_report: object):
        """Sets the network_report of this CubeAIValidateResult.


        :param network_report: The network_report of this CubeAIValidateResult.
        :type network_report: object
        """
        if network_report is None:
            raise ValueError("Invalid value for `network_report`, must not be `None`")  # noqa: E501

        self._network_report = network_report

    @property
    def network_c_graph(self) -> object:
        """Gets the network_c_graph of this CubeAIValidateResult.


        :return: The network_c_graph of this CubeAIValidateResult.
        :rtype: object
        """
        return self._network_c_graph

    @network_c_graph.setter
    def network_c_graph(self, network_c_graph: object):
        """Sets the network_c_graph of this CubeAIValidateResult.


        :param network_c_graph: The network_c_graph of this CubeAIValidateResult.
        :type network_c_graph: object
        """
        if network_c_graph is None:
            raise ValueError("Invalid value for `network_c_graph`, must not be `None`")  # noqa: E501

        self._network_c_graph = network_c_graph