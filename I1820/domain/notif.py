# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 19-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class I1820Notification:
    '''
    The I1820Notification object contains information that is used to
    send notification into end devices.
    :param type: type of target end device.
    :type type: str
    :param device: identification of target end device.
    :type device: str
    :param settings: configurations wanted to apply on target end device.
    :type settings: dict
    '''
    def __init__(self, kind: str, device: str,
                 settings: dict):
        self.type = kind
        self.device = device
        self.settings = settings

    def to_json(self):
            result = {
                'kind': self.kind,
                'device': self.device,
                'settings': self.settings,
            }
            return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        kind = raw_values['kind']
        device = raw_values['device']
        settings = raw_values['settings']
        return cls(kind, device, settings)
