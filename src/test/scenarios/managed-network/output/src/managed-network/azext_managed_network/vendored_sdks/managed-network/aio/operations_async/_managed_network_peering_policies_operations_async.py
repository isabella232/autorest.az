# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ManagedNetworkPeeringPoliciesOperations:
    """ManagedNetworkPeeringPoliciesOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~managed_network_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        managed_network_name: str,
        managed_network_peering_policy_name: str,
        **kwargs
    ) -> "models.ManagedNetworkPeeringPolicy":
        """The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param managed_network_name: The name of the Managed Network.
        :type managed_network_name: str
        :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
        :type managed_network_peering_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedNetworkPeeringPolicy or the result of cls(response)
        :rtype: ~managed_network_management_client.models.ManagedNetworkPeeringPolicy
        :raises: ~managed_network_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.ManagedNetworkPeeringPolicy"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'managedNetworkName': self._serialize.url("managed_network_name", managed_network_name, 'str'),
            'managedNetworkPeeringPolicyName': self._serialize.url("managed_network_peering_policy_name", managed_network_peering_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ManagedNetworkPeeringPolicy', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies/{managedNetworkPeeringPolicyName}'}

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        managed_network_name: str,
        managed_network_peering_policy_name: str,
        type: Union[str, "models.Type"],
        location: Optional[str] = None,
        id: Optional[str] = None,
        spokes: Optional[List["ResourceId"]] = None,
        mesh: Optional[List["ResourceId"]] = None,
        **kwargs
    ) -> "models.ManagedNetworkPeeringPolicy":
        cls: ClsType["models.ManagedNetworkPeeringPolicy"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        managed_network_policy = models.ManagedNetworkPeeringPolicy(location=location, type=type, id=id, spokes=spokes, mesh=mesh)

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'managedNetworkName': self._serialize.url("managed_network_name", managed_network_name, 'str'),
            'managedNetworkPeeringPolicyName': self._serialize.url("managed_network_peering_policy_name", managed_network_peering_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(managed_network_policy, 'ManagedNetworkPeeringPolicy')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ManagedNetworkPeeringPolicy', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ManagedNetworkPeeringPolicy', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies/{managedNetworkPeeringPolicyName}'}

    async def create_or_update(
        self,
        resource_group_name: str,
        managed_network_name: str,
        managed_network_peering_policy_name: str,
        type: Union[str, "models.Type"],
        location: Optional[str] = None,
        id: Optional[str] = None,
        spokes: Optional[List["ResourceId"]] = None,
        mesh: Optional[List["ResourceId"]] = None,
        **kwargs
    ) -> "models.ManagedNetworkPeeringPolicy":
        """The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param managed_network_name: The name of the Managed Network.
        :type managed_network_name: str
        :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
        :type managed_network_peering_policy_name: str
        :param type: Gets or sets the connectivity type of a network structure policy.
        :type type: str or ~managed_network_management_client.models.Type
        :param location: The geo-location where the resource lives.
        :type location: str
        :param id: Resource Id.
        :type id: str
        :param spokes: Gets or sets the spokes group IDs.
        :type spokes: list[~managed_network_management_client.models.ResourceId]
        :param mesh: Gets or sets the mesh group IDs.
        :type mesh: list[~managed_network_management_client.models.ResourceId]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns ManagedNetworkPeeringPolicy
        :rtype: ~azure.core.polling.LROPoller[~managed_network_management_client.models.ManagedNetworkPeeringPolicy]

        :raises ~managed_network_management_client.models.ErrorResponseException:
        """
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop('polling', True)
        cls: ClsType["models.ManagedNetworkPeeringPolicy"] = kwargs.pop('cls', None )
        raw_result = await self._create_or_update_initial(
            resource_group_name=resource_group_name,
            managed_network_name=managed_network_name,
            managed_network_peering_policy_name=managed_network_peering_policy_name,
            type=type,
            location=location,
            id=id,
            spokes=spokes,
            mesh=mesh,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('ManagedNetworkPeeringPolicy', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies/{managedNetworkPeeringPolicyName}'}

    async def _delete_initial(
        self,
        resource_group_name: str,
        managed_network_name: str,
        managed_network_peering_policy_name: str,
        **kwargs
    ) -> None:
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'managedNetworkName': self._serialize.url("managed_network_name", managed_network_name, 'str'),
            'managedNetworkPeeringPolicyName': self._serialize.url("managed_network_peering_policy_name", managed_network_peering_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies/{managedNetworkPeeringPolicyName}'}

    async def delete(
        self,
        resource_group_name: str,
        managed_network_name: str,
        managed_network_peering_policy_name: str,
        **kwargs
    ) -> None:
        """The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param managed_network_name: The name of the Managed Network.
        :type managed_network_name: str
        :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
        :type managed_network_peering_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~managed_network_management_client.models.ErrorResponseException:
        """
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop('polling', True)
        cls: ClsType[None] = kwargs.pop('cls', None )
        raw_result = await self._delete_initial(
            resource_group_name=resource_group_name,
            managed_network_name=managed_network_name,
            managed_network_peering_policy_name=managed_network_peering_policy_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies/{managedNetworkPeeringPolicyName}'}

    def list_by_managed_network(
        self,
        resource_group_name: str,
        managed_network_name: str,
        top: Optional[int] = None,
        skiptoken: Optional[str] = None,
        **kwargs
    ) -> "models.ManagedNetworkPeeringPolicyListResult":
        """The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param managed_network_name: The name of the Managed Network.
        :type managed_network_name: str
        :param top: May be used to limit the number of results in a page for list queries.
        :type top: int
        :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skiptoken parameter that specifies a starting point to use for subsequent calls.
        :type skiptoken: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedNetworkPeeringPolicyListResult or the result of cls(response)
        :rtype: ~managed_network_management_client.models.ManagedNetworkPeeringPolicyListResult
        :raises: ~managed_network_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.ManagedNetworkPeeringPolicyListResult"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_managed_network.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'managedNetworkName': self._serialize.url("managed_network_name", managed_network_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            if top is not None:
                query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=20, minimum=1)
            if skiptoken is not None:
                query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ManagedNetworkPeeringPolicyListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.ErrorResponseException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_managed_network.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetwork/managedNetworks/{managedNetworkName}/managedNetworkPeeringPolicies'}
