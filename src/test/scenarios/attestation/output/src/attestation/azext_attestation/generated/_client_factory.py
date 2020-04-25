# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_attestation(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.attestation import AttestationManagementClient
    return get_mgmt_service_client(cli_ctx, AttestationManagementClient)


def cf_operation(cli_ctx, *_):
    return cf_attestation(cli_ctx).operation


def cf_attestation_provider(cli_ctx, *_):
    return cf_attestation(cli_ctx).attestation_provider
