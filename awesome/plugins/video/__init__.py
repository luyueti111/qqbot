from nonebot import on_command, CommandSession

from .data_source import get_video_info


@on_command('video')
async def video(session: CommandSession):
    query = session.current_arg_text.strip()
    if not query:
        query = "一生所爱"

    url, title, content, cover = await get_video_info(query)
    with open("/Users/luyueti/Desktop/code/qqbot/awesome/plugins/video/temp_json.txt", "r") as f:
        xml = f.read().format(title, url, cover, url, title, content)

    await session.send({
        "type": "xml",
        "data": {
            "data": xml
        }
    })
