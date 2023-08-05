# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_gachalogs']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20.0,<1.0.0',
 'matplotlib>=3.5.1',
 'nonebot-adapter-onebot>=2.0.0b1',
 'nonebot2>=2.0.0a16',
 'xlsxwriter>=3.0.2']

setup_kwargs = {
    'name': 'nonebot-plugin-gachalogs',
    'version': '0.2.0',
    'description': 'A Genshin GachaLogs analysis plugin for Nonebot2',
    'long_description': '<h1 align="center">Nonebot Plugin GachaLogs</h1></br>\n\n\n<p align="center">🤖 用于统计及导出原神祈愿记录的 Nonebot2 插件</p></br>\n\n\n<p align="center">现已支持抽卡记录链接自动更新！</p></br>\n\n\n<p align="center">\n  <a href="https://github.com/monsterxcn/nonebot-plugin-gachalogs/actions">\n    <img src="https://img.shields.io/github/workflow/status/monsterxcn/nonebot-plugin-gachalogs/Build%20distributions?style=flat-square" alt="actions">\n  </a>\n  <a href="https://raw.githubusercontent.com/monsterxcn/nonebot-plugin-gachalogs/master/LICENSE">\n    <img src="https://img.shields.io/github/license/monsterxcn/nonebot-plugin-gachalogs?style=flat-square" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-gachalogs">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-gachalogs?style=flat-square" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.7.3+-blue?style=flat-square" alt="python"><br />\n</p></br>\n\n\n**安装方法**\n\n\n如果你正在使用 2.0.0.beta1 以上版本 NoneBot，推荐使用以下命令安装插件本体：\n\n\n```bash\n# 从 nb_cli 安装\npython3 -m nb plugins install nonebot-plugin-gachalogs\n\n# 或从 PyPI 安装\npython3 -m pip install nonebot-plugin-gachalogs\n```\n\n\n<details><summary><i>在 NoneBot 2.0.0.alpha16 上使用此插件</i></summary></br>\n\n\n在过时的 NoneBot 2.0.0.alpha16 可能仍有机会体验此插件！不过，千万不要通过 NoneBot 脚手架或 PyPI 安装，你只能通过 Git 手动安装。以下命令仅作参考：\n\n\n```bash\n# 进入 Bot 根目录\ncd /path/to/bot\n# 安装依赖\n# source venv/bin/activate\npython3 -m pip install matplotlib Pillow xlsxwriter\n# 安装插件\ngit clone https://github.com/monsterxcn/nonebot-plugin-gachalogs.git\ncd nonebot_plugin_gachalogs\ncp -r nonebot_plugin_gachalogs /path/to/bot/plugins/\ncp -r data/gachalogs /path/to/bot/data/\n```\n\n\n</details>\n\n\n一般来说，无需设置环境变量，只需重启 Bot 即可直接开始使用此插件。如果需要，你也可以在 Nonebot2 当前使用的 `.env` 文件中，参考 [.env.example](.env.example) 添加这些环境变量：\n\n\n - `gachalogs_safe_group` 安全群组，只有在安全群组内才允许输入链接、Cookie 等内容\n - `gacha_expire_sec` 祈愿历史记录本地缓存过期秒数，不设置默认 1 小时\n - `resources_dir` 包含 `gachalogs` 文件夹的上级目录路径，不设置默认 Bot 根目录下 `data` 文件夹\n - `gachalogs_font` 抽卡记录绘制使用字体，不设置默认为 `LXGW-Bold.ttf`\n - `gachalogs_pie_font` 抽卡记录饼图绘制使用字体，不设置默认为 `LXGW-Bold-minipie.ttf`\n\n\n\\* *私聊导出文件需要 go-cqhttp 支持 [相关接口](https://docs.go-cqhttp.org/api/#%E4%B8%8A%E4%BC%A0%E7%A7%81%E8%81%8A%E6%96%87%E4%BB%B6)*\n\n\n重启 Bot 即可体验此插件。\n\n\n**使用方法**\n\n\n插件支持以下命令：\n\n\n - `抽卡记录` / `ckjl`\n   \n   返回一张统计饼图，样式与 https://genshin.voderl.cn/ 一致。附带 `-f` / `--force` 可要求强制获取最新祈愿记录，祈愿记录结果默认缓存 1 小时。\n   \n   初次使用要求输入一次祈愿历史记录链接或米游社通行证 Cookie。如果初次使用输入链接（只要回复的内容中含有即可，不必手动截取准确的链接地址），在该链接的 AuthKey 过期（24 小时）后需要重新输入链接或 Cookie 才能刷新数据。如果初次使用输入 Cookie，只要 Cookie 有效，后续使用时抽卡记录链接将自动更新，无需再次输入。\n   \n   注意，Cookie 需要登陆 [米游社通行证](https://user.mihoyo.com/#/login/) 获取，而非 [米游社 BBS](https://bbs.mihoyo.com/)，其中需要包含 `stoken` `stuid` 或 `login_ticket`。\n   \n   ![祈愿统计图](data/readme/result.png)\n   \n - `抽卡记录导出` / `ckjldc`\n   \n   导出祈愿历史记录，默认导出为表格，可选格式包括 `excel` 表格、`json` 文件、`url` 链接等。此命令还可以附带 `cookie` 来导出当前绑定的米游社 Cookie，你可能在一些地方需要用到它。管理员可使用 `ckjldc [@某人] [格式]` 形式的命令导出指定 QQ 的祈愿历史记录。\n   \n   导出表格与 JSON 文件均符合 [统一可交换祈愿记录标准](https://github.com/DGP-Studio/Snap.Genshin/wiki/StandardFormat)（UIGF）格式，你可以尝试在其他支持此标准的工具中导入。导出链接可以在某些工具中使用。\n   \n   在不安全群组中使用此命令，Bot 会尝试通过私聊发送文件，如果未添加 Bot 为好友将无法发送导出内容。在环境变量中添加安全群组以允许群聊导出，如果大家并不在意安全隐患的话。插件已不再使用下图中的私聊发送文件方式，而是通过 go-cqhttp 提供的接口。\n   \n   ![导出示意图](data/readme/export.png)\n   \n - `抽卡记录删除` / `ckjlsc`\n   \n   删除本地缓存，不带任何参数默认删除自己的记录，可通过 @某人 的方式指定操作用户，可附带 `all` / `config` / `全部` / `配置` 将配置数据连同记录数据全部删除。非 Bot 管理员只能删除自己的数据。默认的删除只会删除记录数据，不会影响 Cookie 等配置数据。\n   \n   记录和配置一旦删除将无法恢复，所以此命令会要求重新发送附带 `-f` 的命令以确认操作。你也可以在第一次发送命令时就附带 `-f` 直接确认操作。\n\n\n**特别鸣谢**\n\n\n[@nonebot/nonebot2](https://github.com/nonebot/nonebot2/) | [@Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp) | [@sunfkny/genshin-gacha-export](https://github.com/sunfkny/genshin-gacha-export) | [@voderl/genshin-gacha-analyzer](https://github.com/voderl/genshin-gacha-analyzer)\n\n\n> 插件主要功能是从 [@sunfkny/genshin-gacha-export](https://github.com/sunfkny/genshin-gacha-export) 抄的，溜溜…\n',
    'author': 'monsterxcn',
    'author_email': 'monsterxcn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/monsterxcn/nonebot-plugin-gachalogs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0',
}


setup(**setup_kwargs)
