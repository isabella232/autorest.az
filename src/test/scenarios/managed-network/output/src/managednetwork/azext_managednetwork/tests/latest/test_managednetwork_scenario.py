# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: ManagedNetworksPut
@try_manual
def step_managednetworksput(test, rg):
    test.cmd('az managednetwork mn create '
             '--location "eastus" '
             '--properties "{{\\"scope\\":{{\\"managementGroups\\":[{{\\"id\\":\\"/providers/Microsoft.Management/manag'
             'ementGroups/20000000-0001-0000-0000-000000000000\\"}},{{\\"id\\":\\"/providers/Microsoft.Management/manag'
             'ementGroups/20000000-0002-0000-0000-000000000000\\"}}],\\"subnets\\":[{{\\"id\\":\\"/subscriptions/{subsc'
             'ription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}},{{'
             '\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetwo'
             'rks/{vn}/subnets/default\\"}}],\\"subscriptions\\":[{{\\"id\\":\\"subscriptionA\\"}},{{\\"id\\":\\"subscr'
             'iptionB\\"}}],\\"virtualNetworks\\":[{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/p'
             'roviders/Microsoft.Network/virtualNetworks/{vn_2}\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/res'
             'ourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn_3}\\"}}]}}}}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsPut
@try_manual
def step_managementnetworkgroupsput(test, rg):
    test.cmd('az managednetwork managed-network-group create '
             '--properties-management-groups "[]" '
             '--properties-subnets id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtua'
             'lNetworks/VnetA/subnets/subnetA" '
             '--properties-virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Netwo'
             'rk/virtualNetworks/VnetA" '
             '--properties-virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Netwo'
             'rk/virtualNetworks/VnetB" '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsPut
@try_manual
def step_scopeassignmentsput(test, rg):
    test.cmd('az managednetwork scope-assignment create '
             '--properties-assigned-managed-network "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Mic'
             'rosoft.ManagedNetwork/managedNetworks/{myManagedNetwork}" '
             '--scope "subscriptions/subscriptionC" '
             '--scope-assignment-name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesPut
@try_manual
def step_managednetworkpeeringpoliciesput(test, rg):
    test.cmd('az managednetwork managed-network-peering-policy create '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--properties "{{\\"type\\":\\"HubAndSpokeTopology\\",\\"hub\\":{{\\"id\\":\\"/subscriptions/{subscription'
             '_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn_4}\\"}},\\"spokes\\":[{{\\"id\\"'
             ':\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.ManagedNetwork/managedNetwor'
             'ks/{myManagedNetwork}/managedNetworkGroups/{myManagedNetworkGroup1}\\"}}]}}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksGet
@try_manual
def step_managednetworksget(test, rg):
    test.cmd('az managednetwork mn show '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksListByResourceGroup
@try_manual
def step_managednetworkslistbyresourcegroup(test, rg):
    test.cmd('az managednetwork mn list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksListBySubscription
@try_manual
def step_managednetworkslistbysubscription(test, rg):
    test.cmd('az managednetwork mn list',
             checks=[])


# EXAMPLE: ScopeAssignmentsGet
@try_manual
def step_scopeassignmentsget(test, rg):
    test.cmd('az managednetwork scope-assignment show '
             '--scope "subscriptions/subscriptionC" '
             '--scope-assignment-name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsList
@try_manual
def step_scopeassignmentslist(test, rg):
    test.cmd('az managednetwork scope-assignment list '
             '--scope "subscriptions/subscriptionC"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsGet
@try_manual
def step_managementnetworkgroupsget(test, rg):
    test.cmd('az managednetwork managed-network-group show '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksGroupsListByManagedNetwork
@try_manual
def step_managednetworksgroupslistbymanagednetwork(test, rg):
    test.cmd('az managednetwork managed-network-group list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesGet
@try_manual
def step_managednetworkpeeringpoliciesget(test, rg):
    test.cmd('az managednetwork managed-network-peering-policy show '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesListByManagedNetwork
@try_manual
def step_managednetworkpeeringpolicieslistbymanagednetwork(test, rg):
    test.cmd('az managednetwork managed-network-peering-policy list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesDelete
@try_manual
def step_managednetworkpeeringpoliciesdelete(test, rg):
    test.cmd('az managednetwork managed-network-peering-policy delete '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsDelete
@try_manual
def step_scopeassignmentsdelete(test, rg):
    test.cmd('az managednetwork scope-assignment delete '
             '--scope "subscriptions/subscriptionC" '
             '--scope-assignment-name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsDelete
@try_manual
def step_managementnetworkgroupsdelete(test, rg):
    test.cmd('az managednetwork managed-network-group delete '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksDelete
@try_manual
def step_managednetworksdelete(test, rg):
    test.cmd('az managednetwork mn delete '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


class ManagedNetworkManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestmanagednetwork_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanagednetwork_VnetC'[:7], key='vn', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanagednetwork_VnetA'[:7], key='vn_2', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanagednetwork_VnetB'[:7], key='vn_3', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanagednetwork_myHubVnet'[:7], key='vn_4', resource_group_key='rg')
    def test_managednetwork(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myManagedNetwork': self.create_random_name(prefix='clitestmanaged_networks'[:7], length=24),
            'subscriptionCAssignment': self.create_random_name(prefix='clitestscope_assignments'[:7], length=24),
            'myManagedNetworkGroup1': self.create_random_name(prefix='clitestmanaged_network_groups'[:7], length=24),
            'myHubAndSpoke': self.create_random_name(prefix='clitestmanaged_network_peering_policies'[:7], length=24),
        })

        setup(self, rg)
        step_managednetworksput(self, rg)
        step_managementnetworkgroupsput(self, rg)
        step_scopeassignmentsput(self, rg)
        step_managednetworkpeeringpoliciesput(self, rg)
        step_managednetworksget(self, rg)
        step_managednetworkslistbyresourcegroup(self, rg)
        step_managednetworkslistbysubscription(self, rg)
        step_scopeassignmentsget(self, rg)
        step_scopeassignmentslist(self, rg)
        step_managementnetworkgroupsget(self, rg)
        step_managednetworksgroupslistbymanagednetwork(self, rg)
        step_managednetworkpeeringpoliciesget(self, rg)
        step_managednetworkpeeringpolicieslistbymanagednetwork(self, rg)
        step_managednetworkpeeringpoliciesdelete(self, rg)
        step_scopeassignmentsdelete(self, rg)
        step_managementnetworkgroupsdelete(self, rg)
        step_managednetworksdelete(self, rg)
        cleanup(self, rg)
