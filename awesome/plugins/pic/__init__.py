from nonebot import on_command, CommandSession

from .data_source import get_pic


@on_command('pic', aliases=('sexpic', '搜图', '涩图'))
async def pic(session: CommandSession):
    query = session.current_arg_text.strip()
    if not query:
        query = "色图"
    query_pic = await get_pic(query)
    await session.send(query_pic)
