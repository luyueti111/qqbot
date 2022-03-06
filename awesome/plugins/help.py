import nonebot
from nonebot import on_command, CommandSession

__plugin_name__ = '帮助'
__plugin_usage__ = r"""获取命令列表
/help
"""


@on_command('help', aliases=['使用帮助', '帮助', '使用方法'])
async def _(session: CommandSession):
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send(
            '支持的功能：\n\n' + '\n'.join(p.usage for p in plugins))
        return

    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)