from nonebot import on_command, CommandSession


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
