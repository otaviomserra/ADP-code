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

class SetLightOperationBody(object):
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
        'side': 'str',
        'color': 'str',
        'duration': 'int',
        'blink': 'bool'
    }

    attribute_map = {
        'side': 'side',
        'color': 'color',
        'duration': 'duration',
        'blink': 'blink'
    }

    def __init__(self, side=None, color=None, duration=None, blink=None):  # noqa: E501
        """SetLightOperationBody - a model defined in Swagger"""  # noqa: E501
        self._side = None
        self._color = None
        self._duration = None
        self._blink = None
        self.discriminator = None
        if side is not None:
            self.side = side
        self.color = color
        if duration is not None:
            self.duration = duration
        self.blink = blink

    @property
    def side(self):
        """Gets the side of this SetLightOperationBody.  # noqa: E501

        The side of the Lanes.  # noqa: E501

        :return: The side of this SetLightOperationBody.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this SetLightOperationBody.

        The side of the Lanes.  # noqa: E501

        :param side: The side of this SetLightOperationBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "PRIMARY", "SECONDARY"]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def color(self):
        """Gets the color of this SetLightOperationBody.  # noqa: E501

        Select the color you which to see.  # noqa: E501

        :return: The color of this SetLightOperationBody.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this SetLightOperationBody.

        Select the color you which to see.  # noqa: E501

        :param color: The color of this SetLightOperationBody.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501
        allowed_values = ["BLACK", "RED", "GREEN", "BLUE", "YELLOW"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def duration(self):
        """Gets the duration of this SetLightOperationBody.  # noqa: E501

        Select the duration (in seconds) on wish the light will be on.  # noqa: E501

        :return: The duration of this SetLightOperationBody.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SetLightOperationBody.

        Select the duration (in seconds) on wish the light will be on.  # noqa: E501

        :param duration: The duration of this SetLightOperationBody.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def blink(self):
        """Gets the blink of this SetLightOperationBody.  # noqa: E501

        Select if the light should blink or be solid during the execution of the command  # noqa: E501

        :return: The blink of this SetLightOperationBody.  # noqa: E501
        :rtype: bool
        """
        return self._blink

    @blink.setter
    def blink(self, blink):
        """Sets the blink of this SetLightOperationBody.

        Select if the light should blink or be solid during the execution of the command  # noqa: E501

        :param blink: The blink of this SetLightOperationBody.  # noqa: E501
        :type: bool
        """
        if blink is None:
            raise ValueError("Invalid value for `blink`, must not be `None`")  # noqa: E501

        self._blink = blink

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
        if issubclass(SetLightOperationBody, dict):
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
        if not isinstance(other, SetLightOperationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
