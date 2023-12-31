# coding: utf-8

"""
    ILS API Documentation

    Neoception® Intralogistics Suite is a collection of modules for automation in the context of manufacturing.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@neoception.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PutToLightOperationBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'carrier_id': 'str'
    }

    attribute_map = {
        'carrier_id': 'carrierId'
    }

    def __init__(self, carrier_id=None):  # noqa: E501
        """PutToLightOperationBody - a model defined in Swagger"""  # noqa: E501
        self._carrier_id = None
        self.discriminator = None
        self.carrier_id = carrier_id

    @property
    def carrier_id(self):
        """Gets the carrier_id of this PutToLightOperationBody.  # noqa: E501

        The Carrier's id.  # noqa: E501

        :return: The carrier_id of this PutToLightOperationBody.  # noqa: E501
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this PutToLightOperationBody.

        The Carrier's id.  # noqa: E501

        :param carrier_id: The carrier_id of this PutToLightOperationBody.  # noqa: E501
        :type: str
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501

        self._carrier_id = carrier_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PutToLightOperationBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutToLightOperationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
