from pyVmomi import vim
from cmdbase_utils import as_gib
from .utils import dictify_ov, get_obj_path, get_obj_ref
from .commons import Entity

class VM(Entity[vim.VirtualMachine]):
    def collect(self):
        info = dictify_ov(self.obj.config.extraConfig)

        host = self.obj.runtime.host
        
        if self.obj.resourcePool:            
            cluster = self.obj.resourcePool
            while cluster and not isinstance(cluster, vim.ClusterComputeResource):                
                cluster = cluster.parent
        else:
            cluster = None
        
        data = {
            "_c": "VM",
            "_k": "vmware_vm.ref",
            "name": self.name,
            "memory": self.obj.config.hardware.memoryMB / 1024,
            "cpu": self.obj.config.hardware.numCPU,
            "disks": {
                x.unitNumber: {
                    "datastore": {"_c": "VDisk", "name": x.backing.datastore.name},
                    "capacity": as_gib(x.capacityInBytes)
                }
                for x in self.obj.config.hardware.device if hasattr(x, "capacityInBytes")
            },
            "os_disks": {
                x.diskPath: {
                    "capacity": as_gib(x.capacity)
                }
                for x in self.obj.guest.disk
            },
            "ipaddress": self.obj.guest.ipAddress,
            "hostname": self.obj.guest.hostName,
            "vmware_vm": {
                "ref": self.ref,
                "cluster": {"_c": "VMCluster", "_k": "vmware_cluster.ref", "name": cluster.name, "vmware_cluster": {"ref": f"{self.context.refprefix}{get_obj_ref(cluster)}"}} if cluster else None, # None for templates
                "template": self.obj.config.template,
                "power_state": self.obj.runtime.powerState,
                "folder": get_obj_path(self.obj.parent),
                "datastores": [{"_c": "VDisk", "name": f"{x.name}"} for x in self.obj.datastore],
                "networks": [x.name for x in self.obj.network], # TODO: reference to vswitch instead?
                "host": {"_c": "Server", "_k": "vmware_host.ref", "name": host.name, "vmware_host": {"ref": f"{self.context.refprefix}{get_obj_ref(host)}"}},
                "config_created": self.obj.config.createDate,
                "config_changed": self.obj.config.changeVersion,
                "cores_per_socket": self.obj.config.hardware.numCoresPerSocket,
                # TODO: normalize below references
                "guest_bitness": info.get("guestOS.detailed.data", {}).get("bitness", None),
                "guest_tools": info.get("guestinfo.vmtools.description", None),
                "guest_kernel": info.get("guestOS.detailed.data", {}).get("kernelVersion", None),
                "guest_os": info.get("guestOS.detailed.data", {}).get("prettyName", None),
                "guest_config_os": self.obj.config.guestFullName,
            }
        }

        return data
