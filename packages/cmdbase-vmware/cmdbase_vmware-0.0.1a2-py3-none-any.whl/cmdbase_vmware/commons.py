from __future__ import annotations
from argparse import ArgumentParser
import logging
import re
from typing import Callable, Generic, Iterable, Literal, TypeVar
from uuid import UUID
from pyVmomi import vim, vmodl
from pyVim.connect import SmartConnect, Disconnect
from zut import Filters
from cmdbase_utils import BaseContext, BaseEntity
from .utils import get_obj_attr, get_obj_name, get_obj_ref, get_obj_type

logger = logging.getLogger(__name__)

T_Obj = TypeVar("T_Obj", bound=vim.ManagedEntity)


class Context(BaseContext):
    prog = 'cmdbase-vmware'

    def __exit__(self, exc_type = None, exc_value = None, exc_traceback = None):
        super().__exit__(exc_type, exc_value, exc_traceback)
        try:
            Disconnect(self._service_instance)
        except AttributeError:
            pass


    # -------------------------------------------------------------------------
    # region VMWare client
    #

    @property
    def service_instance(self) -> vim.ServiceInstance:
        try:
            return self._service_instance 
        except AttributeError:
            pass

        host = self._get_option('vcenter_host')
        user = self._get_option('vcenter_user')
        password = self._getsecret_option('vcenter_password')
        disable_ssl_verify = self._getboolean_option('vcenter_disable_ssl_verify', fallback=False)

        logger.info(f'connect to vcenter host {host} with user {user}')
        self._service_instance = SmartConnect(host=host, user=user, pwd=password, disableSslCertValidation=disable_ssl_verify)
    
        return self._service_instance


    @property
    def service_content(self) -> vim.ServiceInstanceContent:
        try:
            return self._service_content
        except AttributeError:
            pass

        self._service_content = self.service_instance.RetrieveContent()
        return self._service_content


    def find_obj(self, type: type[T_Obj], specs: list[str|re.Pattern]|str|re.Pattern|UUID, *, key: Literal['name', 'ref', 'uuid', 'bios_uuid'] = 'name', normalize: bool = False, default = '__raise__') -> T_Obj:
        """
        Find a single vim managed object.
        """
        if key in ['uuid', 'bios_uuid']:
            if not isinstance(specs, (UUID,str)):
                raise TypeError(f"specs must be UUID or str for key {key}, got {type(specs).__name__}")
            
            if isinstance(specs, UUID):
                uuid = specs
            else:
                uuid = UUID(specs)

            obj = None
            
            if key == 'bios_uuid':
                # NOTE: uuid is "BIOS UUID". Seems to match the end of `sudo cat /sys/class/dmi/id/product_uuid`.
                if type == vim.VirtualMachine:
                    obj = self._find_by_uuid(uuid, for_vm=True, instance_uuid=False)
                else:
                    raise ValueError(f"key '{key}' can be used only for virtual machines")
                
            else:
                if type == vim.VirtualMachine:
                    obj = self._find_by_uuid(uuid, for_vm=True, instance_uuid=True)
                elif type == vim.HostSystem:
                    obj = self._find_by_uuid(uuid, for_vm=False, instance_uuid=False)
                else:
                    raise ValueError(f"key '{key}' can be used only for virtual machines or host systems")

            if obj:
                return obj
            elif default == '__raise__':
                raise KeyError(f"not found: {specs} (type: {type.__name__})")
            else:
                return obj

        else:
            generator = self.get_objs(types=type, search=specs, key=key, normalize=normalize)
            try:
                if default == '__raise__':
                    return next(generator)
                else:
                    return next(generator, default)
            except StopIteration:
                raise KeyError(f"not found: {specs} (type: {type.__name__})")
            

    def _find_by_uuid(self, uuid: UUID|str, for_vm: bool, instance_uuid: bool):
        if isinstance(uuid, UUID):
            uuid = str(uuid)
        
        for datacenter in self.get_objs(vim.Datacenter):
            obj = self.service_content.searchIndex.FindByUuid(datacenter, uuid, vmSearch=for_vm, instanceUuid=instance_uuid)
            if obj:
                return obj


    def list_objs(self, types: list[type|str]|type|str = None, specs: list[str|re.Pattern]|str|re.Pattern = None, *, key: Literal['name', 'ref'] = 'name', normalize: bool = None, sort_key: str|list[str]|Callable = None):        
        """
        Search vim managed objects, returning a list that can optionnally be sorted.
        """
        objs = [obj for obj in self.get_objs(types, specs, key=key, normalize=normalize)]

        if sort_key:
            if isinstance(sort_key, str):
                sort_key = [sort_key]

            if isinstance(sort_key, list):
                sort_func = lambda obj: [get_obj_attr(obj, attr) for attr in sort_key]
            else:
                sort_func = sort_key

            objs.sort(key=sort_func)

        return objs


    def get_objs(self, types: list[type|str]|type|str = None, search: list[str|re.Pattern]|str|re.Pattern = None, *, key: Literal['name', 'ref'] = 'name', normalize: bool = None):
        """
        Search vim managed objects, returning a generator.
        """

        # Prepare value filter
        filters = Filters(search, normalize=normalize)

        # Prepare types
        if not types:
            types = []
        elif isinstance(types, (str,type)):
            types = [types]
        
        types = [get_obj_type(_type) for _type in types]

        # Search using a container view
        view = None
        try:
            view = self.service_content.viewManager.CreateContainerView(self.service_content.rootFolder, types, recursive=True)

            for obj in view.view:
                if self._obj_matches(obj, key, filters):
                    yield obj
        finally:
            if view:
                view.Destroy()


    def _obj_matches(self, obj: vim.ManagedEntity, key: Literal['name', 'ref'], filters: Filters):
        if not filters:
            return True
        
        if key == 'name':
            try:
                value = obj.name
            except vim.fault.NoPermission:
                return False
            
        elif key == 'ref':
            value = get_obj_ref(obj)
            
        else:
            raise ValueError(f"key not supported: {key}")
        
        return filters.matches(value)


    @property
    def cookie(self) -> dict:
        try:
            return self._cookie
        except AttributeError:
            pass
    
        # Get the cookie built from the current session
        client_cookie = self.service_instance._stub.cookie

        # Break apart the cookie into it's component parts
        cookie_name = client_cookie.split("=", 1)[0]
        cookie_value = client_cookie.split("=", 1)[1].split(";", 1)[0]
        cookie_path = client_cookie.split("=", 1)[1].split(";", 1)[1].split(
            ";", 1)[0].lstrip()
        cookie_text = " " + cookie_value + "; $" + cookie_path

        # Make a cookie
        self._cookie = dict()
        self._cookie[cookie_name] = cookie_text
        return self._cookie


    def wait_for_tasks(self, *tasks: vim.Task):
        """
        Given a service instance and tasks, return after all the tasks are complete.
        """
        property_collector = self.service_instance.content.propertyCollector
        task_list = [str(task) for task in tasks]
        # Create filter
        obj_specs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task) for task in tasks]
        property_spec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task, pathSet=[], all=True)
        filter_spec = vmodl.query.PropertyCollector.FilterSpec()
        filter_spec.objectSet = obj_specs
        filter_spec.propSet = [property_spec]
        pc_filter = property_collector.CreateFilter(filter_spec, True)
        try:
            version, state = None, None
            # Loop looking for updates till the state moves to a completed state.
            while task_list:
                update = property_collector.WaitForUpdates(version)
                for filter_set in update.filterSet:
                    for obj_set in filter_set.objectSet:
                        task = obj_set.obj
                        for change in obj_set.changeSet:
                            if change.name == 'info':
                                state = change.val.state
                            elif change.name == 'info.state':
                                state = change.val
                            else:
                                continue

                            if not str(task) in task_list:
                                continue

                            if state == vim.TaskInfo.State.success:
                                # Remove task from taskList
                                task_list.remove(str(task))
                            elif state == vim.TaskInfo.State.error:
                                raise task.info.error
                # Move to next version
                version = update.version
        finally:
            if pc_filter:
                pc_filter.Destroy()

    #endregion


class Entity(BaseEntity[Context, T_Obj], Generic[T_Obj]):
    objtype_parent = vim.ManagedEntity

    @property
    def name(self):
        return get_obj_name(self.obj)
    
    @property
    def ref(self):
        return f"{self.context.refprefix}{get_obj_ref(self.obj)}"


    @classmethod
    def extract_add_arguments(cls, parser: ArgumentParser):
        parser.add_argument('search', nargs='*', help="Search term(s).")
        parser.add_argument('--key', '-k', choices=['name', 'ref'], default='name', help="Search key to use (default: %(default)s).")
        parser.add_argument('--normalize', '-n', action='store_true', help="Normalize search term(s) before searching.")
        super().extract_add_arguments(parser)


    @classmethod
    def extract_objs(cls, context: Context, search: list[str|re.Pattern]|str|re.Pattern = None, key: str = 'name', normalize: bool = False) -> Iterable[T_Obj]:
        return context.get_objs(cls.get_objtype(), search, key=key, normalize=normalize)
