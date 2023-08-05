# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.9.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_channel_api_client.configuration import Configuration


class ChannelReturnLineRequest(object):
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
        'channel_product_no': 'str',
        'merchant_product_no': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'channel_product_no': 'ChannelProductNo',
        'merchant_product_no': 'MerchantProductNo',
        'quantity': 'Quantity'
    }

    def __init__(self, channel_product_no=None, merchant_product_no=None, quantity=None, local_vars_configuration=None):  # noqa: E501
        """ChannelReturnLineRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channel_product_no = None
        self._merchant_product_no = None
        self._quantity = None
        self.discriminator = None

        self.channel_product_no = channel_product_no
        self.merchant_product_no = merchant_product_no
        self.quantity = quantity

    @property
    def channel_product_no(self):
        """Gets the channel_product_no of this ChannelReturnLineRequest.  # noqa: E501

        The unique product reference used by the Channel.  # noqa: E501

        :return: The channel_product_no of this ChannelReturnLineRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """Sets the channel_product_no of this ChannelReturnLineRequest.

        The unique product reference used by the Channel.  # noqa: E501

        :param channel_product_no: The channel_product_no of this ChannelReturnLineRequest.  # noqa: E501
        :type channel_product_no: str
        """

        self._channel_product_no = channel_product_no

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this ChannelReturnLineRequest.  # noqa: E501

        The unique product reference used by the Merchant.  # noqa: E501

        :return: The merchant_product_no of this ChannelReturnLineRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this ChannelReturnLineRequest.

        The unique product reference used by the Merchant.  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this ChannelReturnLineRequest.  # noqa: E501
        :type merchant_product_no: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def quantity(self):
        """Gets the quantity of this ChannelReturnLineRequest.  # noqa: E501

        Number of items of the product in this return.  # noqa: E501

        :return: The quantity of this ChannelReturnLineRequest.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ChannelReturnLineRequest.

        Number of items of the product in this return.  # noqa: E501

        :param quantity: The quantity of this ChannelReturnLineRequest.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quantity is not None and quantity < 0):  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quantity = quantity

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
        if not isinstance(other, ChannelReturnLineRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelReturnLineRequest):
            return True

        return self.to_dict() != other.to_dict()
