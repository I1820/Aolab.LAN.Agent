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


class Log:
    '''
    The I1820Log object contains information that is used to
    report end device states into I1820 platform.
    :param type: type of target end device.
    :type kind: str
    :param device: identification of target end device.
    :type device: str
    :param states: states of target device in the list format.
    :type states: list
    '''
    def __init__(self, kind: str, device: str,
                 states: list,
                 timestamp: datetime.datetime = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()

        self.states = dict()
        for state in states:
            if 'name' not in state or 'value' not in state:
                raise ValueError(
                    'states must be an array of names and values.')
            else:
                self.states[state['name']] = state['value']

        self.kind = kind
        self.device = device
        self.timestamp = timestamp

    def to_json(self):
        result = {
                'timestamp': self.timestamp.timestamp(),
                'kind': self.kind,
                'device': self.device,
                'states': self.states,
        }
        return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        states = []
        for key, value in raw_values['states'].items():
            states += {'name': key, 'value': value}
        kind = raw_values['kind']
        device = raw_values['device']
        timestamp = datetime.datetime.fromtimestamp(
            raw_values['timestamp'])
        return cls(kind, device, states, timestamp)
