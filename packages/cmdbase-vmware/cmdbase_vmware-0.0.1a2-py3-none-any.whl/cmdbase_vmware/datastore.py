from pyVmomi import vim
from cmdbase_utils import as_gib
from .commons import Entity

class Datastore(Entity[vim.Datastore]):
    def collect(self):
        data = {
            "_c": "VDisk",
            "_k": "vmware_datastore.ref",
            "name": self.name,
            'capacity': as_gib(self.obj.summary.capacity),
            'freespace': as_gib(self.obj.summary.freeSpace),
            "vmware_datastore": {
                "ref": self.ref,
                "uuid": self.obj.info.vmfs.uuid,
                'type': self.obj.summary.type,
                'scsi_disks': [
                    {'name': extent.diskName, 'partition': extent.partition}
                    for extent in self.obj.info.vmfs.extent
                ]
            }
        }

        return data
