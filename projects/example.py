#!/usr/bin/env python3

from i1820 import App, Notification

import time

# dev_eui = '0000000000000074'
dev_eui = 'device_identification'

token = 'device_token'
# token = 'aQtfclhd-RfHEKFNYT1SNodJtu0CGHcrZcORCU-cKOE='

app = App(dev_eui, token, '127.0.0.1')


@app.notification('lamp', 'alarm', 'smartLamp')
def lamp_notification(data: Notification):
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
