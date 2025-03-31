#!/usr/bin/env python3
import eda_common as eda

from banners.api.v1alpha1.pysrc.banner import BANNER_SCHEMA
from banners.api.v1alpha1.pysrc.bannerstate import (
    Y_NODES,
    BannerState,
)


class EdaStateHandler:
    def handle_cr(self, cr_obj: BannerState):
        nodes = cr_obj.spec.nodes
        eda.update_cr(
            schema=BANNER_SCHEMA,
            name=cr_obj.metadata.name,
            status={
                Y_NODES: nodes,
            },
        )
