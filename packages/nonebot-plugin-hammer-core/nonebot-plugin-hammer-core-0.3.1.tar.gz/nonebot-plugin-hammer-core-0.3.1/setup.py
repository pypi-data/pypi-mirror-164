# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_hammer_core', 'nonebot_plugin_hammer_core.util']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-hammer-core',
    'version': '0.3.1',
    'description': 'core dependency of nonebot-plugin-hammer-xxx',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# Nonebot Plugin Hammer Core\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/ArgonarioD/nonebot-plugin-hammer-core/main/LICENSE">\n    <img src="https://img.shields.io/github/license/ArgonarioD/nonebot-plugin-hammer-core" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-hammer-core">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-hammer-core.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="python">\n  <img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">\n</p>\n\n\n## 介绍\n本仓库为nonebot-plugin-hammer-xxx等插件的核心依赖，其中主要内容为我本人（ArgonarioD）在开发nonebot2插件与bot时常用的轮子，本仓库在一般情况下不作为nonebot的插件而是作为插件的依赖库安装到nonebot的运行环境中\n\n## 已经实现的轮子\n - `util/constant.py` 常量\n - `util/message_factory.py` 快速构建消息（回复消息）\n - `util/onebot_utils.get_qq_nickname_with_group` 查找QQ群员昵称字符串格式化生成（对不在本群的群员查找昵称与对应群名并格式化生成）\n\n## 鸣谢\n - [onebot](https://github.com/botuniverse/onebot)\n - [nonebot2](https://github.com/nonebot/nonebot2)\n\n---\n~~*如果觉得有用的话求点个Star啵QwQ*~~',
    'author': 'ArgonarioD',
    'author_email': '739062975@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://docs.hammer-hfut.tk:233',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
