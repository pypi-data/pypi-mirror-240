# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tailwind_cp']

package_data = \
{'': ['*']}

install_requires = \
['pyperclip>=1.8.2,<2.0.0', 'rich>=13.6.0,<14.0.0', 'textual>=0.41.0,<0.42.0']

entry_points = \
{'console_scripts': ['twcp = tailwind_cp.main:main']}

setup_kwargs = {
    'name': 'tailwind-color-picker',
    'version': '0.1.1',
    'description': 'TUI Application for browsing and copying Tailwind colors to the clipboard.',
    'long_description': "# Tailwind Color Picker\n\nThis tool displays the Tailwind color palette from which you can yank.\n\n![screenshot](twcp-screenshot.png)\n\nThe yanked color is hex with hash i.e. `#f8fafc`\n\n**Why?** I just like Tailwind colors and I like using them for things other than web development. This helps.\n\nColors are from the [Tailwind Documentation](https://tailwindcss.com/docs/customizing-colors\n).\n\n### Installation:\n\n```\npipx install tailwind-color-picker\n```\n\n### Usage:\n\nRun with `twcp`.\n\nBindings, etc:\n\n```\nj / down   - move cursor down\nk / up     - move cursor up\nh / left   - move cursor left\nl / right  - move cursor right\ny / enter  - yank (copy) the select color\nq / Ctrl+c - quit\n\nSelecting a color with the mouse will copy it, if you mouse.\n```\n\n### Other Information\n\nThis app was built using [Textual](https://textual.textualize.io/).\n\nThis currently yanks only the hex code. It's not really meant to generate the css class names that you would use if developing with Tailwind. But it could be a helpful preview of the default palette.\n",
    'author': 'Dan Cook',
    'author_email': 'cook.r.dan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/1dancook/tailwind-color-picker',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
