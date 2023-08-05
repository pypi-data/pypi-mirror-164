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


class ChannelAddressRequest(object):
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
        'gender': 'Gender',
        'company_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'street_name': 'str',
        'house_nr': 'str',
        'house_nr_addition': 'str',
        'zip_code': 'str',
        'city': 'str',
        'region': 'str',
        'country_iso': 'str',
        'original': 'str'
    }

    attribute_map = {
        'gender': 'Gender',
        'company_name': 'CompanyName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'street_name': 'StreetName',
        'house_nr': 'HouseNr',
        'house_nr_addition': 'HouseNrAddition',
        'zip_code': 'ZipCode',
        'city': 'City',
        'region': 'Region',
        'country_iso': 'CountryIso',
        'original': 'Original'
    }

    def __init__(self, gender=None, company_name=None, first_name=None, last_name=None, street_name=None, house_nr=None, house_nr_addition=None, zip_code=None, city=None, region=None, country_iso=None, original=None, local_vars_configuration=None):  # noqa: E501
        """ChannelAddressRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gender = None
        self._company_name = None
        self._first_name = None
        self._last_name = None
        self._street_name = None
        self._house_nr = None
        self._house_nr_addition = None
        self._zip_code = None
        self._city = None
        self._region = None
        self._country_iso = None
        self._original = None
        self.discriminator = None

        self.gender = gender
        self.company_name = company_name
        self.first_name = first_name
        self.last_name = last_name
        self.street_name = street_name
        self.house_nr = house_nr
        self.house_nr_addition = house_nr_addition
        self.zip_code = zip_code
        self.city = city
        self.region = region
        self.country_iso = country_iso
        self.original = original

    @property
    def gender(self):
        """Gets the gender of this ChannelAddressRequest.  # noqa: E501

        Optional. The customer's gender.  # noqa: E501

        :return: The gender of this ChannelAddressRequest.  # noqa: E501
        :rtype: Gender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ChannelAddressRequest.

        Optional. The customer's gender.  # noqa: E501

        :param gender: The gender of this ChannelAddressRequest.  # noqa: E501
        :type gender: Gender
        """

        self._gender = gender

    @property
    def company_name(self):
        """Gets the company_name of this ChannelAddressRequest.  # noqa: E501

        Optional. Company addressed too.  # noqa: E501

        :return: The company_name of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ChannelAddressRequest.

        Optional. Company addressed too.  # noqa: E501

        :param company_name: The company_name of this ChannelAddressRequest.  # noqa: E501
        :type company_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) > 50):
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) < 0):
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._company_name = company_name

    @property
    def first_name(self):
        """Gets the first_name of this ChannelAddressRequest.  # noqa: E501

        The first name of the customer.  # noqa: E501

        :return: The first_name of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ChannelAddressRequest.

        The first name of the customer.  # noqa: E501

        :param first_name: The first_name of this ChannelAddressRequest.  # noqa: E501
        :type first_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 50):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) < 0):
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ChannelAddressRequest.  # noqa: E501

        The last name of the customer (includes the surname prefix [tussenvoegsel] like 'de', 'van', 'du').  # noqa: E501

        :return: The last_name of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ChannelAddressRequest.

        The last name of the customer (includes the surname prefix [tussenvoegsel] like 'de', 'van', 'du').  # noqa: E501

        :param last_name: The last_name of this ChannelAddressRequest.  # noqa: E501
        :type last_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 50):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) < 0):
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_name = last_name

    @property
    def street_name(self):
        """Gets the street_name of this ChannelAddressRequest.  # noqa: E501

        The name of the street (without house number information)  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :return: The street_name of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ChannelAddressRequest.

        The name of the street (without house number information)  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :param street_name: The street_name of this ChannelAddressRequest.  # noqa: E501
        :type street_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                street_name is not None and len(street_name) > 50):
            raise ValueError("Invalid value for `street_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                street_name is not None and len(street_name) < 0):
            raise ValueError("Invalid value for `street_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._street_name = street_name

    @property
    def house_nr(self):
        """Gets the house_nr of this ChannelAddressRequest.  # noqa: E501

        The house number  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :return: The house_nr of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._house_nr

    @house_nr.setter
    def house_nr(self, house_nr):
        """Sets the house_nr of this ChannelAddressRequest.

        The house number  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :param house_nr: The house_nr of this ChannelAddressRequest.  # noqa: E501
        :type house_nr: str
        """
        if (self.local_vars_configuration.client_side_validation and
                house_nr is not None and len(house_nr) > 50):
            raise ValueError("Invalid value for `house_nr`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                house_nr is not None and len(house_nr) < 0):
            raise ValueError("Invalid value for `house_nr`, length must be greater than or equal to `0`")  # noqa: E501

        self._house_nr = house_nr

    @property
    def house_nr_addition(self):
        """Gets the house_nr_addition of this ChannelAddressRequest.  # noqa: E501

        Optional. Addition to the house number  If the address is: Groenhazengracht 2c, the address will be:  StreetName: Groenhazengracht  HouseNo: 2  HouseNrAddition: c  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :return: The house_nr_addition of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._house_nr_addition

    @house_nr_addition.setter
    def house_nr_addition(self, house_nr_addition):
        """Sets the house_nr_addition of this ChannelAddressRequest.

        Optional. Addition to the house number  If the address is: Groenhazengracht 2c, the address will be:  StreetName: Groenhazengracht  HouseNo: 2  HouseNrAddition: c  This field might be empty if address validation is disabled in ChannelEngine.  # noqa: E501

        :param house_nr_addition: The house_nr_addition of this ChannelAddressRequest.  # noqa: E501
        :type house_nr_addition: str
        """
        if (self.local_vars_configuration.client_side_validation and
                house_nr_addition is not None and len(house_nr_addition) > 50):
            raise ValueError("Invalid value for `house_nr_addition`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                house_nr_addition is not None and len(house_nr_addition) < 0):
            raise ValueError("Invalid value for `house_nr_addition`, length must be greater than or equal to `0`")  # noqa: E501

        self._house_nr_addition = house_nr_addition

    @property
    def zip_code(self):
        """Gets the zip_code of this ChannelAddressRequest.  # noqa: E501

        The zip or postal code.  # noqa: E501

        :return: The zip_code of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this ChannelAddressRequest.

        The zip or postal code.  # noqa: E501

        :param zip_code: The zip_code of this ChannelAddressRequest.  # noqa: E501
        :type zip_code: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this ChannelAddressRequest.  # noqa: E501

        The name of the city.  # noqa: E501

        :return: The city of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ChannelAddressRequest.

        The name of the city.  # noqa: E501

        :param city: The city of this ChannelAddressRequest.  # noqa: E501
        :type city: str
        """
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) > 50):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) < 0):
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `0`")  # noqa: E501

        self._city = city

    @property
    def region(self):
        """Gets the region of this ChannelAddressRequest.  # noqa: E501

        Optional. State/province/region.  # noqa: E501

        :return: The region of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ChannelAddressRequest.

        Optional. State/province/region.  # noqa: E501

        :param region: The region of this ChannelAddressRequest.  # noqa: E501
        :type region: str
        """
        if (self.local_vars_configuration.client_side_validation and
                region is not None and len(region) > 50):
            raise ValueError("Invalid value for `region`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                region is not None and len(region) < 0):
            raise ValueError("Invalid value for `region`, length must be greater than or equal to `0`")  # noqa: E501

        self._region = region

    @property
    def country_iso(self):
        """Gets the country_iso of this ChannelAddressRequest.  # noqa: E501

        For example: NL, BE, FR.  # noqa: E501

        :return: The country_iso of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_iso

    @country_iso.setter
    def country_iso(self, country_iso):
        """Sets the country_iso of this ChannelAddressRequest.

        For example: NL, BE, FR.  # noqa: E501

        :param country_iso: The country_iso of this ChannelAddressRequest.  # noqa: E501
        :type country_iso: str
        """
        if (self.local_vars_configuration.client_side_validation and
                country_iso is not None and len(country_iso) > 2):
            raise ValueError("Invalid value for `country_iso`, length must be less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country_iso is not None and len(country_iso) < 0):
            raise ValueError("Invalid value for `country_iso`, length must be greater than or equal to `0`")  # noqa: E501

        self._country_iso = country_iso

    @property
    def original(self):
        """Gets the original of this ChannelAddressRequest.  # noqa: E501

        Optional. The address as a single string: use in case the address lines are entered  as single lines and later parsed into street, house number and house number addition.  # noqa: E501

        :return: The original of this ChannelAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this ChannelAddressRequest.

        Optional. The address as a single string: use in case the address lines are entered  as single lines and later parsed into street, house number and house number addition.  # noqa: E501

        :param original: The original of this ChannelAddressRequest.  # noqa: E501
        :type original: str
        """
        if (self.local_vars_configuration.client_side_validation and
                original is not None and len(original) > 256):
            raise ValueError("Invalid value for `original`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                original is not None and len(original) < 0):
            raise ValueError("Invalid value for `original`, length must be greater than or equal to `0`")  # noqa: E501

        self._original = original

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
        if not isinstance(other, ChannelAddressRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelAddressRequest):
            return True

        return self.to_dict() != other.to_dict()
