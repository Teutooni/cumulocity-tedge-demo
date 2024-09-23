# Monitoring script for Philips Hue motion sensor

Requires Python 3.10+ as it uses [aiohue](https://github.com/home-assistant-libs/aiohue) to listen for events on Hue bridge v2. Update hueip and huetoken accordingly.

Does one thing: triggers on Hue ResourceTypes.MOTION event and sends a "te/device/main///m/sensors" measurement to thin edge.

## Installation

MQTT: `pip install paho-mqtt`
Aiohue: 
* clone https://github.com/home-assistant-libs/aiohue
* go to aiohue folder and create setup.py file with contents: 
```
import setuptools
setuptools.setup()
```
* install aiohue `pip install .`

As always with python, might want to run in a venv or replace pip with version specific, i.e. pip3.10 if running multiple python versions.