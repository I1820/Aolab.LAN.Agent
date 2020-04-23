# In The Name Of God
# ========================================
# [] File Name : I1820App.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .domain.log import Log
from .domain.notif import Notification
from .errors import I1820Exception

import paho.mqtt.client as mqtt
import logging
import asyncio
import threading
import re
import base64
import json
import typing

i1820_logger_app = logging.getLogger('I1820.app')

dev_eui_regex = re.compile(r'[a-fA-f0-9]{16}')

class App:
    def __init__(self, dev_eui: str, token: str, mqtt_ip: str,
                 mqtt_port: int = 1883, logger=None):
        # MQTT Up and Running
        self.client = mqtt.Client()
        self.client.connect(mqtt_ip, mqtt_port)
        self.client.on_connect = self._on_connect

        # Device Identification
        if dev_eui_regex.fullmatch(dev_eui) is None:
            raise I1820Exception("invalid device eui")
        self.dev_eui = dev_eui

        # Token
        self.token = token

        # Notification/Action handlers
        self.notification_handlers: typing.Dict[str, typing.Callable[[Notification], None]] = {}

        # Event loop
        self.loop = asyncio.new_event_loop()

        if logger is None:
            self.logger = i1820_logger_app

    def run(self):
        print(" * Node ID: %s" % self.dev_eui)
        t = threading.Thread(target=self._run)
        t.daemon = True
        t.start()

    def _run(self):
        asyncio.set_event_loop(self.loop)
        self._loop()
        try:
            self.loop.run_forever()
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            self.loop.close()

    def notification(self, *things: typing.List[str]):
        def _notification(fn):
            for thing in things:
                self.notification_handlers[thing] = fn
            return fn
        return _notification

    def log(self, type, device, states):
        log = Log(type, device, states)
        data = {
            'data': base64.b64encode(
                log.to_json().encode('ascii')).decode('ascii'),
            'token': self.token,
        }
        self.logger.info('log: %s' % data)
        self.client.publish('log/%s/send' % self.dev_eui,
                            json.dumps(data))

    def _loop(self):
        self.client.loop()
        self.loop.call_soon(self._loop)

    def _on_connect(self, client, userdata, flags, rc):
        self.logger.info("MQTT connection is here")
        client.subscribe('notification/%s/request' % self.dev_eui)
        client.message_callback_add('notification/%s/request' %
                                    self.dev_eui, self._on_notification)

    def _on_notification(self, client, userdata, message):
        data = json.loads(message.payload.decode('ascii'))
        notif = Notification.from_json(base64.b64decode(
            data['data']
        ))

        try:
            self.notification_handlers[notif.type](notif)
            self.logger.info('device: %s -- settings: %r' %
                             (notif.device, notif.settings))
        except KeyError:
            pass
