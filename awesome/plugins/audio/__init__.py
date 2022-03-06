from nonebot import on_command, CommandSession

__plugin_name__ = '语音'
__plugin_usage__ = r"""文字转语音
/audio  [信息]
"""


@on_command('audio')
async def audio(session: CommandSession):
    query = session.current_arg_text.strip()
    if not query:
        query = "芜湖起飞"

    await session.send({
        "type": "tts",
        "data": {
            "text": query
        }
    })
