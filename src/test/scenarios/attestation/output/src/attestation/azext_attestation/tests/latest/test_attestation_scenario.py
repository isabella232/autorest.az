# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_list_operation
from .example_steps import step_create_provider
from .example_steps import step_attestation_provider_show
from .example_steps import step_attestation_provider_provider_list
from .example_steps import step_attestation_provider_provider_list2
from .example_steps import step_attestation_provider_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg, rg_2, rg_3):
    pass


# Env mytest
@try_manual
def mytest(test, rg, rg_2, rg_3):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg, rg_2, rg_3):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg, rg_2, rg_3):
    setup_scenario(test, rg, rg_2, rg_3)
    step_list_operation(test, rg, rg_2, rg_3, checks=[])
    step_create_provider(test, rg, rg_2, rg_3, checks=[])
    step_attestation_provider_show(test, rg, rg_2, rg_3, checks=[])
    mytest(test, rg, rg_2, rg_3)
    step_attestation_provider_provider_list(test, rg, rg_2, rg_3, checks=[])
    step_attestation_provider_provider_list2(test, rg, rg_2, rg_3, checks=[])
    step_attestation_provider_delete(test, rg, rg_2, rg_3, checks=[])
    cleanup_scenario(test, rg, rg_2, rg_3)


# Test class for Scenario
@try_manual
class AttestationScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestattestation_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestattestation_testrg1'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestattestation_sample-resource-group'[:7], key='rg_3',
                           parameter_name='rg_3')
    def test_attestation_Scenario(self, rg, rg_2, rg_3):

        call_scenario(self, rg, rg_2, rg_3)
        calc_coverage(__file__)
        raise_if()

