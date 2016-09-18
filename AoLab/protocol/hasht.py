# In The Name Of God
# ========================================
# [] File Name : hasht.py
#
# [] Creation Date : 18-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import AoLabSerialProtocol
from ..domain.message import AoLabThingMessage


class HashtProtocol(AoLabSerialProtocol):

    thing_types = {
        't': 'temperature',
        'l': 'light',
        'h': 'humidity',
        'm': 'motion'
    }

    def handler(self, message: str) -> AoLabThingMessage:
        parts = message.split(',')
        node = parts[0][1:]
        battery = parts[-1][:-1]
        things = []
        for thing in parts[1:-1]:
            things.append({
                'type': self.thing_types[thing[0]],
                'value': thing[2:],
                'device': thing[1]
            })
        return AoLabThingMessage(node, battery, *things)