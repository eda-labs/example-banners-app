#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as ecommon

from common.metadata import Metadata, Y_NAME

from banners.api.v1alpha1.pysrc.constants import *
Y_NODES = 'nodes'
# Package objects (GVK Schemas)
BANNERSTATE_SCHEMA = ecommon.Schema(group='banners.eda.local', version='v1alpha1', kind='BannerState')


class BannerStateSpec:
    def __init__(
        self,
        nodes: list[str],
    ):
        self.nodes = nodes
        
    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.nodes is not None:
            _rval[Y_NODES] = self.nodes
        return _rval

    @staticmethod
    def from_input(obj):
        if obj:
            _nodes = obj.get(Y_NODES)
            return BannerStateSpec(
                nodes=_nodes,
            )
        return None  # pragma: no cover


class BannerStateStatus:
    def __init__(
        self,
    ):
        pass
        
    def to_input(self):  # pragma: no cover
        _rval = {}
        return _rval

    @staticmethod
    def from_input(obj):
        if obj:
            return BannerStateStatus(
            )
        return None  # pragma: no cover


class BannerState:
    def __init__(
        self,
        metadata: Metadata,
        spec: BannerStateSpec,
        status: BannerStateStatus
    ):
        self.metadata = metadata
        self.spec = spec
        self.status = status

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.metadata is not None:
            _rval[Y_NAME] = self.metadata.name
        if self.spec is not None:
            _rval[Y_SPEC] = self.spec.to_input()
        if self.status is not None:
            _rval[Y_STATUS] = self.status.to_input()
        return _rval

    @staticmethod
    def from_input(obj):
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = BannerStateSpec.from_input(obj.get(Y_SPEC, None))
            _status = BannerStateStatus.from_input(obj.get(Y_STATUS))
            return BannerState(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class BannerStateList:
    def __init__(
        self,
        listMeta: any,
        items: list[BannerState]
    ):
        self.listMeta = listMeta
        self.items = items

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.listMeta is not None:
            _rval[Y_METADATA] = self.listMeta
        if self.items is not None:
            _rval[Y_ITEMS] = self.items
        return _rval

    @staticmethod
    def from_input(obj):
        if obj:
            _listMeta = obj.get(Y_METADATA, None)
            _items = obj.get(Y_ITEMS, [])
            return BannerStateList(
                listMeta=_listMeta,
                items=_items,
            )
        return None  # pragma: no cover
