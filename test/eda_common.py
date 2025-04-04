#
# Stub for EDA common, so you can run your scripts in bash
#
import os
import json
from utils.log import log_msg

DEBUG = os.getenv('DEBUG') if os.getenv('DEBUG') is not None else False
gSpecDb = {}
update_cr_list = []


class Schema:
    def __init__(self, group, version, kind):
        self.group = group
        self.version = version
        self.kind = kind

    def __eq__(self, other):
        return self.group == other.group and self.version == other.version and self.kind == other.kind

    def __hash__(self):
        return hash(self.group) ^ hash(self.kind)

    def __reduce__(self):
        return (self.__class__, (self.group, self.version, self.kind))

    def __lt__(self, other):
        return f'{self.group}_{self.kind}_{self.version}' < f'{other.group}_{other.kind}_{other.version}'


def update_cr(schema, name, spec=None, status=None, labels: dict = {}, ns=None):
    global update_cr_list
    if labels != {}:
        cr: dict
        for cr in update_cr_list:
            if cr.get('schema', None) == schema and cr.get('name', None) == name:
                for k, v in labels.items():
                    cr[k] = v
                return
    temp_cr_dict = {}
    temp_cr_dict["schema"] = schema
    temp_cr_dict["name"] = name
    if spec is not None:
        temp_cr_dict["spec"] = spec
    if status is not None:
        temp_cr_dict["status"] = status
    if labels != {}:
        temp_cr_dict["labels"] = status
    update_cr_list.insert(0, temp_cr_dict)
    log_msg(f'\n{schema.group}/{schema.version}/{schema.kind} name {name}:', debug=DEBUG)
    if spec is not None:
        log_msg("spec", dict=spec, debug=DEBUG)
        log_msg(f"================ configs for {name}", debug=DEBUG)
        configs = spec.get('configs', [])
        for cfg in configs:
            log_msg(cfg['path'], dict=json.loads(cfg['config']), debug=DEBUG)
        log_msg(f"================ done {name}", debug=DEBUG)
    if status is not None:
        log_msg("status", dict=status, debug=DEBUG)
    if labels is not None:
        log_msg("labels", dict=labels, debug=DEBUG)

#
# Use this functions to add to a fake cr db
#


def test_addcr(schema, cr):
    global gSpecDb
    gvkDb = gSpecDb.get(schema, [])
    gvkDb.append(cr)
    gSpecDb[schema] = gvkDb
