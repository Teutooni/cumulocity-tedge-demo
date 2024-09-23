import urllib.request
import json
import paho.mqtt.publish as publish
import asyncio
import contextlib
import logging
from aiohue import HueBridgeV2
from aiohue.v2.models.resource import ResourceTypes

hueip = "192.168.1.37"
huetoken = "<your token here>"

async def main():
        async with HueBridgeV2(hueip, huetoken) as bridge:
                print("Connected to bridge: ", bridge.bridge_id)

                def handle_event(event_type, item):
                        if item.type == ResourceTypes.MOTION:
                                time = item.motion.motion_report.changed.isoformat()
                                motion = 1 if item.motion.motion_report.motion else 0
                                
                                measurement = json.dumps({'time': time, 'motion': motion})
                                
                                result = publish.single("te/device/main///m/sensors", measurement)

                bridge.subscribe(handle_event)

                await asyncio.Future() # sleep forever, listening to events


with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
