"""
Export inventory of VMWare managed objects to a YAML file.
"""
import logging
from argparse import ArgumentParser
import os
from pyVmomi import vim
from .commons import Context, get_obj_name, get_obj_ref

logger = logging.getLogger(__name__)

DEFAULT_OUT = Context.get_out_dir().joinpath("inventory.yml")


def add_arguments(parser: ArgumentParser):
    parser.add_argument('--out', '-o', default=DEFAULT_OUT, help="Output YAML file (default: %(default)s).")
    Context.add_argument(parser)


def inventory(context: Context, out: os.PathLike = DEFAULT_OUT):
    path = str(out).format(context=context.arg)
    logger.info(f"export inventory to {path}")

    os.makedirs(os.path.dirname(path), exist_ok=True)    
    with open(path, 'w', encoding='utf-8') as fp:                
        found_by_ref: dict[str,vim.ManagedEntity] = {}

        def recurse_tree(obj: vim.ManagedEntity, depth: int):
            space = ' ' * 2 * depth
            ref = get_obj_ref(obj)
            name = get_obj_name(obj)
            found_by_ref[ref] = obj
            print(f'{space}- {name} [{type(obj).__name__}, {ref}]', file=fp)

            if isinstance(obj, vim.Datacenter):
                print(f'{space}  - (datastore)', file=fp)
                for sub in obj.datastore:
                    recurse_tree(sub, depth+2)
                
                print(f'{space}  - (network)', file=fp)
                for sub in obj.network:
                    recurse_tree(sub, depth+2)
            
                recurse_tree(obj.datastoreFolder, depth+1)
                recurse_tree(obj.networkFolder, depth+1)
                recurse_tree(obj.hostFolder, depth+1)
                recurse_tree(obj.vmFolder, depth+1)

            elif isinstance(obj, vim.ComputeResource):
                print(f'{space}  - (host)', file=fp)
                for sub in obj.host:
                    recurse_tree(sub, depth+2)

                recurse_tree(obj.resourcePool, depth+1)

            if hasattr(obj, 'childEntity'):
                for sub in obj.childEntity:
                    recurse_tree(sub, depth+1)

        # Walk through the tree starting from root folder
        recurse_tree(context.service_content.rootFolder, 0)

        # Search through the container view
        view = None
        try:
            view = context.service_content.viewManager.CreateContainerView(context.service_content.rootFolder, recursive=True)
            first = True
            for obj in view.view:
                ref = get_obj_ref(obj)
                if not found_by_ref.pop(ref, None):
                    if first:
                        print(f'- (found in container view but not in inventory tree)', file=fp)
                        first = False
                
                    name = get_obj_name(obj)
                    print(f'  - {name} [{type(obj).__name__}, {ref}], child of {get_obj_name(obj.parent)} ({get_obj_ref(obj.parent)})', file=fp)
        finally:
            if view:
                view.Destroy()

        # Show elements missing in the container view
        first = True
        for ref, obj in found_by_ref.items():
            if obj == context.service_content.rootFolder:
                continue

            if first:
                print(f'- (found in inventory tree but not in container view)', file=fp)
                first = False
        
            name = get_obj_name(obj)
            print(f'  - {name} [{type(obj).__name__}, {ref}], child of {get_obj_name(obj.parent)} ({get_obj_ref(obj.parent)})', file=fp)
