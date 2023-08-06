# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simaple',
 'simaple.benchmark',
 'simaple.character',
 'simaple.core',
 'simaple.fetch',
 'simaple.fetch.application',
 'simaple.fetch.element',
 'simaple.fetch.element.character',
 'simaple.fetch.element.gear',
 'simaple.fetch.response',
 'simaple.fetch.translator',
 'simaple.fetch.translator.asset',
 'simaple.fetch.translator.kms',
 'simaple.gear',
 'simaple.gear.compute',
 'simaple.gear.improvements',
 'simaple.job',
 'simaple.job.builtin',
 'simaple.metric',
 'simaple.optimizer',
 'simaple.preset']

package_data = \
{'': ['*'],
 'simaple.benchmark': ['builtin/*', 'resources/*'],
 'simaple.gear': ['resources/*'],
 'simaple.job.builtin': ['resources/default_active_skill/*',
                         'resources/passive_skill/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'aiohttp>=3.8.1,<4.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'loguru>=0.5.3,<0.6.0',
 'numpy>=1.22.3,<2.0.0',
 'poethepoet>=0.10.0,<0.11.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.7.2,<2.0.0',
 'types-PyYAML>=6.0.4,<7.0.0']

setup_kwargs = {
    'name': 'simaple',
    'version': '0.0.0',
    'description': 'Maplestory calculation / Simulation library',
    'long_description': '# Simultion library for Maplestory\n\n- 메이플스토리에 관련된 다양한 연산을 지원하는 패키지.\n- Package for various calculation related with Maplestory.\n\n## Install\n- `pip install simaple`\n\n## Functions\n\n### 아이템 관련\n\n- 강화 수치 계산, 강화 수치 역연산\n- gear improvement calculation / derivation\n\n### 스텟 관련\n\n- 스텟 공격력 계산, 환산 주스텟 계산\n\n### 홈페이지 연동\n\n- 홈페이지 데이터 불러오기 기능\n\n\n## Examples\n\n### Hompage data fetch\n\n- Fetch\n```python\nfrom simaple.fetch.application.base import KMSFetchApplication\nfrom simaple.gear.slot_name import SlotName\n\napp = KMSFetchApplication()\n\ncharacter_response = app.run("Character-Name")\n```\n\n- Load Item information\n```python\nfrom simaple.fetch.application.base import KMSFetchApplication\nfrom simaple.gear.slot_name import SlotName\n\napp = KMSFetchApplication()\n\ncharacter_response = app.run("Character-Name")\ncap = character_response.get_item(SlotName.cap)\n\nprint(cap.show())\n```\n\n- Load raw-data for custom application\n\n```python\nfrom simaple.fetch.application.base import KMSFetchApplication\n\ncharacter_response = app.run("Character-Name")\nraw_data = character_response.get_raw()\n\nprint(raw_data)\n```\n',
    'author': 'meson324',
    'author_email': 'meson324@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/oleneyl/simaple',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
