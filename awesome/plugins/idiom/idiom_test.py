import json
with open("/Users/luyueti/Desktop/code/qqbot/awesome/plugins/idiom/idiom.json", "r") as f:
    data = json.load(f)
get_word = "自作自受"

word_in_db = [d for d in data if d["word"] == get_word]
word_in_db = word_in_db[0]
end_py = word_in_db['pinyin'].split(" ")[-1]
q_word = [d for d in data if d['pinyin'].split(" ")[0] == end_py]
print(q_word)
