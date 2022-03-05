import json
from random import sample

with open("/Users/luyueti/Desktop/code/qqbot/awesome/plugins/idiom/idiom.json", "r") as f:
    data = json.load(f)


async def is_legal(word_from_user, word_from_bot=None):
    word_from_user_in_db = [w for w in data if w['word'] == word_from_user]

    if not word_from_user_in_db:
        return False, "{}在词库中不存在".format(word_from_user)
    if word_from_bot is None:
        return True, ""

    end_py = word_from_bot['pinyin'].split(" ")[-1]
    st_py = word_from_user_in_db[0]['pinyin'].split(" ")[0]
    if end_py != st_py:
        return False, "{}和{}不匹配".format(end_py, st_py)

    return True, ""


async def get_word(word_from_user):
    word_in_db = [d for d in data if d["word"] == word_from_user]
    word_in_db = word_in_db[0]
    end_py = word_in_db['pinyin'].split(" ")[-1]
    q_word = [d for d in data if d['pinyin'].split(" ")[0] == end_py and d['word'] != word_from_user]
    if not q_word:
        return "", False
    else:
        return sample(q_word, 1)[0], True


async def get_end_py(word_from_user):
    word_in_db = [d for d in data if d["word"] == word_from_user]
    word_in_db = word_in_db[0]
    return word_in_db['pinyin'].split(" ")[-1]