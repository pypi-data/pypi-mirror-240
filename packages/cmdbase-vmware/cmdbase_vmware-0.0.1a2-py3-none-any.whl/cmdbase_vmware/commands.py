import os
from argparse import ArgumentParser
from zut import add_module_command, add_func_command, get_help_text, get_leaf_classes
from .commons import Context, Entity
from . import inventory, dump


def add_arguments(parser: ArgumentParser):
    """
    Add all commands defined in `cmdbase_vmware`.

    It may be reused as is by applications that extend it.
    """

    subparsers = parser.add_subparsers(title="commands")
    add_func_command(subparsers, all_handle, all_add_arguments, name='all', doc=f"(Default) {get_help_text(all_handle.__doc__)}")

    for entity_cls in _get_entity_classes():
        add_func_command(subparsers,
            func = entity_cls.extract_handle,
            add_arguments = entity_cls.extract_add_arguments,
            doc = entity_cls.extract_doc(),
            name = entity_cls.get_itemname(),
        )

    add_module_command(subparsers, inventory)
    add_module_command(subparsers, dump)


def all_add_arguments(parser: ArgumentParser):
    parser.add_argument('--out', '-o', help="output json file (default: send to CMDBase API)")
    Context.add_argument(parser)


def all_handle(context: Context, out: os.PathLike = None):
    """
    Collect and export all data.
    """
    for entity_cls in _get_entity_classes():
        entity_cls.extract_handle(context, out)


def _get_entity_classes():
    return sorted(get_leaf_classes(Entity), key=lambda cls: cls.get_itemname())
