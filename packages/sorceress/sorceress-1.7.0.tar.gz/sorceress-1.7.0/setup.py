# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sorceress']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sorceress',
    'version': '1.7.0',
    'description': 'Python package for creating optical illusions',
    'long_description': '# sorceress 1.7\n\n### Purpose of package\n\nThe purpose of this package is to provide creating optical illusions with simple way. Package written in Python however repo includes also JavaScript.\n\n### Getting started🚀️\n\nPackage can be found on pypi hence you can install it with using pip.\n\n```\npip install sorceress==1.7\n```\n\n```\n#importing\nimport sorceress\n#another way to import \nfrom sorceress import sorceress\n```\n\n### Features\n\n+ Illusions written in Python    **Illusions written in JavaScript**\n  - chromatic                   - footsteps\n  - dotill                      - thelilac\n  - realtimegrid                - EyeMovements\n  - addlines\n  - eyecolour\n  - dakinPex\n  - bruno\n  - dolboeuf\n  - kanizsa\n  - tAki2001\n  - cafewall\n  - ccob\n  - ebbinghaus\n  - whiteill\n  - enigma\n  - blackhole\n\n## Examples\n\nFor each function, I added example of how to use it. You can find them in the documentation. I will show just few examples.\n\nfrom sorcerer import sorcerer\nsorcerer.chromatic("myimage.jpg","outputname" ,circle=False, method="CMCCAT2000", gif=True, Gifduration=7)\nsorcerer.addlines("myimage.png","desiredoutputname",linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0))\n\nillusions that written in JavaScript can be found in the repo. You can find them in the folder called "js". You can run them in the browser or in the node.js.\n\n\n\n## Contribution\n\nAny contribution, bug report, suggestion is always welcome.\n\n##Author\n+ Main Maintainer: Enes Altun\n',
    'author': 'altunenes',
    'author_email': 'enesaltun2@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/altunenes/sorceress',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
