from nonebot import on_command, CommandSession


@on_command('music')
async def music(session: CommandSession):
    # query = session.current_arg_text.strip()
    # if not query:
    #     query = "色图"
    # query_pic = await get_pic(query)
    await session.send({
        "type": "music",
        "data": {
            "type": "163",
            "id": "28949129"
        }
    })
