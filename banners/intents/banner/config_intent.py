#!/usr/bin/env python3
import eda_common as eda
import utils.node_utils as nutils
import utils.exceptions as e

from common.constants import PLATFORM_SRL, PLATFORM_SROS
from utils.log import log_msg
from banners.api.v1alpha1.pysrc.banner import Banner
from banners.api.v1alpha1.pysrc.bannerstate import BANNERSTATE_SCHEMA
from banners.intents.banner.handlers import get_config_handler
from banners.intents.banner.init import init_globals_defaults, validate

EDA_DEBUG = False

def process_cr(cr):
    """Process Banner CR."""
    log_msg("Banner CR:", debug=EDA_DEBUG, dict=cr)
    cr_obj = Banner.from_input(cr)
    if cr_obj is None:
        return

    cr_name = cr_obj.metadata.name
    validate(cr_obj)
    init_globals_defaults(cr_obj)
    nodes = {}

    if cr_obj.spec.nodeSelector is not None and len(cr_obj.spec.nodeSelector) > 0:
        log_msg("Filtering nodes with node selectors:", debug=EDA_DEBUG, dict=cr_obj.spec.nodeSelector)
        for node_cr in nutils.list_nodes(filter=[], label_filter=cr_obj.spec.nodeSelector):
            node_name = node_cr["metadata"]["name"]
            nodes[node_name] = node_cr
            log_msg("Found node:", debug=EDA_DEBUG, dict=node_name)

    if cr_obj.spec.nodes is not None and len(cr_obj.spec.nodes) > 0:
        for node in cr_obj.spec.nodes:
            if node not in nodes:
                node_cr = nutils.get_node(name=node)
                if node_cr is None:
                    msg = f"Node {node} not found"
                    raise e.InvalidInput(msg)
                nodes[node] = node_cr

    for node, node_cr in nodes.items():
        if node_cr is not None:
            node_spec = node_cr["spec"]
            if node_spec.get("operatingSystem", None) is not None:
                if node_spec.get("operatingSystem") == PLATFORM_SRL:
                    srl_handler = get_config_handler(PLATFORM_SRL)
                    if srl_handler is not None:
                        srl_handler.handle_cr(cr_obj, node_cr)
                elif node_spec.get("operatingSystem") == PLATFORM_SROS:
                    sros_handler = get_config_handler(PLATFORM_SROS)
                    if sros_handler is not None:
                        sros_handler.handle_cr(cr_obj, node_cr)
                else:
                    msg = f'Operating system unsupported for {node}, os is {node_spec.get("operatingSystem", None)}'
                    raise e.InvalidInput(msg)
            else:
                msg = f'Operating system unsupported for {node}, os is {node_spec.get("operatingSystem", None)}'
                raise e.InvalidInput(msg)

    eda.update_cr(
        schema=BANNERSTATE_SCHEMA,
        name=cr_name,
        spec={
            "nodes": list(nodes.keys()),
        },
    )
