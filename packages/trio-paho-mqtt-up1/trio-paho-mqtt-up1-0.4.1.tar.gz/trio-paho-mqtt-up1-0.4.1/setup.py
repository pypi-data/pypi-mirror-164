# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trio_paho_mqtt']

package_data = \
{'': ['*']}

install_requires = \
['paho-mqtt>=1.6.1,<2.0.0', 'trio>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'trio-paho-mqtt-up1',
    'version': '0.4.1',
    'description': 'MQTT support for the Trio async runtime using Paho (update fork)',
    'long_description': "# trio_paho_mqtt\n[trio](https://github.com/python-trio/trio) specific async MQTT client. The goal of this project is to have all \nthe MQTT protocol stuff handled by [paho-mqtt](https://github.com/eclipse/paho.mqtt.python),\nwhile the async loopy stuff is handled by trio. This keeps our MQTT communication async, without having to\nshove paho-mqtt into a thread, and without having to reimplement the MQTT protocol.\n\nAll callbacks are also removed to be more trio-like. Messages are accessed through an `async for` loop.\n\nThis is meant to be a light-as-possible wrapper around paho-mqtt. That way if something goes wrong with MQTT message\nparsing, it's not my fault ;-)\n\n## Usage\nFirst, see the `example.py` and paho-mqtt documentation.\nThe goal is to expose all the same methods as the paho-mqtt `Client`. If any methods (besides callbacks) are missing\nor do something unexpected, this is a bug. Please open an issue.\n\n`AsyncClient` is initialized with a sync `mqtt.Client` and a `trio.Nursery` but then otherwise should operate much\nlike the sync `Client`.  Methods are *not* coroutines, they are non-blocking functions, so you do not need to call\n`await`. The only exception is accessing messages through `async for`.\n\n### Example\n\nPlease see `example.py` for a working example!\n(example in README removed because it was not working)\n\n\n## Related projects\n  - [gmqtt](https://github.com/wialon/gmqtt) - Uses asyncio and callbacks. Isn't compatible with trio.\n  - [hbmqtt](https://github.com/beerfactory/hbmqtt) - Uses asyncio. Reimplements the MQTT protocol.\n  - [aiomqtt](https://github.com/mossblaser/aiomqtt) - Uses asyncio and wraps paho, but still uses the loop from \n  paho-mqtt. I believe all operations are put into a worker thread.\n  - [distmqtt](https://github.com/smurfix/distmqtt) - anyio-ified hbmqtt fork. Works with trio.\n  - [asyncio-mqtt](https://github.com/sbtinstruments/asyncio-mqtt) - Same idea as this lib (a light wrapper for paho mqtt), but for asyncio. \n",
    'author': 'Olivier (fork)',
    'author_email': 'triopahomqtt.python@librepush.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
