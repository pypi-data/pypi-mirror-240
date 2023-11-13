"""
Export all available information about VMWare managed objects to JSON files.
"""
import json
import logging
import os
import re
from argparse import ArgumentParser
from datetime import date
from types import BuiltinFunctionType, BuiltinMethodType, FunctionType, MethodType
from pyVmomi import vim
from zut import ExtendedJSONEncoder
from .utils import dictify_ov, get_obj_name, get_obj_ref
from .commons import Context

logger = logging.getLogger(__name__)

DEFAULT_OUT = Context.get_out_dir().joinpath("dumps/{type}/{name} ({ref}).json")

def add_arguments(parser: ArgumentParser):
    parser.add_argument('search', nargs='*', help="Search term(s).")
    parser.add_argument('--key', '-k', choices=['name', 'ref'], default='name', help="Search key to use (default: %(default)s).")
    parser.add_argument('--normalize', '-n', action='store_true', help="Normalize search term(s) before searching.")
    parser.add_argument('--type', '-t', dest='types', metavar='type', help="Managed object type name (example: datastore).")
    parser.add_argument('--first', '-f', action='store_true', help="Only handle the first object found for each type.")
    parser.add_argument('--out', '-o', default=DEFAULT_OUT, help="Output JSON file (default: %(default)s).")
    Context.add_argument(parser)


def dump(context: Context, search: list[str|re.Pattern]|str|re.Pattern = None, key: str = 'name', normalize: bool = False, first: bool = False, types: list[type|str]|type|str = None, out: os.PathLike = DEFAULT_OUT):
    sample_types = []

    for obj in context.get_objs(types, search, key=key, normalize=normalize):
        if first:
            if type(obj) in sample_types:
                continue

        name = obj.name
        ref = get_obj_ref(obj)

        out = str(out).format(context=context.arg, type=type(obj).__name__, name=name, ref=ref)
        logger.info(f"export {name} ({ref}) to {out}")
        
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as fp:
            data = inspect_obj(obj)
            json.dump(data, fp=fp, indent=4, cls=ExtendedJSONEncoder, ensure_ascii=False)

        if first:
            sample_types.append(type(obj))


def inspect_obj(obj: vim.ManagedEntity, with_object_types=False, exclude_keys=[], maxdepth=None):
    for key in ['dynamicProperty', 'recentTask']:
        if not key in exclude_keys:
            exclude_keys.append(key)
    exclude_keys_containing = ['capability', 'alarm']
    keypath = []

    def keypath_str():
        s = ''
        for key in keypath:
            s += ('.' if s and not isinstance(key, int) else '') + (f"[{key}]" if isinstance(key, int) else key)
        return s

    def forward(key: str):
        keypath.append(key)

    def backward():
        del keypath[-1]

    def inspect_object(obj: object):
        result = { '_type': type(obj).__name__ } if with_object_types else {}
        any = False
        for key in dir(obj):
            ignore = False
            if key.startswith('_') or key in exclude_keys:
                ignore = True
            else:
                for containing in exclude_keys_containing:
                    if containing in key.lower():
                        ignore = True
                        break

            if ignore:
                continue

            forward(key)
            
            try:
                value = getattr(obj, key)
            except: # problem getting the data (e.g. invalid/not-supported accessor)
                logger.error('cannot read attribute: %s', keypath_str())
                value = "!error: cannot attribute"
            
            value = inspect(value)

            if value is not None:
                result[key] = value
                any = True

            backward()

        if any:
            return result

    def inspect_dict(data: dict):
        result = {}
        any = False
        for key in data:
            forward(key)
            value = inspect(data[key])
            if value is not None:
                result[key] = value
                any = True
            backward()

        if any:
            return result

    def inspect_list(data: list):
        result = dictify_ov(data)
        if isinstance(result, dict):
            return result

        # general case
        result = []
        any = False
        for i, value in enumerate(data):
            forward(i)
            extracted = inspect(value)
            if extracted is not None:
                result.append(extracted)
                any = True
            backward()

        if any:
            return result

    def inspect(data):
        if data is None or isinstance(data, (type, FunctionType, MethodType, BuiltinMethodType, BuiltinFunctionType)):
            return None
        
        elif isinstance(data, (str, int, float, complex)):
            return data

        elif isinstance(data, date):
            if data.year == 1970 and data.month == 1 and data.day == 1:
                return None
            return data

        elif isinstance(data, vim.ManagedEntity):
            if not keypath: # depth == 0
                result = identify_obj(data)
                for key, value in inspect_object(data).items():
                    result[key] = value
                return result
            else:
                return identify_obj(data)

        elif maxdepth and len(keypath) >= maxdepth:
            logger.error('reached maxdepth: %s', type(data).__name__)
            return f"!error:maxdepth({type(data).__name__})"

        elif isinstance(data, dict):
            return inspect_dict(data)

        elif isinstance(data, list):
            return inspect_list(data)
            
        else:
            return inspect_object(data)

    return inspect(obj)


def identify_obj(obj: vim.ManagedEntity) -> dict:
    if obj is None:
        return None

    if not isinstance(obj, vim.ManagedEntity):
        raise ValueError(f'invalid type: {type(obj)}')

    data = {
        "_type": type(obj).__name__, # managed object type
        "ref": get_obj_ref(obj),
        "name": get_obj_name(obj),
    }

    if data["name"] == "Resources" and isinstance(obj, vim.ResourcePool) and hasattr(obj, 'parent') and isinstance(obj.parent, vim.ClusterComputeResource):
        # root resource pool of a cluster (named 'Resources'): let's prepend cluster name
        data["name"] = get_obj_name(obj.parent) + "/" + data["name"]

    return data
