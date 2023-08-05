# coding: utf-8

"""
    Assetic Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

##from assetic.models.asset_sub_class_representation import AssetSubClassRepresentation  # noqa: F401,E501
##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501


class AssetClassRepresentation(object):
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
        'id': 'str',
        'name': 'str',
        'sub_types': 'list[AssetSubClassRepresentation]',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'sub_types': 'SubTypes',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, name=None, sub_types=None, links=None, embedded=None):  # noqa: E501
        """AssetClassRepresentation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._sub_types = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sub_types is not None:
            self.sub_types = sub_types
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this AssetClassRepresentation.  # noqa: E501


        :return: The id of this AssetClassRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetClassRepresentation.


        :param id: The id of this AssetClassRepresentation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetClassRepresentation.  # noqa: E501


        :return: The name of this AssetClassRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetClassRepresentation.


        :param name: The name of this AssetClassRepresentation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sub_types(self):
        """Gets the sub_types of this AssetClassRepresentation.  # noqa: E501


        :return: The sub_types of this AssetClassRepresentation.  # noqa: E501
        :rtype: list[AssetSubClassRepresentation]
        """
        return self._sub_types

    @sub_types.setter
    def sub_types(self, sub_types):
        """Sets the sub_types of this AssetClassRepresentation.


        :param sub_types: The sub_types of this AssetClassRepresentation.  # noqa: E501
        :type: list[AssetSubClassRepresentation]
        """

        self._sub_types = sub_types

    @property
    def links(self):
        """Gets the links of this AssetClassRepresentation.  # noqa: E501


        :return: The links of this AssetClassRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssetClassRepresentation.


        :param links: The links of this AssetClassRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this AssetClassRepresentation.  # noqa: E501


        :return: The embedded of this AssetClassRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this AssetClassRepresentation.


        :param embedded: The embedded of this AssetClassRepresentation.  # noqa: E501
        :type: list[EmbeddedResource]
        """

        self._embedded = embedded

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
        if issubclass(AssetClassRepresentation, dict):
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
        if not isinstance(other, AssetClassRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
