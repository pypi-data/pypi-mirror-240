from __future__ import annotations
import re
from typing import Any
from pyVmomi import vim


def get_obj_ref(obj: vim.ManagedEntity) -> str:
    """
    Get the value of the Managed Object Reference (MOR) of the given object.

    See: https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/mo-types-landing.html
    """
    text = str(obj)
    m = re.match(r"^'(.*)\:(.*)'$", text)
    if not m:
        raise ValueError(f'invalid object identifier: {text}')
    
    expected_type = type(obj).__name__
    if m.group(1) != expected_type:
        raise ValueError(f'invalid type for object identifier: {text}, expected: {expected_type}')
    return m.group(2)


def get_obj_attr(obj: vim.ManagedEntity, attr: str):
    try:
        return getattr(obj, attr)
    except Exception as err:
        return f"!{type(err).__name__}:{err}"


def get_obj_name(obj: vim.ManagedEntity) -> str:
    return get_obj_attr(obj, 'name')


def get_obj_name_or_ref(obj: vim.ManagedEntity) -> str:
    try:
        return obj.name
    except vim.fault.NoPermission:
        return f"ref:{get_obj_ref(obj)}"


def get_obj_path(obj: vim.ManagedEntity) -> str:
    """ Return the full path of the given vim managed object. """
    if not obj.parent or isinstance(obj.parent, vim.Datacenter):
        return get_obj_name_or_ref(obj)
    else:
        return get_obj_path(obj.parent) + "/" + get_obj_name_or_ref(obj)


def _enumerate_obj_types(cls: type[vim.ManagedEntity]):
    yield cls

    for subcls in cls.__subclasses__():
        yield from _enumerate_obj_types(subcls)


OBJ_TYPES: dict[str,vim.ManagedEntity] = {cls.__name__.split('.')[-1].lower(): cls for cls in _enumerate_obj_types(vim.ManagedEntity)}


def get_obj_type(value: str|type|vim.ManagedEntity) -> type[vim.ManagedEntity]:
    if not value:
        raise ValueError(f"name cannot be blank")
    
    elif isinstance(value, type):
        if not issubclass(value, vim.ManagedEntity):
            raise TypeError(f"type {value} is not a subclass of vim.ManagedEntity")
        
        return value
    
    elif isinstance(value, vim.ManagedEntity):
        return type(value)
    
    elif not isinstance(value, str):
        raise TypeError(f"invalid type for name: {value}")
    
    else:
        lower = value.lower()

        # Search in types
        if lower in OBJ_TYPES:
            return OBJ_TYPES[lower]

        # Handle aliases            
        if lower == 'vm':
            return vim.VirtualMachine
        if lower == 'host':
            return vim.HostSystem
        if lower == 'net':
            return vim.Network
        if lower == 'dvs':
            return vim.DistributedVirtualSwitch
        if lower == 'dvp':
            return vim.dvs.DistributedVirtualPortgroup
        if lower == 'ds':
            return vim.Datastore
        if lower == 'dc':
            return vim.Datacenter
        if lower == 'cluster':
            return vim.ClusterComputeResource

        raise KeyError(f"vim managed object type not found for name {value}")


def dictify_ov(data: list):
    """
    Return a dict if obj is a list of OptionValue objects.
    Otherwise leave as is.
    """
    if not isinstance(data, list):
        return data

    def allinstance(enumerable_instance, element_type):
        any = False
        for element in enumerable_instance:
            any = True
            if not isinstance(element, element_type):
                return False
        return any
        
    if allinstance(data, vim.option.OptionValue) or allinstance(data, vim.CustomFieldsManager.StringValue): #example for vm: config.extraConfig, summary.config.customValue
        result = {}
        for ov in data:
            key = ov.key
            value = ov.value
            if key == "guestOS.detailed.data":
                value = parse_guestos_detailed_data(value)
            result[key] = value
        return result

    elif allinstance(data, vim.host.SystemIdentificationInfo): #example for host: summary.hardware.otherIdentifyingInfo
        result = {}
        for ov in data:
            key = ov.identifierType.key
            value = ov.identifierValue
            result[key] = value
        return result

    else:
        return data


def parse_guestos_detailed_data(val: str) -> dict:
    data = {}

    if not val:
        return data

    for m in re.findall(r"([a-zA-Z0-9]+)='([^']+)'", val):
        key = m[0]
        value = m[1]
        if key == "bitness":
            value = int(value)
        data[key] =value

    if len(data) == 0:
        return val

    data = dict(sorted(data.items()))

    return data


def detect_specials(obj: vim.ManagedObject, expected: dict[str,Any], attr_prefix: str = None, use_full_attr: bool = False):
    results = None

    for attr, expected_value in expected.items():
        full_attr = (f'{attr_prefix}.' if attr_prefix else '') + attr
        value = get_obj_attr(obj, attr)

        if isinstance(expected_value, dict) and isinstance(value, vim.ManagedObject):
            result = detect_specials(value, expected_value, attr_prefix=full_attr)
        elif value != expected_value:
            result = f'{full_attr if use_full_attr else attr}: {value}'
        else:
            continue

        results = (f'\n{results}' if results else '') + result

    return results
