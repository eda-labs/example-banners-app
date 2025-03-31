#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as ecommon

from common.metadata import Metadata, Y_NAME

from banners.api.v1alpha1.pysrc.constants import *
Y_NODES = 'nodes'
Y_NODESELECTOR = 'nodeSelector'
Y_LOGINBANNER = 'loginBanner'
# Package objects (GVK Schemas)
BANNER_SCHEMA = ecommon.Schema(group='banners.eda.local', version='v1alpha1', kind='Banner')


class BannerSpec:
    def __init__(
        self,
        nodes: list[str],
        nodeSelector: list[str],
        loginBanner: str,
    ):
        self.nodes = nodes
        self.nodeSelector = nodeSelector
        self.loginBanner = loginBanner
        
    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.nodes is not None:
            _rval[Y_NODES] = self.nodes
        if self.nodeSelector is not None:
            _rval[Y_NODESELECTOR] = self.nodeSelector
        if self.loginBanner is not None:
            _rval[Y_LOGINBANNER] = self.loginBanner
        return _rval

    @staticmethod
    def from_input(obj):
        if obj:
            _nodes = obj.get(Y_NODES)
            _nodeSelector = obj.get(Y_NODESELECTOR)
            _loginBanner = obj.get(Y_LOGINBANNER)
            return BannerSpec(
                nodes=_nodes,
                nodeSelector=_nodeSelector,
                loginBanner=_loginBanner,
            )
        return None  # pragma: no cover


class BannerStatus:
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
            return BannerStatus(
                nodes=_nodes,
            )
        return None  # pragma: no cover


class Banner:
    def __init__(
        self,
        metadata: Metadata,
        spec: BannerSpec,
        status: BannerStatus
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
            _spec = BannerSpec.from_input(obj.get(Y_SPEC, None))
            _status = BannerStatus.from_input(obj.get(Y_STATUS))
            return Banner(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class BannerList:
    def __init__(
        self,
        listMeta: any,
        items: list[Banner]
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
            return BannerList(
                listMeta=_listMeta,
                items=_items,
            )
        return None  # pragma: no cover
