from enum import Enum, Flag
import logging
from uuid import UUID
from cmdbase_utils import normalize_hwaddress
from .commons import Context, Entity

logger = logging.getLogger(__name__)


class Port(Entity): #TODO: merge with host and server?
    def collect(self):
        if self.obj['HostId']:
            if self.obj.get('ServerPortProperties'):
                host_obj = self.context.get_cached_obj('servers', self.obj['HostId'])
                host = {"_c": "Server", "_k": "datacore_server.uuid", "name": host_obj['Caption'], "datacore_server": {"uuid": UUID(host_obj['Id'])}}
            else:
                host_obj = self.context.get_cached_obj('hosts', self.obj['HostId'])
                host = {"_c": "Host", "_k": "datacore_host.ref", "name": host_obj['Caption'], "datacore_host": {"ref": f"{self.context.refprefix}host-{host_obj['Id']}"}}
        else:
            host = None

        data = {
            'Id': self.obj['Id'],
            'ExtendedCaption': self.obj['ExtendedCaption'],
            'host': host,
            'connected': self.obj.get('Connected'),
            'hwaddress': normalize_hwaddress(self.obj['PhysicalName']) if 'PhysicalName' in self.obj else normalize_hwaddress(self.obj['PortName']),
            'type': ScsiPortType(self.obj.get('PortType')),
            'mode': ScsiMode(self.obj.get('PortMode')),
            'role': PortRole(self.obj['ServerPortProperties']['Role']) if 'ServerPortProperties' in self.obj else None,

        }
    
        if 'PortId' in self.obj:
            data['PortId'] = self.obj.get('PortId')
        elif 'StateInfo' in self.obj and 'PortId' in self.obj['StateInfo']:
            data['PortId'] = self.obj['StateInfo']['PortId']
        else:
            data['PortId'] = None

        data['PortName'] = self.obj.get('PortName')

        return data


class ScsiPortType(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_ScsiPortType
    Unknown = 0
    SCSI = 1
    FibreChannel = 2
    iSCSI = 3
    Loopback = 4
    

class ScsiMode(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_ScsiMode
    NonSCSI = 0
    Initiator = 1
    Target = 2
    InitiatorTarget = 3
    Unknown = 4


class PortRole(Flag):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_PortRole
    NoRole = 0
    Frontend = 1
    Backend = 2
    Mirror = 4
    All = 7
