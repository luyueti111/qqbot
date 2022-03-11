import os

from nonebot import on_command, CommandSession
import json
from random import sample
from .funcs import is_legal, get_word, get_end_py


__plugin_name__ = '成语接龙'
__plugin_usage__ = "/game  [开始词/成语]"


@on_command('game', aliases=('games', "成语接龙"))
async def game(session: CommandSession):
    word_from_user = session.current_arg_text.strip()
    with open("{}/awesome/plugins/idiom/idiom.json".format(os.getcwd()), "r") as f:
        data = json.load(f)

    if not word_from_user:
        word_from_bot = sample(data, 1)[0]
        info = "我先开始啦！{}".format(word_from_bot['word'])
        word_from_user = (await session.aget(prompt=info)).strip()
    else:
        word_from_bot = None

    while True:
        is_lg, msg = await is_legal(word_from_user, word_from_bot)
        if not is_lg:
            message = msg
            break
        else:
            word_from_bot, is_win = await get_word(word_from_user)
            if not is_win:
                message = "你赢了，找不到以{}开头的词".format((await get_end_py(word_from_user)))
                break
            else:
                info = word_from_bot['word']
                word_from_user = (await session.aget(prompt=info)).strip()

    await session.send(message)
