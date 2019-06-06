#!/usr/bin/env python3

from I1820.app import I1820App
from I1820.domain.notif import I1820Notification

import time

# dev_eui = '0000000000000074'
dev_eui = 'device_identification'

token = 'device_token'
# token = 'A5evk1nK7uu_867mP3eqyePcNPIqfKVg8gcf7iMJ6_4='

app = I1820App(dev_eui, token, '127.0.0.1')


@app.notification('lamp', 'alarm', 'smartLamp')
def lamp_notification(data: I1820Notification):
    return True


if __name__ == '__main__':
    app.run()
    temperature = 10
    light = 1
    motion = 1
    while True:
        temperature = (temperature + 10) % 100
        light = light / 2 if light >= 128 else light * 2
        motion = 0 if motion == 1 else 1

        states = []
        states.append({
            'name': 'temperature',
            'value': str(temperature)
        })
        states.append({
            'name': 'light',
            'value': str(light)
        })
        states.append({
            'name': 'motion',
            'value': str(motion)
        })
        states.append({
            'name': 'humidity',
            'value': '24'
        })

        app.log('multisensor', '1', states)
        time.sleep(5)
