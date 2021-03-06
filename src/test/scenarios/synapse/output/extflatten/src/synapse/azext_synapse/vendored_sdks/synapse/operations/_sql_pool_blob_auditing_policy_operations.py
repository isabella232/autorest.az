# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SQLPoolBlobAuditingPolicyOperations(object):
    """SQLPoolBlobAuditingPolicyOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~synapse_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        sql_pool_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SQLPoolBlobAuditingPolicy"
        """Get a SQL pool's blob auditing policy.

        Get a SQL pool's blob auditing policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name.
        :type sql_pool_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SQLPoolBlobAuditingPolicy, or the result of cls(response)
        :rtype: ~synapse_management_client.models.SQLPoolBlobAuditingPolicy
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SQLPoolBlobAuditingPolicy"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        blob_auditing_policy_name = "default"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'sqlPoolName': self._serialize.url("sql_pool_name", sql_pool_name, 'str'),
            'blobAuditingPolicyName': self._serialize.url("blob_auditing_policy_name", blob_auditing_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SQLPoolBlobAuditingPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}/auditingSettings/{blobAuditingPolicyName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        sql_pool_name,  # type: str
        state=None,  # type: Optional[Union[str, "models.BlobAuditingPolicyState"]]
        storage_endpoint=None,  # type: Optional[str]
        storage_account_access_key=None,  # type: Optional[str]
        retention_days=None,  # type: Optional[int]
        audit_actions_and_groups=None,  # type: Optional[List[str]]
        storage_account_subscription_id=None,  # type: Optional[str]
        is_storage_secondary_key_in_use=None,  # type: Optional[bool]
        is_azure_monitor_target_enabled=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SQLPoolBlobAuditingPolicy"
        """Creates or updates a SQL pool's blob auditing policy.

        Creates or updates a SQL pool's blob auditing policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name.
        :type sql_pool_name: str
        :param state: Specifies the state of the policy. If state is Enabled, storageEndpoint or
         isAzureMonitorTargetEnabled are required.
        :type state: str or ~synapse_management_client.models.BlobAuditingPolicyState
        :param storage_endpoint: Specifies the blob storage endpoint (e.g.
         https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint is required.
        :type storage_endpoint: str
        :param storage_account_access_key: Specifies the identifier key of the auditing storage
         account. If state is Enabled and storageEndpoint is specified, storageAccountAccessKey is
         required.
        :type storage_account_access_key: str
        :param retention_days: Specifies the number of days to keep in the audit logs in the storage
         account.
        :type retention_days: int
        :param audit_actions_and_groups: Specifies the Actions-Groups and Actions to audit.

         The recommended set of action groups to use is the following combination - this will audit all
         the queries and stored procedures executed against the database, as well as successful and
         failed logins:

         BATCH_COMPLETED_GROUP,
         SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,
         FAILED_DATABASE_AUTHENTICATION_GROUP.

         This above combination is also the set that is configured by default when enabling auditing
         from the Azure portal.

         The supported action groups to audit are (note: choose only specific groups that cover your
         auditing needs. Using unnecessary groups could lead to very large quantities of audit records):

         APPLICATION_ROLE_CHANGE_PASSWORD_GROUP
         BACKUP_RESTORE_GROUP
         DATABASE_LOGOUT_GROUP
         DATABASE_OBJECT_CHANGE_GROUP
         DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP
         DATABASE_OBJECT_PERMISSION_CHANGE_GROUP
         DATABASE_OPERATION_GROUP
         DATABASE_PERMISSION_CHANGE_GROUP
         DATABASE_PRINCIPAL_CHANGE_GROUP
         DATABASE_PRINCIPAL_IMPERSONATION_GROUP
         DATABASE_ROLE_MEMBER_CHANGE_GROUP
         FAILED_DATABASE_AUTHENTICATION_GROUP
         SCHEMA_OBJECT_ACCESS_GROUP
         SCHEMA_OBJECT_CHANGE_GROUP
         SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP
         SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP
         SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP
         USER_CHANGE_PASSWORD_GROUP
         BATCH_STARTED_GROUP
         BATCH_COMPLETED_GROUP

         These are groups that cover all sql statements and stored procedures executed against the
         database, and should not be used in combination with other groups as this will result in
         duplicate audit logs.

         For more information, see `Database-Level Audit Action Groups <https://docs.microsoft.com/en-
         us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-
         actions#database-level-audit-action-groups>`_.

         For Database auditing policy, specific Actions can also be specified (note that Actions cannot
         be specified for Server auditing policy). The supported actions to audit are:
         SELECT
         UPDATE
         INSERT
         DELETE
         EXECUTE
         RECEIVE
         REFERENCES

         The general form for defining an action to be audited is:
         {action} ON {object} BY {principal}

         Note that :code:`<object>` in the above format can refer to an object like a table, view, or
         stored procedure, or an entire database or schema. For the latter cases, the forms
         DATABASE::{db_name} and SCHEMA::{schema_name} are used, respectively.

         For example:
         SELECT on dbo.myTable by public
         SELECT on DATABASE::myDatabase by public
         SELECT on SCHEMA::mySchema by public

         For more information, see `Database-Level Audit Actions <https://docs.microsoft.com/en-
         us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-
         actions#database-level-audit-actions>`_.
        :type audit_actions_and_groups: list[str]
        :param storage_account_subscription_id: Specifies the blob storage subscription Id.
        :type storage_account_subscription_id: str
        :param is_storage_secondary_key_in_use: Specifies whether storageAccountAccessKey value is the
         storage's secondary key.
        :type is_storage_secondary_key_in_use: bool
        :param is_azure_monitor_target_enabled: Specifies whether audit events are sent to Azure
         Monitor.
         In order to send the events to Azure Monitor, specify 'state' as 'Enabled' and
         'isAzureMonitorTargetEnabled' as true.

         When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents'
         diagnostic logs category on the database should be also created.
         Note that for server level audit you should use the 'master' database as {databaseName}.

         Diagnostic Settings URI format:
         PUT
         https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-
         version=2017-05-01-preview

         For more information, see `Diagnostic Settings REST API
         <https://go.microsoft.com/fwlink/?linkid=2033207>`_
         or `Diagnostic Settings PowerShell <https://go.microsoft.com/fwlink/?linkid=2033043>`_.
        :type is_azure_monitor_target_enabled: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SQLPoolBlobAuditingPolicy, or the result of cls(response)
        :rtype: ~synapse_management_client.models.SQLPoolBlobAuditingPolicy
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SQLPoolBlobAuditingPolicy"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        parameters = models.SQLPoolBlobAuditingPolicy(state=state, storage_endpoint=storage_endpoint, storage_account_access_key=storage_account_access_key, retention_days=retention_days, audit_actions_and_groups=audit_actions_and_groups, storage_account_subscription_id=storage_account_subscription_id, is_storage_secondary_key_in_use=is_storage_secondary_key_in_use, is_azure_monitor_target_enabled=is_azure_monitor_target_enabled)
        api_version = "2019-06-01-preview"
        blob_auditing_policy_name = "default"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'sqlPoolName': self._serialize.url("sql_pool_name", sql_pool_name, 'str'),
            'blobAuditingPolicyName': self._serialize.url("blob_auditing_policy_name", blob_auditing_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'SQLPoolBlobAuditingPolicy')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('SQLPoolBlobAuditingPolicy', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SQLPoolBlobAuditingPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}/auditingSettings/{blobAuditingPolicyName}'}  # type: ignore
