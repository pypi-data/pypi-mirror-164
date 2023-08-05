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


class ServiceCriteriaScoreRepresentation(object):
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
        'id': 'int',
        'assessment_date': 'datetime',
        'score': 'float',
        'created_date': 'datetime',
        'is_most_recent_score': 'bool',
        'asset_category': 'str',
        'asset_category_id': 'str',
        'asset_id': 'str',
        'component_id': 'str',
        'assessed_by_resource_id': 'str',
        'assessed_by_resource_name': 'str',
        'service_criteria_type_id': 'str',
        'service_criteria_type_label': 'str',
        'service_criteria_type_group': 'str',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'assessment_date': 'AssessmentDate',
        'score': 'Score',
        'created_date': 'CreatedDate',
        'is_most_recent_score': 'IsMostRecentScore',
        'asset_category': 'AssetCategory',
        'asset_category_id': 'AssetCategoryId',
        'asset_id': 'AssetId',
        'component_id': 'ComponentId',
        'assessed_by_resource_id': 'AssessedByResourceId',
        'assessed_by_resource_name': 'AssessedByResourceName',
        'service_criteria_type_id': 'ServiceCriteriaTypeId',
        'service_criteria_type_label': 'ServiceCriteriaTypeLabel',
        'service_criteria_type_group': 'ServiceCriteriaTypeGroup',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, assessment_date=None, score=None, created_date=None, is_most_recent_score=None, asset_category=None, asset_category_id=None, asset_id=None, component_id=None, assessed_by_resource_id=None, assessed_by_resource_name=None, service_criteria_type_id=None, service_criteria_type_label=None, service_criteria_type_group=None, links=None, embedded=None):  # noqa: E501
        """ServiceCriteriaScoreRepresentation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._assessment_date = None
        self._score = None
        self._created_date = None
        self._is_most_recent_score = None
        self._asset_category = None
        self._asset_category_id = None
        self._asset_id = None
        self._component_id = None
        self._assessed_by_resource_id = None
        self._assessed_by_resource_name = None
        self._service_criteria_type_id = None
        self._service_criteria_type_label = None
        self._service_criteria_type_group = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if assessment_date is not None:
            self.assessment_date = assessment_date
        if score is not None:
            self.score = score
        if created_date is not None:
            self.created_date = created_date
        if is_most_recent_score is not None:
            self.is_most_recent_score = is_most_recent_score
        if asset_category is not None:
            self.asset_category = asset_category
        if asset_category_id is not None:
            self.asset_category_id = asset_category_id
        if asset_id is not None:
            self.asset_id = asset_id
        if component_id is not None:
            self.component_id = component_id
        if assessed_by_resource_id is not None:
            self.assessed_by_resource_id = assessed_by_resource_id
        if assessed_by_resource_name is not None:
            self.assessed_by_resource_name = assessed_by_resource_name
        if service_criteria_type_id is not None:
            self.service_criteria_type_id = service_criteria_type_id
        if service_criteria_type_label is not None:
            self.service_criteria_type_label = service_criteria_type_label
        if service_criteria_type_group is not None:
            self.service_criteria_type_group = service_criteria_type_group
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceCriteriaScoreRepresentation.


        :param id: The id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def assessment_date(self):
        """Gets the assessment_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The assessment_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._assessment_date

    @assessment_date.setter
    def assessment_date(self, assessment_date):
        """Sets the assessment_date of this ServiceCriteriaScoreRepresentation.


        :param assessment_date: The assessment_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: datetime
        """

        self._assessment_date = assessment_date

    @property
    def score(self):
        """Gets the score of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The score of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ServiceCriteriaScoreRepresentation.


        :param score: The score of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def created_date(self):
        """Gets the created_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The created_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ServiceCriteriaScoreRepresentation.


        :param created_date: The created_date of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def is_most_recent_score(self):
        """Gets the is_most_recent_score of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The is_most_recent_score of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: bool
        """
        return self._is_most_recent_score

    @is_most_recent_score.setter
    def is_most_recent_score(self, is_most_recent_score):
        """Sets the is_most_recent_score of this ServiceCriteriaScoreRepresentation.


        :param is_most_recent_score: The is_most_recent_score of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: bool
        """

        self._is_most_recent_score = is_most_recent_score

    @property
    def asset_category(self):
        """Gets the asset_category of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The asset_category of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_category

    @asset_category.setter
    def asset_category(self, asset_category):
        """Sets the asset_category of this ServiceCriteriaScoreRepresentation.


        :param asset_category: The asset_category of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_category = asset_category

    @property
    def asset_category_id(self):
        """Gets the asset_category_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The asset_category_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_category_id

    @asset_category_id.setter
    def asset_category_id(self, asset_category_id):
        """Sets the asset_category_id of this ServiceCriteriaScoreRepresentation.


        :param asset_category_id: The asset_category_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_category_id = asset_category_id

    @property
    def asset_id(self):
        """Gets the asset_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The asset_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ServiceCriteriaScoreRepresentation.


        :param asset_id: The asset_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def component_id(self):
        """Gets the component_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The component_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ServiceCriteriaScoreRepresentation.


        :param component_id: The component_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

    @property
    def assessed_by_resource_id(self):
        """Gets the assessed_by_resource_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The assessed_by_resource_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._assessed_by_resource_id

    @assessed_by_resource_id.setter
    def assessed_by_resource_id(self, assessed_by_resource_id):
        """Sets the assessed_by_resource_id of this ServiceCriteriaScoreRepresentation.


        :param assessed_by_resource_id: The assessed_by_resource_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._assessed_by_resource_id = assessed_by_resource_id

    @property
    def assessed_by_resource_name(self):
        """Gets the assessed_by_resource_name of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The assessed_by_resource_name of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._assessed_by_resource_name

    @assessed_by_resource_name.setter
    def assessed_by_resource_name(self, assessed_by_resource_name):
        """Sets the assessed_by_resource_name of this ServiceCriteriaScoreRepresentation.


        :param assessed_by_resource_name: The assessed_by_resource_name of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._assessed_by_resource_name = assessed_by_resource_name

    @property
    def service_criteria_type_id(self):
        """Gets the service_criteria_type_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The service_criteria_type_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._service_criteria_type_id

    @service_criteria_type_id.setter
    def service_criteria_type_id(self, service_criteria_type_id):
        """Sets the service_criteria_type_id of this ServiceCriteriaScoreRepresentation.


        :param service_criteria_type_id: The service_criteria_type_id of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._service_criteria_type_id = service_criteria_type_id

    @property
    def service_criteria_type_label(self):
        """Gets the service_criteria_type_label of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The service_criteria_type_label of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._service_criteria_type_label

    @service_criteria_type_label.setter
    def service_criteria_type_label(self, service_criteria_type_label):
        """Sets the service_criteria_type_label of this ServiceCriteriaScoreRepresentation.


        :param service_criteria_type_label: The service_criteria_type_label of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """

        self._service_criteria_type_label = service_criteria_type_label

    @property
    def service_criteria_type_group(self):
        """Gets the service_criteria_type_group of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The service_criteria_type_group of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._service_criteria_type_group

    @service_criteria_type_group.setter
    def service_criteria_type_group(self, service_criteria_type_group):
        """Sets the service_criteria_type_group of this ServiceCriteriaScoreRepresentation.


        :param service_criteria_type_group: The service_criteria_type_group of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: str
        """
        allowed_values = ["Condition", "Risk", "Holistic", "Meter", "Sustainability"]  # noqa: E501
        if "None" in allowed_values:
            allowed_values.append(None)
        if service_criteria_type_group not in allowed_values:
            # Could be an integer enum returned by API
            try:
                int_type = int(service_criteria_type_group)
            except ValueError:
                raise ValueError(
                    "Invalid value for `service_criteria_type_group` ({0}), must be one of {1}"  # noqa: E501
                    .format(service_criteria_type_group, allowed_values)
                )

        self._service_criteria_type_group = service_criteria_type_group

    @property
    def links(self):
        """Gets the links of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The links of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ServiceCriteriaScoreRepresentation.


        :param links: The links of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this ServiceCriteriaScoreRepresentation.  # noqa: E501


        :return: The embedded of this ServiceCriteriaScoreRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this ServiceCriteriaScoreRepresentation.


        :param embedded: The embedded of this ServiceCriteriaScoreRepresentation.  # noqa: E501
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
        if issubclass(ServiceCriteriaScoreRepresentation, dict):
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
        if not isinstance(other, ServiceCriteriaScoreRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
