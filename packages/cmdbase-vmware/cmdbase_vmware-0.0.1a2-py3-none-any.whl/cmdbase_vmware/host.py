from pyVmomi import vim
from cmdbase_utils import as_gib
from .utils import dictify_ov
from .commons import Entity

class Host(Entity[vim.HostSystem]):
    def collect(self):
        info = dictify_ov(self.obj.hardware.systemInfo.otherIdentifyingInfo)

        data = {
            "_c": "Server",
            "_k": "vmware_host.ref",
            "name": self.name,
            "memory": as_gib(self.obj.hardware.memorySize),
            "cpu": self.obj.hardware.cpuInfo.numCpuPackages,
            "cpu_cores": self.obj.hardware.cpuInfo.numCpuCores,
            "cpu_threads": self.obj.hardware.cpuInfo.numCpuThreads,
            "cpu_product": {"_c": "Product", "name": self.obj.summary.hardware.cpuModel},
            "cpu_frequency": self.obj.hardware.cpuInfo.hz/10**9,
            "product": {"_c": "Product", "name": self.obj.hardware.systemInfo.model, "vendor": {"_c": "Vendor", "name": self.obj.hardware.systemInfo.vendor}},
            "serial": info["SerialNumberTag"],
            "location": {"_c": "Enclosure", "_k": "serial", "serial": info["EnclosureSerialNumberTag"]},
            "vmware_host": {
                "ref": self.ref,
                "cluster":self.obj.parent.name,
                "master": (self.obj.runtime.dasHostState and self.obj.runtime.dasHostState.state == "master") or None,
                "booted": self.obj.runtime.bootTime,
                "app": self.obj.config.product.fullName,
            }
        }

        return data
