
from enum import Enum
import logging
from .commons import Entity

logger = logging.getLogger(__name__)


class Host(Entity):
    def collect(self):
        data = {
            "_c": "Server",
            "name": self.obj["Caption"],
            "datacore_host": {
                "ref": f'{self.context.refprefix}{self.obj["Id"]}',
                "group": self.context.get_cached_obj('hostgroups', self.obj["HostGroupId"], default=None, prop='Caption'),
                'hostname': self.obj['HostName'],
                'type': ClientMachineType(self.obj['State']),
                'state': ClientState(self.obj['State']),
                #TODO: ports
            }
        }

        return data



class ClientState(Enum):
    # See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/RESTReferenceGuide.html#TypeDetails_ClientState
    Unknown	= 0
    NoPortConnection = 1
    PortsConnected = 2


class ClientMachineType(Enum):
    StorageServer =	0	# DataCore Server
    Windows	= 1	# Microsoft Windows (all other versions)
    HPUX = 2	# HP HPUX
    HPUX_8LUN = 3	# HP HPUX 8 LUNS
    Netware = 4	# Novell NETWARE
    AIX = 5	# IBM AIX with DataCore AP
    Solaris = 6	# Sun Solaris Legacy
    Irix = 7	# IRIX
    Linux = 8	# Linux (all other distributions)
    TRU64 = 9	# TRU64
    MAC_OS = 10	# Apple Mac OS
    WIN_AP_MPIO = 11	# Microsoft Windows with DataCore MPIO
    ESXi = 12	# VMware ESXi
    AIX_MPIO = 13	# IBM AIX Native MPIO Legacy
    CitrixXenServer = 14	# Citrix XenServer
    Virtual_Iron = 15	# Virtual Iron
    SolarisSanFoundation = 16	# Oracle (Sun) Solaris
    WindowsServer = 17	# Microsoft Windows (all other versions)
    AixMpioTL6Plus = 18	# IBM AIX
    SuseEnterpriseLinuxServer11 = 19	# Linux Suse Enterprise Server 11
    WindowsServer2012 = 20	# Microsoft Windows Server 2012 and Windows Server 2012 R2
