# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /ManagedNetworks/put/ManagedNetworksPut
@try_manual
def step_mn_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn create '
             '--location "eastus" '
             '--properties "{{\\"managementGroups\\":[{{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20'
             '000000-0001-0000-0000-000000000000\\"}},{{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20'
             '000000-0002-0000-0000-000000000000\\"}}],\\"subscriptions\\":[{{\\"id\\":\\"subscriptionA\\"}},{{\\"id\\"'
             ':\\"subscriptionB\\"}}],\\"virtualNetworks\\":[{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGro'
             'ups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn}\\"}},{{\\"id\\":\\"/subscriptions/{subscription'
             '_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn_2}\\"}}],\\"subnets\\":[{{\\"id'
             '\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{'
             'vn_3}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/M'
             'icrosoft.Network/virtualNetworks/{vn_3}/subnets/default\\"}}]}}" '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworks/get/ManagedNetworksGet
@try_manual
def step_mn_show_modify(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn show-modify '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworks/get/ManagedNetworksListByResourceGroup
@try_manual
def step_mn_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworks/get/ManagedNetworksListBySubscription
@try_manual
def step_mn_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn list '
             '-g ""',
             checks=checks)


# EXAMPLE: /ManagedNetworks/patch/ManagedNetworksPatch
@try_manual
def step_mn_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn update '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkGroups/put/ManagementNetworkGroupsPut
@try_manual
def step_mn_group_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn group create '
             '--management-groups "[]" '
             '--subnets id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNet'
             'works/{vn}/subnets/default" id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.'
             'Network/virtualNetworks/{vn_2}/subnets/default" '
             '--virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualN'
             'etworks/VnetA" '
             '--virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualN'
             'etworks/VnetB" '
             '--group-name "{myManagedNetworkGroup}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)
    test.cmd('az managed-network mn group wait --created '
             '--group-name "{myManagedNetworkGroup}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ManagedNetworkGroups/get/ManagedNetworksGroupsListByManagedNetwork
@try_manual
def step_mn_group_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn group list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkGroups/get/ManagementNetworkGroupsGet
@try_manual
def step_mn_group_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn group show '
             '--group-name "{myManagedNetworkGroup}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkPeeringPolicies/put/ManagedNetworkPeeringPoliciesPut
@try_manual
def step_managed_network_peering(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network managed-network-peering-policy hub-and-spoke-topology create '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myManagedNetworkPeeringPolicy}" '
             '--hub id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetwork'
             's/{vn_4}" '
             '--spokes id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.ManagedNetwork/mana'
             'gedNetworks/{myManagedNetwork}/managedNetworkGroups/{myManagedNetworkGroup}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkPeeringPolicies/get/ManagedNetworkPeeringPoliciesGet
@try_manual
def step_managed_network_peering_policy_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network managed-network-peering-policy show '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myManagedNetworkPeeringPolicy}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkPeeringPolicies/get/ManagedNetworkPeeringPoliciesListByManagedNetwork
@try_manual
def step_managed_network_peering_policy_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network managed-network-peering-policy list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkPeeringPolicies/delete/ManagedNetworkPeeringPoliciesDelete
@try_manual
def step_managed_network_peering_policy_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network managed-network-peering-policy delete -y '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myManagedNetworkPeeringPolicy}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ManagedNetworkGroups/delete/ManagementNetworkGroupsDelete
@try_manual
def step_mn_group_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn group delete -y '
             '--group-name "{myManagedNetworkGroup}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ScopeAssignments/put/ScopeAssignmentsPut
@try_manual
def step_mn_scope_assignment_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn scope-assignment create '
             '--assigned-managed-network "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Mana'
             'gedNetwork/managedNetworks/{myManagedNetwork}" '
             '--scope "subscriptions/subscriptionC" '
             '--name "{myScopeAssignment}"',
             checks=checks)


# EXAMPLE: /ScopeAssignments/get/ScopeAssignmentsGet
@try_manual
def step_mn_scope_assignment_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn scope-assignment show '
             '--scope "subscriptions/subscriptionC" '
             '--name "{myScopeAssignment}"',
             checks=checks)


# EXAMPLE: /ScopeAssignments/get/ScopeAssignmentsList
@try_manual
def step_mn_scope_assignment_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn scope-assignment list '
             '--scope "subscriptions/subscriptionC"',
             checks=checks)


# EXAMPLE: /ScopeAssignments/delete/ScopeAssignmentsDelete
@try_manual
def step_mn_scope_assignment_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn scope-assignment delete -y '
             '--scope "subscriptions/subscriptionC" '
             '--name "{myScopeAssignment}"',
             checks=checks)


# EXAMPLE: /ManagedNetworks/delete/ManagedNetworksDelete
@try_manual
def step_mn_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az managed-network mn delete -y '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=checks)

