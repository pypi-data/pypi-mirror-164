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


class MerchantOrderAcknowledgementRequest(object):
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
        'merchant_order_no': 'str',
        'order_id': 'int'
    }

    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',
        'order_id': 'OrderId'
    }

    def __init__(self, merchant_order_no=None, order_id=None, local_vars_configuration=None):  # noqa: E501
        """MerchantOrderAcknowledgementRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merchant_order_no = None
        self._order_id = None
        self.discriminator = None

        self.merchant_order_no = merchant_order_no
        self.order_id = order_id

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this MerchantOrderAcknowledgementRequest.  # noqa: E501

        Your own order reference, this will be used in consecutive order processing API calls.  # noqa: E501

        :return: The merchant_order_no of this MerchantOrderAcknowledgementRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this MerchantOrderAcknowledgementRequest.

        Your own order reference, this will be used in consecutive order processing API calls.  # noqa: E501

        :param merchant_order_no: The merchant_order_no of this MerchantOrderAcknowledgementRequest.  # noqa: E501
        :type merchant_order_no: str
        """
        if self.local_vars_configuration.client_side_validation and merchant_order_no is None:  # noqa: E501
            raise ValueError("Invalid value for `merchant_order_no`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_order_no is not None and len(merchant_order_no) > 50):
            raise ValueError("Invalid value for `merchant_order_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                merchant_order_no is not None and len(merchant_order_no) < 0):
            raise ValueError("Invalid value for `merchant_order_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._merchant_order_no = merchant_order_no

    @property
    def order_id(self):
        """Gets the order_id of this MerchantOrderAcknowledgementRequest.  # noqa: E501

        The ChannelEngine order ID of the order you would like to acknowledge.  # noqa: E501

        :return: The order_id of this MerchantOrderAcknowledgementRequest.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MerchantOrderAcknowledgementRequest.

        The ChannelEngine order ID of the order you would like to acknowledge.  # noqa: E501

        :param order_id: The order_id of this MerchantOrderAcknowledgementRequest.  # noqa: E501
        :type order_id: int
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if not isinstance(other, MerchantOrderAcknowledgementRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantOrderAcknowledgementRequest):
            return True

        return self.to_dict() != other.to_dict()
