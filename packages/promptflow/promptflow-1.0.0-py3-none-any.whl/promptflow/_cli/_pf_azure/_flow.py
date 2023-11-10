# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import argparse
from typing import Dict, List

from promptflow._cli._params import add_param_set, logging_params
from promptflow._cli._pf_azure._utils import _get_azure_pf_client
from promptflow._cli._utils import _set_workspace_argument_for_subparsers, activate_action


def add_parser_flow(subparsers):
    """Add flow parser to the pf subparsers."""
    flow_parser = subparsers.add_parser(
        "flow",
        description="Manage flows for promptflow.",
        help="pfazure flow",
    )
    flow_subparsers = flow_parser.add_subparsers()
    add_parser_flow_create(flow_subparsers)
    # add_parser_flow_get(flow_subparsers)
    # add_parser_flow_list(flow_subparsers)
    # add_parser_flow_delete(flow_subparsers)
    # add_parser_flow_download(flow_subparsers)
    flow_parser.set_defaults(action="flow")


def add_parser_flow_create(subparsers):
    """Add flow create parser to the pf flow subparsers."""
    epilog = """
Use "--set" to set flow properties like:
    name: Flow name that will be created in remote. Default to be flow folder name + timestamp if not specified.
    type: Flow type. Default to be "standard" if not specified. Available types are: "standard", "evaluation", "chat".
    description: Flow description. e.g. "--set description=<description>."
    tags: Flow tags. e.g. "--set tags.key1=value1 tags.key2=value2."

Examples:
# Create a flow to azure portal with local flow folder.
pfazure flow create --flow <flow-folder-path> --set name=<flow-name> type=<flow-type>

# Create a flow with more properties
pfazure flow create --flow <flow-folder-path> --set name=<flow-name> type=<flow-type> description=<flow-description> tags.key1=value1 tags.key2=value2
"""  # noqa: E501
    add_param_source = lambda parser: parser.add_argument(  # noqa: E731
        "--flow", type=str, help="Source folder of the flow."
    )
    add_params = [
        _set_workspace_argument_for_subparsers,
        add_param_source,
        add_param_set,
    ] + logging_params

    activate_action(
        name="create",
        description="A CLI tool to create a flow to Azure.",
        epilog=epilog,
        add_params=add_params,
        subparsers=subparsers,
        help_message="Create a flow to Azure with local flow folder.",
        action_param_name="sub_action",
    )


def add_parser_flow_list(subparsers):
    """Add flow list parser to the pf flow subparsers."""
    add_params = [_set_workspace_argument_for_subparsers] + logging_params

    activate_action(
        name="list",
        description="List flows for promptflow.",
        epilog=None,
        add_params=add_params,
        subparsers=subparsers,
        help_message="pf flow list",
        action_param_name="sub_action",
    )


def add_parser_flow_download(subparsers):
    """Add flow download parser to the pf flow subparsers."""
    add_param_source = lambda parser: parser.add_argument(  # noqa: E731
        "--source", type=str, help="The flow folder path on file share to download."
    )
    add_param_destination = lambda parser: parser.add_argument(  # noqa: E731
        "--destination", "-d", type=str, help="The destination folder path to download."
    )
    add_params = [
        _set_workspace_argument_for_subparsers,
        add_param_source,
        add_param_destination,
    ] + logging_params

    activate_action(
        name="download",
        description="Download a flow from file share to local.",
        epilog=None,
        add_params=add_params,
        subparsers=subparsers,
        help_message="pf flow download",
        action_param_name="sub_action",
    )


def dispatch_flow_commands(args: argparse.Namespace):
    if args.sub_action == "create":
        create_flow(args)


def _get_flow_operation(subscription_id, resource_group, workspace_name):
    pf_client = _get_azure_pf_client(subscription_id, resource_group, workspace_name)
    return pf_client._flows


def create_flow(args: argparse.Namespace):
    """Create a flow for promptflow."""
    pf = _get_azure_pf_client(args.subscription, args.resource_group, args.workspace_name, debug=args.debug)
    params = _parse_flow_metadata_args(args.params_override)
    pf.flows.create_or_update(
        flow=args.flow,
        name=params.get("name", None),
        type=params.get("type", None),
        description=params.get("description", None),
        tags=params.get("tags", None),
    )


def list_flows(
    workspace_name: str,
    resource_group: str,
    subscription_id: str,
):
    """List flows for promptflow."""
    flow_operations = _get_flow_operation(subscription_id, resource_group, workspace_name)
    flows = flow_operations._list()
    flow_count = len(flows)
    print(f"Collected {flow_count} flows.")
    if flow_count > 0:
        print("=================== Flows ===================")
        for flow in flows:
            print(f"Name: {flow.name!r}, owner: {flow.owner!r}, flow_id: {flow.flow_id!r}")


def download_flow(
    source: str,
    destination: str,
    workspace_name: str,
    resource_group: str,
    subscription_id: str,
):
    """Download a flow from file share to local."""
    flow_operations = _get_flow_operation(subscription_id, resource_group, workspace_name)
    flow_operations.download(source, destination)
    print(f"Successfully download flow from file share path {source!r} to {destination!r}.")


def _parse_flow_metadata_args(params: List[Dict[str, str]]) -> Dict:
    result, tags = {}, {}
    if not params:
        return result
    for param in params:
        for k, v in param.items():
            if k.startswith("tags."):
                tag_key = k.replace("tags.", "")
                tags[tag_key] = v
                continue
            result[k] = v
    result["tags"] = tags
    return result
