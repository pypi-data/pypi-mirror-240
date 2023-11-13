from argparse import ArgumentParser
from pyVmomi import vim
from .commons import Context, Entity


class License(Entity[vim.LicenseManager.LicenseInfo]):
    @classmethod
    def extract_add_arguments(cls, parser: ArgumentParser):
        parser.add_argument('--out', '-o', help="Output json file (default: send to CMDBase API).")
        Context.add_argument(parser)


    @classmethod
    def extract_objs(cls, context: Context):
        return sorted(context.service_content.licenseManager.licenses, key=lambda obj: (obj.name, obj.licenseKey))
    

    @property
    def name(self):
        return f"VMWare {self.obj.licenseKey}"
    

    @classmethod
    def collect_headers(cls, context: Context):
        return [
            # Define aliases
            {"_c": "Vendor", "name": "VMWare", "_a": "VMWare"}
        ]


    def collect(self):
        if self.obj.editionKey == 'eval':
            return None
        
        product_name = self.obj.name
        if product_name.startswith("VMware vSphere"):
            product_name = product_name[len("VMware "):]

        data = {
            "_c": "License",
            "_k": ["product", "serial"],
            "name": self.name,
            "serial": self.obj.licenseKey,
            "product": {"_c": "Product", "name": product_name, "vendor": {"_a": "VMWare"}},
            "vmware_license": {
                "edition": self.obj.editionKey,
                "cost_unit": self.obj.costUnit,
                "total_units": self.obj.total,
                "used_units": self.obj.used,
            }
        }

        return data
