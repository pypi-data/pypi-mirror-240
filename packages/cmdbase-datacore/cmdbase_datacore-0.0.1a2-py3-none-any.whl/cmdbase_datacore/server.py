from enum import Enum
import logging
import re
from uuid import UUID
from cmdbase_utils import as_gib
from .commons import Context, Entity

logger = logging.getLogger(__name__)


class Server(Entity):
    @classmethod
    def collect_headers(cls, context: Context):
        cls.license_name_per_serverid = {}


        data_list = [
            # Define aliases
            {"_c": "Vendor", "name": "Datacore", "_a": "Datacore"},
            {"_c": "Vendor", "name": "Microsoft", "_a": "Microsoft"},
        ]

        for obj in context.get_with_retries('servergroups'):
            data = cls.collect_servergroup(context, obj)
            data_list.append(data)

        return data_list


    @classmethod
    def collect_servergroup(cls, context: Context, obj: dict):
        licenses = []
        nonserver_license_name = None
        for productkey in obj["ExistingProductKeys"]:
            license_data = {
                "_c": "License",
                "name": f'Datacore {productkey["LastFive"]}',
                "serial_suffix": productkey["LastFive"],
                "key": productkey["Key"],
                "vendor": {"_a": "Datacore"},
            }
            licenses.append(license_data)

            if productkey["ServerId"]:
                cls.license_name_per_serverid[productkey["ServerId"]] = license_data["name"]
            else:
                nonserver_license_name = license_data["name"]
        
        data = {
            "_c": "VDiskCluster",
            "name": f'Datacore {obj["Caption"]}' + (f' {context.arg}' if context.arg else ''),
            "_r_for_datacore_servergroup": licenses,
            "datacore_servergroup": {
                "uuid": UUID(obj["Id"]),
                "license_capacity": as_gib(obj["LicenseSettings"]["StorageCapacity"]["Value"]), # The maximum storage allowed.
                "license_used": as_gib(obj["StorageUsed"]["Value"]), #	The amount of storage used that counts toward the group license storage limit.
            },
            "_a": f'servergroup:{obj["Id"]}', # define alias
        }

        if nonserver_license_name:
            data["datacore_servergroup"]["license"] = {"_c": "License", "name": nonserver_license_name}

        return data
        

    def collect(self):
        data = {
            "_c": "VM" if self.obj["IsVirtualMachine"] else "Server",
            "name": self.obj["Caption"],
            "cluster": {"_a": f'servergroup:{self.obj["GroupId"]}'}, # use alias
            "memory": as_gib(self.obj['TotalSystemMemory']['Value']),
            "cpu_product": {"_c": "Product", "name": self.obj['ProcessorInfo']['ProcessorName']},
            "product": {"_c": "Product", "name": f'{self.obj["ProductName"]} {self.obj["ProductType"]}', "vendor": {"_a": "Datacore"}, "_a": f'productof:{self.obj["Id"]}'},
            "product_version": f'{self.obj["ProductName"]} (build {self.obj["ProductBuild"]})',
            "license": {
                "_c": "License",
                "name": self.license_name_per_serverid[self.obj["Id"]] if self.obj["Id"] in self.license_name_per_serverid else f'Datacore {self.obj["LicenseNumber"]}',
                "num": self.obj["LicenseNumber"],
                "product": {"_a": f'productof:{self.obj["Id"]}'}
            },
            "datacore_server": {
                "uuid": UUID(self.obj["Id"]),
            }
        }
        
        # TODO: do this through rules
        if m := re.match(r'^Microsoft (?P<product>Windows Server) (?P<version>.+) (?P<edition>Standard|Enterprise), Build (?P<build>.+)$', self.obj['OsVersion']):
            data["os"] = {"_c": "Product", "name": f'{m["product"]} {m["edition"]}', "vendor": {"_a": "Microsoft"}}
            data["os_version"] = f'{m["version"]} (build {m["build"]})'
        else:
            data["os"] = self.obj['OsVersion']

        data["datacore_server"]["raw"] = {
            #TODO: sort it
            'HostName': self.obj['HostName'],
            'IpAddresses': self.obj['IpAddresses'],
            'State': ServerState(self.obj['State']),
            'NumberPhysicalCores': self.obj['ProcessorInfo']['NumberPhysicalCores'],
            'NumberCores': self.obj['ProcessorInfo']['NumberCores'],
            'AvailableSystemMemory': as_gib(self.obj['AvailableSystemMemory']['Value']),
            #TODO 'DiskPools': [d for d in sorted(server_diskpools, key=lambda d: d.obj['Caption'])],
            #TODO 'PhysicalDisks': [PhysicalDisk(disk) for disk in sorted(self.obj['PhysicalDisks'], key=lambda data: data['Caption'])],
            #TODO 'VirtualDisks': sorted(server_virtualdisks, key=lambda d: d.caption),
            #TODO: ports
        }

        return data


class ServerState(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_ServerState
    NotPresent = 0
    Offline = 1
    Online = 2
    Failed = 3
