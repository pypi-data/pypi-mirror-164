# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.configuration import Configuration


class ProductMessage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'reference': 'str',
        'warnings': 'list[str]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'reference': 'Reference',
        'warnings': 'Warnings',
        'errors': 'Errors'
    }

    def __init__(self, name=None, reference=None, warnings=None, errors=None, local_vars_configuration=None):  # noqa: E501
        """ProductMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._reference = None
        self._warnings = None
        self._errors = None
        self.discriminator = None

        self.name = name
        self.reference = reference
        self.warnings = warnings
        self.errors = errors

    @property
    def name(self):
        """Gets the name of this ProductMessage.  # noqa: E501


        :return: The name of this ProductMessage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductMessage.


        :param name: The name of this ProductMessage.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def reference(self):
        """Gets the reference of this ProductMessage.  # noqa: E501


        :return: The reference of this ProductMessage.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ProductMessage.


        :param reference: The reference of this ProductMessage.  # noqa: E501
        :type reference: str
        """

        self._reference = reference

    @property
    def warnings(self):
        """Gets the warnings of this ProductMessage.  # noqa: E501


        :return: The warnings of this ProductMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ProductMessage.


        :param warnings: The warnings of this ProductMessage.  # noqa: E501
        :type warnings: list[str]
        """

        self._warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this ProductMessage.  # noqa: E501


        :return: The errors of this ProductMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ProductMessage.


        :param errors: The errors of this ProductMessage.  # noqa: E501
        :type errors: list[str]
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductMessage):
            return True

        return self.to_dict() != other.to_dict()
