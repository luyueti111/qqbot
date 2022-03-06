import sys

import nonebot
from nonebot import on_command, CommandSession
from prettytable import PrettyTable

__plugin_name__ = '获取帮助列表'
__plugin_usage__ = "/help"


@on_command('help', aliases=['使用帮助', '帮助', '使用方法'])
async def _(session: CommandSession):
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))
    table = PrettyTable(['名称', '用法'], encoding=sys.stdout.encoding)
    for index, p in enumerate(plugins):
        table.add_row([p.name, p.usage])
    table.align = 'r'
    table.padding_width = 4
    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send(table.get_string())
        return

    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)