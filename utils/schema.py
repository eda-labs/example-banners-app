#!/usr/bin/env python3

import eda_common as p

NAMESPACE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                            version='v1',
                            kind='Namespace')
NODE_USER_SCHEMA = p.Schema(group='core.eda.nokia.com',
                            version='v1',
                            kind='NodeUser')
CONFIGLET_SCHEMA = p.Schema(group='config.eda.nokia.com',
                            version='v1alpha1',
                            kind='Configlet')
CONFIGLET_STATE_SCHEMA = p.Schema(group='config.eda.nokia.com',
                                  version='v1alpha1',
                                  kind='ConfigletState')
CONFIG_SCHEMA = p.Schema(group='core.eda.nokia.com',
                         version='v1',
                         kind='NodeConfig')
TOPOLOGY_NODE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                version='v1',
                                kind='TopoNode')
TOPOLOGY_LINK_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                version='v1',
                                kind='TopoLink')
TARGET_NODE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                              version='v1',
                              kind='TargetNode')
NODE_PROFILE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                               version='v1',
                               kind='NodeProfile')
ARTIFACT_SCHEMA = p.Schema(group='artifacts.eda.nokia.com',
                           version='v1',
                           kind='Artifact')
GLOBAL_CONFIG_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                version='v1',
                                kind='GlobalConfig')
EDGE_INTERFACE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                 version='v1',
                                 kind='EdgeInterface')
IP_ALLOCATION_POOL_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                     version='v1',
                                     kind='IPAllocationPool')
NODE_SECURITY_PROFILE_SCHEMA = p.Schema(group='core.eda.nokia.com',
                                        version='v1',
                                        kind='NodeSecurityProfile')

# Kubernetes core objects
POD_SCHEMA = p.Schema(group='',
                            version='v1',
                            kind='Pod')
DEPLOYMENT_SCHEMA = p.Schema(group='apps',
                             version='v1',
                             kind='Deployment')
DEPLOYMENT_SCHEMA = p.Schema(group='apps',
                             version='v1',
                             kind='Deployment')
CONFIG_MAP_SCHEMA = p.Schema(group='',
                             version='v1',
                             kind='ConfigMap')
SECRET_SCHEMA = p.Schema(group='',
                         version='v1',
                         kind='Secret')
