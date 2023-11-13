import logging
from .commons import Entity

logger = logging.getLogger(__name__)


class PortConnection(Entity): #TODO: merge with host and server?
    def collect(self):
        data = {
            'Id': self.obj.get('Id'),
            'Caption': self.obj.get('Caption'),
            'PortAId': self.obj.get('PortAId'),
            'PortBId': self.obj.get('PortBId'),
            'Connected': self.obj.get('Connected'),
            'Present': self.obj.get('Present', None),
        }

        return data

