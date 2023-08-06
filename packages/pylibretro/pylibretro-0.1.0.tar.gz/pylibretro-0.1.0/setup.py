# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylibretro']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0']

setup_kwargs = {
    'name': 'pylibretro',
    'version': '0.1.0',
    'description': 'WIP Python library that runs Libretro cores',
    'long_description': '# pylibretro\n\n⚠️ This library is currently (and probably will remain) in a **severe pre-alpha state**. At the moment it is however able to load the 2048 core, press buttons and get screen output (as you can see below!). However, many callbacks and functions aren\'t handled, other cores (such as the PCSX ReARMed core) segfault etc. Use at your peril.\n\n![](2048example.gif)\n\n## Installation\n`pip install pylibretro`\n\n(the only dependency is [Pillow](https://pypi.org/project/Pillow/) if you wish to install it manually)\n\n## Usage\nYou can create the GIF shown above by using the [example file](example.py) in this repository. However, here\'s a condensed, minimal usage example:\n\n```python\nfrom pylibretro import Core, buttons\n\nlastframe = None\n\ndef on_frame(frame):\n    global lastframe\n    lastframe = frame\n\n# Load the core\ncore = Core("./2048_libretro.so")\ncore.on_video_refresh = on_frame\ncore.retro_init()\ncore.retro_load_game(None)\n\n# Start a 2048 game (by pressing the START button for one frame)\ncore.joystick[buttons.START] = True\ncore.retro_run()\ncore.joystick[buttons.START] = False\n\n# Run core for 10 frames\nfor i in range(10):\n    core.retro_run()\n\n# Show the last screen output\nlastframe.show()\n```\n\n## Licenses\npylibretro is licensed under [AGPLv3 or later](LICENSE.md).\n\nCredits to Rob Loach for [noarch](https://github.com/RobLoach/noarch) (which indicated how to call Libretro\'s API), the RetroArch team for [Libretro](https://www.libretro.com/index.php/api/) itself and also the [2048 core](https://github.com/libretro/libretro-2048) included within this repository as an example. Their corresponding licenses are also included in the license file.\n',
    'author': 'James Ravindran',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesravi/pylibretro',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
