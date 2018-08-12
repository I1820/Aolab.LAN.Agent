# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime
import json


class I1820Log:
    '''
    The I1820Log object contains information that is used to
    report end device states into I1820 platform.
    :param type: type of target end device.
    :type type: str
    :param device: identification of target end device.
    :type device: str
    :param states: states of target device.
    :type states: dict
    '''
    def __init__(self, type: str, device: str,
                 states: dict,
                 timestamp: datetime.datetime = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()

        self.states = states
        self.type = type
        self.device = device
        self.timestamp = timestamp

    def to_json(self):
        result = {
                'timestamp': self.timestamp.timestamp(),
                'type': self.type,
                'device': self.device,
                'states': self.states,
        }
        return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        states = raw_values['states']
        type = raw_values['type']
        device = raw_values['device']
        timestamp = datetime.datetime.fromtimestamp(
            raw_values['timestamp'])
        return cls(type, device, states, timestamp)
