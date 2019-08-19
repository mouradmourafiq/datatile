#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon sdk

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.14.4
    Contact: contact@polyaxon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Experiment(object):
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
        'uuid': 'str',
        'unique_name': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'deleted': 'bool',
        'user': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'started_at': 'str',
        'finished_at': 'str',
        'project': 'str',
        'is_managed': 'str',
        'spec': 'str',
        'backend': 'str',
        'framework': 'str',
        'last_status': 'str',
        'code_reference': 'str',
        'resources': 'dict(str, str)',
        'readme': 'str',
        'bookmarked': 'bool',
        'params': 'dict(str, str)',
        'run_env': 'dict(str, str)',
        'build_job': 'str',
        'data_refs': 'dict(str, str)',
        'artifact_refs': 'dict(str, str)',
        'original': 'str',
        'cloning_strategy': 'str',
        'experiment_group': 'str',
        'num_jobs': 'int',
        'has_tensorboard': 'bool',
        'last_metric': 'dict(str, float)'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'unique_name': 'unique_name',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'deleted': 'deleted',
        'user': 'user',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'project': 'project',
        'is_managed': 'is_managed',
        'spec': 'spec',
        'backend': 'backend',
        'framework': 'framework',
        'last_status': 'last_status',
        'code_reference': 'code_reference',
        'resources': 'resources',
        'readme': 'readme',
        'bookmarked': 'bookmarked',
        'params': 'params',
        'run_env': 'run_env',
        'build_job': 'build_job',
        'data_refs': 'data_refs',
        'artifact_refs': 'artifact_refs',
        'original': 'original',
        'cloning_strategy': 'cloning_strategy',
        'experiment_group': 'experiment_group',
        'num_jobs': 'num_jobs',
        'has_tensorboard': 'has_tensorboard',
        'last_metric': 'last_metric'
    }

    def __init__(self, id=None, uuid=None, unique_name=None, name=None, description=None, tags=None, deleted=None, user=None, created_at=None, updated_at=None, started_at=None, finished_at=None, project=None, is_managed=None, spec=None, backend=None, framework=None, last_status=None, code_reference=None, resources=None, readme=None, bookmarked=None, params=None, run_env=None, build_job=None, data_refs=None, artifact_refs=None, original=None, cloning_strategy=None, experiment_group=None, num_jobs=None, has_tensorboard=None, last_metric=None):  # noqa: E501
        """V1Experiment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._uuid = None
        self._unique_name = None
        self._name = None
        self._description = None
        self._tags = None
        self._deleted = None
        self._user = None
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._finished_at = None
        self._project = None
        self._is_managed = None
        self._spec = None
        self._backend = None
        self._framework = None
        self._last_status = None
        self._code_reference = None
        self._resources = None
        self._readme = None
        self._bookmarked = None
        self._params = None
        self._run_env = None
        self._build_job = None
        self._data_refs = None
        self._artifact_refs = None
        self._original = None
        self._cloning_strategy = None
        self._experiment_group = None
        self._num_jobs = None
        self._has_tensorboard = None
        self._last_metric = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        if unique_name is not None:
            self.unique_name = unique_name
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if deleted is not None:
            self.deleted = deleted
        if user is not None:
            self.user = user
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if project is not None:
            self.project = project
        if is_managed is not None:
            self.is_managed = is_managed
        if spec is not None:
            self.spec = spec
        if backend is not None:
            self.backend = backend
        if framework is not None:
            self.framework = framework
        if last_status is not None:
            self.last_status = last_status
        if code_reference is not None:
            self.code_reference = code_reference
        if resources is not None:
            self.resources = resources
        if readme is not None:
            self.readme = readme
        if bookmarked is not None:
            self.bookmarked = bookmarked
        if params is not None:
            self.params = params
        if run_env is not None:
            self.run_env = run_env
        if build_job is not None:
            self.build_job = build_job
        if data_refs is not None:
            self.data_refs = data_refs
        if artifact_refs is not None:
            self.artifact_refs = artifact_refs
        if original is not None:
            self.original = original
        if cloning_strategy is not None:
            self.cloning_strategy = cloning_strategy
        if experiment_group is not None:
            self.experiment_group = experiment_group
        if num_jobs is not None:
            self.num_jobs = num_jobs
        if has_tensorboard is not None:
            self.has_tensorboard = has_tensorboard
        if last_metric is not None:
            self.last_metric = last_metric

    @property
    def id(self):
        """Gets the id of this V1Experiment.  # noqa: E501


        :return: The id of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1Experiment.


        :param id: The id of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this V1Experiment.  # noqa: E501


        :return: The uuid of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1Experiment.


        :param uuid: The uuid of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def unique_name(self):
        """Gets the unique_name of this V1Experiment.  # noqa: E501


        :return: The unique_name of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this V1Experiment.


        :param unique_name: The unique_name of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._unique_name = unique_name

    @property
    def name(self):
        """Gets the name of this V1Experiment.  # noqa: E501


        :return: The name of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Experiment.


        :param name: The name of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1Experiment.  # noqa: E501


        :return: The description of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1Experiment.


        :param description: The description of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this V1Experiment.  # noqa: E501


        :return: The tags of this V1Experiment.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1Experiment.


        :param tags: The tags of this V1Experiment.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def deleted(self):
        """Gets the deleted of this V1Experiment.  # noqa: E501


        :return: The deleted of this V1Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this V1Experiment.


        :param deleted: The deleted of this V1Experiment.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def user(self):
        """Gets the user of this V1Experiment.  # noqa: E501


        :return: The user of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1Experiment.


        :param user: The user of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def created_at(self):
        """Gets the created_at of this V1Experiment.  # noqa: E501


        :return: The created_at of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1Experiment.


        :param created_at: The created_at of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this V1Experiment.  # noqa: E501


        :return: The updated_at of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V1Experiment.


        :param updated_at: The updated_at of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def started_at(self):
        """Gets the started_at of this V1Experiment.  # noqa: E501


        :return: The started_at of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1Experiment.


        :param started_at: The started_at of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this V1Experiment.  # noqa: E501


        :return: The finished_at of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1Experiment.


        :param finished_at: The finished_at of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def project(self):
        """Gets the project of this V1Experiment.  # noqa: E501


        :return: The project of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1Experiment.


        :param project: The project of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def is_managed(self):
        """Gets the is_managed of this V1Experiment.  # noqa: E501


        :return: The is_managed of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this V1Experiment.


        :param is_managed: The is_managed of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._is_managed = is_managed

    @property
    def spec(self):
        """Gets the spec of this V1Experiment.  # noqa: E501


        :return: The spec of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1Experiment.


        :param spec: The spec of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._spec = spec

    @property
    def backend(self):
        """Gets the backend of this V1Experiment.  # noqa: E501


        :return: The backend of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this V1Experiment.


        :param backend: The backend of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._backend = backend

    @property
    def framework(self):
        """Gets the framework of this V1Experiment.  # noqa: E501


        :return: The framework of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this V1Experiment.


        :param framework: The framework of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._framework = framework

    @property
    def last_status(self):
        """Gets the last_status of this V1Experiment.  # noqa: E501


        :return: The last_status of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        """Sets the last_status of this V1Experiment.


        :param last_status: The last_status of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._last_status = last_status

    @property
    def code_reference(self):
        """Gets the code_reference of this V1Experiment.  # noqa: E501


        :return: The code_reference of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._code_reference

    @code_reference.setter
    def code_reference(self, code_reference):
        """Sets the code_reference of this V1Experiment.


        :param code_reference: The code_reference of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._code_reference = code_reference

    @property
    def resources(self):
        """Gets the resources of this V1Experiment.  # noqa: E501


        :return: The resources of this V1Experiment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1Experiment.


        :param resources: The resources of this V1Experiment.  # noqa: E501
        :type: dict(str, str)
        """

        self._resources = resources

    @property
    def readme(self):
        """Gets the readme of this V1Experiment.  # noqa: E501


        :return: The readme of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this V1Experiment.


        :param readme: The readme of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._readme = readme

    @property
    def bookmarked(self):
        """Gets the bookmarked of this V1Experiment.  # noqa: E501


        :return: The bookmarked of this V1Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._bookmarked

    @bookmarked.setter
    def bookmarked(self, bookmarked):
        """Sets the bookmarked of this V1Experiment.


        :param bookmarked: The bookmarked of this V1Experiment.  # noqa: E501
        :type: bool
        """

        self._bookmarked = bookmarked

    @property
    def params(self):
        """Gets the params of this V1Experiment.  # noqa: E501


        :return: The params of this V1Experiment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this V1Experiment.


        :param params: The params of this V1Experiment.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

    @property
    def run_env(self):
        """Gets the run_env of this V1Experiment.  # noqa: E501


        :return: The run_env of this V1Experiment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._run_env

    @run_env.setter
    def run_env(self, run_env):
        """Sets the run_env of this V1Experiment.


        :param run_env: The run_env of this V1Experiment.  # noqa: E501
        :type: dict(str, str)
        """

        self._run_env = run_env

    @property
    def build_job(self):
        """Gets the build_job of this V1Experiment.  # noqa: E501


        :return: The build_job of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._build_job

    @build_job.setter
    def build_job(self, build_job):
        """Sets the build_job of this V1Experiment.


        :param build_job: The build_job of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._build_job = build_job

    @property
    def data_refs(self):
        """Gets the data_refs of this V1Experiment.  # noqa: E501


        :return: The data_refs of this V1Experiment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data_refs

    @data_refs.setter
    def data_refs(self, data_refs):
        """Sets the data_refs of this V1Experiment.


        :param data_refs: The data_refs of this V1Experiment.  # noqa: E501
        :type: dict(str, str)
        """

        self._data_refs = data_refs

    @property
    def artifact_refs(self):
        """Gets the artifact_refs of this V1Experiment.  # noqa: E501


        :return: The artifact_refs of this V1Experiment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._artifact_refs

    @artifact_refs.setter
    def artifact_refs(self, artifact_refs):
        """Sets the artifact_refs of this V1Experiment.


        :param artifact_refs: The artifact_refs of this V1Experiment.  # noqa: E501
        :type: dict(str, str)
        """

        self._artifact_refs = artifact_refs

    @property
    def original(self):
        """Gets the original of this V1Experiment.  # noqa: E501


        :return: The original of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this V1Experiment.


        :param original: The original of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._original = original

    @property
    def cloning_strategy(self):
        """Gets the cloning_strategy of this V1Experiment.  # noqa: E501


        :return: The cloning_strategy of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._cloning_strategy

    @cloning_strategy.setter
    def cloning_strategy(self, cloning_strategy):
        """Sets the cloning_strategy of this V1Experiment.


        :param cloning_strategy: The cloning_strategy of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._cloning_strategy = cloning_strategy

    @property
    def experiment_group(self):
        """Gets the experiment_group of this V1Experiment.  # noqa: E501


        :return: The experiment_group of this V1Experiment.  # noqa: E501
        :rtype: str
        """
        return self._experiment_group

    @experiment_group.setter
    def experiment_group(self, experiment_group):
        """Sets the experiment_group of this V1Experiment.


        :param experiment_group: The experiment_group of this V1Experiment.  # noqa: E501
        :type: str
        """

        self._experiment_group = experiment_group

    @property
    def num_jobs(self):
        """Gets the num_jobs of this V1Experiment.  # noqa: E501


        :return: The num_jobs of this V1Experiment.  # noqa: E501
        :rtype: int
        """
        return self._num_jobs

    @num_jobs.setter
    def num_jobs(self, num_jobs):
        """Sets the num_jobs of this V1Experiment.


        :param num_jobs: The num_jobs of this V1Experiment.  # noqa: E501
        :type: int
        """

        self._num_jobs = num_jobs

    @property
    def has_tensorboard(self):
        """Gets the has_tensorboard of this V1Experiment.  # noqa: E501


        :return: The has_tensorboard of this V1Experiment.  # noqa: E501
        :rtype: bool
        """
        return self._has_tensorboard

    @has_tensorboard.setter
    def has_tensorboard(self, has_tensorboard):
        """Sets the has_tensorboard of this V1Experiment.


        :param has_tensorboard: The has_tensorboard of this V1Experiment.  # noqa: E501
        :type: bool
        """

        self._has_tensorboard = has_tensorboard

    @property
    def last_metric(self):
        """Gets the last_metric of this V1Experiment.  # noqa: E501


        :return: The last_metric of this V1Experiment.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._last_metric

    @last_metric.setter
    def last_metric(self, last_metric):
        """Sets the last_metric of this V1Experiment.


        :param last_metric: The last_metric of this V1Experiment.  # noqa: E501
        :type: dict(str, float)
        """

        self._last_metric = last_metric

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
        if issubclass(V1Experiment, dict):
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
        if not isinstance(other, V1Experiment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
