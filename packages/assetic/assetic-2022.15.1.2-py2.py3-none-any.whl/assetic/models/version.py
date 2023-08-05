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


class Version(object):
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
        'major': 'int',
        'minor': 'int',
        'build': 'int',
        'revision': 'int',
        'major_revision': 'int',
        'minor_revision': 'int'
    }

    attribute_map = {
        'major': 'Major',
        'minor': 'Minor',
        'build': 'Build',
        'revision': 'Revision',
        'major_revision': 'MajorRevision',
        'minor_revision': 'MinorRevision'
    }

    def __init__(self, major=None, minor=None, build=None, revision=None, major_revision=None, minor_revision=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501

        self._major = None
        self._minor = None
        self._build = None
        self._revision = None
        self._major_revision = None
        self._minor_revision = None
        self.discriminator = None

        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if build is not None:
            self.build = build
        if revision is not None:
            self.revision = revision
        if major_revision is not None:
            self.major_revision = major_revision
        if minor_revision is not None:
            self.minor_revision = minor_revision

    @property
    def major(self):
        """Gets the major of this Version.  # noqa: E501


        :return: The major of this Version.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this Version.


        :param major: The major of this Version.  # noqa: E501
        :type: int
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this Version.  # noqa: E501


        :return: The minor of this Version.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this Version.


        :param minor: The minor of this Version.  # noqa: E501
        :type: int
        """

        self._minor = minor

    @property
    def build(self):
        """Gets the build of this Version.  # noqa: E501


        :return: The build of this Version.  # noqa: E501
        :rtype: int
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this Version.


        :param build: The build of this Version.  # noqa: E501
        :type: int
        """

        self._build = build

    @property
    def revision(self):
        """Gets the revision of this Version.  # noqa: E501


        :return: The revision of this Version.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Version.


        :param revision: The revision of this Version.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def major_revision(self):
        """Gets the major_revision of this Version.  # noqa: E501


        :return: The major_revision of this Version.  # noqa: E501
        :rtype: int
        """
        return self._major_revision

    @major_revision.setter
    def major_revision(self, major_revision):
        """Sets the major_revision of this Version.


        :param major_revision: The major_revision of this Version.  # noqa: E501
        :type: int
        """

        self._major_revision = major_revision

    @property
    def minor_revision(self):
        """Gets the minor_revision of this Version.  # noqa: E501


        :return: The minor_revision of this Version.  # noqa: E501
        :rtype: int
        """
        return self._minor_revision

    @minor_revision.setter
    def minor_revision(self, minor_revision):
        """Sets the minor_revision of this Version.


        :param minor_revision: The minor_revision of this Version.  # noqa: E501
        :type: int
        """

        self._minor_revision = minor_revision

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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
