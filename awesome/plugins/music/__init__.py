from nonebot import on_command, CommandSession

from .data_source import get_song_id

__plugin_name__ = '音乐搜素'
__plugin_usage__ = "/music  [关键词]"


@on_command('music')
async def music(session: CommandSession):
    query = session.current_arg_text.strip()
    if not query:
        query = "一生所爱"
    song_id = await get_song_id(query)
    await session.send({
        "type": "music",
        "data": {
            "type": "163",
            "id": song_id
        }
    })
