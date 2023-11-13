from enum import Enum
import logging
import re
from uuid import UUID
from cmdbase_utils import as_gib
from .commons import Context, Entity

logger = logging.getLogger(__name__)


class VirtualDisk(Entity):
    @classmethod
    def collect_headers(cls, context: Context):
        cls._hosts_per_virtualdisk = cls._get_hosts_per_virtualdisk(context)
        

    def collect(self):
        hosts = self._hosts_per_virtualdisk.get(self.obj["Id"], [])

        data = {
            "_c": "VDisk",
            "name": self.obj["Caption"],
            'product': {"_c": "Product", "name": f"{self.obj['InquiryData']['Product']} {self.obj['InquiryData']['Revision']}", "vendor": {"_c": "Vendor", "name": self.obj['InquiryData']['Vendor']}},
            'serial': self.obj['InquiryData']['Serial'],
            'size': as_gib(self.obj['Size']['Value']),
            'allocated': as_gib(self.context.get_cached_perf('virtualdiskperformance', self.obj["Id"], prop='BytesAllocated')),
            "datacore_virtualdisk": {
                'ref': f'{self.context.refprefix}{self.obj["Id"]}',
                'hosts': [{"_c": "Server", "name": h['Caption']} for h in hosts],
                'hosts_summary': summarize_hosts([h['Caption'] for h in hosts]),
                'group': self.context.get_cached_obj('virtualdiskgroups', self.obj['VirtualDiskGroupId'], None, prop='Caption'),
                'type': VirtualDiskType(self.obj['Type']),
                'sub_type': VirtualDiskSubType(self.obj['SubType']),
                'storage_profile': self.context.get_cached_obj('storageprofiles', self.obj['StorageProfileId'], None, prop='Caption'),
                'recovery_priority': self.obj['RecoveryPriority'],
                'status': VirtualDiskStatus(self.obj['DiskStatus']),
                'is_served': self.obj['IsServed'],
                'scsi_device_id_string': self.obj['ScsiDeviceIdString'],
            }
        }

        return data


    @classmethod
    def _get_hosts_per_virtualdisk(cls, context: Context):
        results: dict[str,list[dict]] = {}

        for obj in context.get_with_retries('physicaldisks'):
            if 'VirtualDiskId' in obj:
                virtualdisk_id = obj['VirtualDiskId']
                host = context.get_cached_obj('hosts', obj['HostId'], None)
                # NOTE: HostId correspond en fait à Server (et donc host = None) pour les PhysicalDisk correspondant aux disques des serveurs et aux mirror trunks
                if host:
                    if virtualdisk_id in results:
                        vd_list = results[virtualdisk_id]
                    else:
                        vd_list = []
                        results[virtualdisk_id] = vd_list
                    vd_list.append(host)

        for host_names in results.values():
            host_names.sort(key=lambda h: h['Caption'])

        return results



class VirtualDiskType(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_VirtualDiskType
    NonMirrored = 0         # Single (non-mirrored) virtual disk created from a single storage source.
    MultiPathMirrored = 2   # Mirrored virtual disk created from two server storage sources.
    Dual = 3                # Dual virtual disk created from a single storage source shared by two servers.


class VirtualDiskSubType(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_VirtualDiskSubType
    Standard = 0	        # The standard virtual disk type.
    ProtocolEndpoint = 1	# A virtual disk used as a Protocol Endpoint.
    VVOL = 2	            # A virtual disk used as a VVOL which will be bound to a Protocol Endpoint.
    Trunk = 3               # An internal virtual disk used as a Trunk which directs mirror traffic.


class VirtualDiskStatus(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_VirtualDiskStatus
    Online = 0 # Online : Virtual disk is online and operating normally.
    Offline = 1 # Offline : Virtual disk is offline and unavailable.
    FailedRedundancy = 2 # Failed Redundancy : One storage source in a mirrored virtual disk is unavailable for mirroring.
    Failed = 3 # Failed : All storage sources in the virtual disk are unavailable and cannot be accessed.
    Unknown = 4 # Unknown: Virtual disk status is unknown and cannot be determined.


def summarize_hosts(hosts: list[str]):
    class CurrentHostSummary:
        def __init__(self, prefix: str, numlen: int, firstnum: int):
            self.prefix: str = prefix
            self.numlen: int = numlen
            self.firstnum: int = firstnum
            self.lastnum: int = firstnum

        @classmethod
        def parse(cls, name):
            m = re.search(r'[0-9]+$', name)
            if not m:
                return None
            numlen = len(m[0])
            prefix = name[0:-numlen]
            firstnum = int(m[0])
            return CurrentHostSummary(prefix, numlen, firstnum)

        def get_host_summary(self):
            if self.lastnum > self.firstnum:
                return f"{self.prefix}[{str(self.firstnum).rjust(self.numlen,'0')}-{str(self.lastnum).rjust(self.numlen,'0')}]"
            else:
                return f"{self.prefix}{str(self.lastnum).rjust(self.numlen,'0')}"

    host_summaries: list[str] = []
    current: CurrentHostSummary = None

    for host in sorted(hosts):
        if current:
            if host.startswith(current.prefix):
                if m := re.search('[0-9]{'+str(current.numlen)+'}$', host):
                    num = int(m[0])
                    if num == current.lastnum + 1:
                        current.lastnum += 1
                        continue
                        
            # End of current summary: we append it to list
            host_summaries.append(current.get_host_summary())

        # Determine if we have a new current summary
        current = CurrentHostSummary.parse(host)
        if not current:
            host_summaries.append(host)

    if current:
        host_summaries.append(current.get_host_summary())

    return host_summaries
