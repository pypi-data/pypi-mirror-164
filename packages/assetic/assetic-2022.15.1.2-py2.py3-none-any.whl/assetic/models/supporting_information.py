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

##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501


class SupportingInformation(object):
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
        'description': 'str',
        'created_by': 'str',
        'created_by_display_name': 'str',
        'created_date_time': 'datetime',
        'system_added_time': 'datetime',
        'last_modified_time': 'datetime',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'description': 'Description',
        'created_by': 'CreatedBy',
        'created_by_display_name': 'CreatedByDisplayName',
        'created_date_time': 'CreatedDateTime',
        'system_added_time': 'SystemAddedTime',
        'last_modified_time': 'LastModifiedTime',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, description=None, created_by=None, created_by_display_name=None, created_date_time=None, system_added_time=None, last_modified_time=None, links=None, embedded=None):  # noqa: E501
        """SupportingInformation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._description = None
        self._created_by = None
        self._created_by_display_name = None
        self._created_date_time = None
        self._system_added_time = None
        self._last_modified_time = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if created_by_display_name is not None:
            self.created_by_display_name = created_by_display_name
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if system_added_time is not None:
            self.system_added_time = system_added_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this SupportingInformation.  # noqa: E501


        :return: The id of this SupportingInformation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupportingInformation.


        :param id: The id of this SupportingInformation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this SupportingInformation.  # noqa: E501


        :return: The description of this SupportingInformation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupportingInformation.


        :param description: The description of this SupportingInformation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_by(self):
        """Gets the created_by of this SupportingInformation.  # noqa: E501


        :return: The created_by of this SupportingInformation.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SupportingInformation.


        :param created_by: The created_by of this SupportingInformation.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_display_name(self):
        """Gets the created_by_display_name of this SupportingInformation.  # noqa: E501


        :return: The created_by_display_name of this SupportingInformation.  # noqa: E501
        :rtype: str
        """
        return self._created_by_display_name

    @created_by_display_name.setter
    def created_by_display_name(self, created_by_display_name):
        """Sets the created_by_display_name of this SupportingInformation.


        :param created_by_display_name: The created_by_display_name of this SupportingInformation.  # noqa: E501
        :type: str
        """

        self._created_by_display_name = created_by_display_name

    @property
    def created_date_time(self):
        """Gets the created_date_time of this SupportingInformation.  # noqa: E501


        :return: The created_date_time of this SupportingInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this SupportingInformation.


        :param created_date_time: The created_date_time of this SupportingInformation.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def system_added_time(self):
        """Gets the system_added_time of this SupportingInformation.  # noqa: E501


        :return: The system_added_time of this SupportingInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._system_added_time

    @system_added_time.setter
    def system_added_time(self, system_added_time):
        """Sets the system_added_time of this SupportingInformation.


        :param system_added_time: The system_added_time of this SupportingInformation.  # noqa: E501
        :type: datetime
        """

        self._system_added_time = system_added_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this SupportingInformation.  # noqa: E501


        :return: The last_modified_time of this SupportingInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this SupportingInformation.


        :param last_modified_time: The last_modified_time of this SupportingInformation.  # noqa: E501
        :type: datetime
        """

        self._last_modified_time = last_modified_time

    @property
    def links(self):
        """Gets the links of this SupportingInformation.  # noqa: E501


        :return: The links of this SupportingInformation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SupportingInformation.


        :param links: The links of this SupportingInformation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this SupportingInformation.  # noqa: E501


        :return: The embedded of this SupportingInformation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this SupportingInformation.


        :param embedded: The embedded of this SupportingInformation.  # noqa: E501
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
        if issubclass(SupportingInformation, dict):
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
        if not isinstance(other, SupportingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
