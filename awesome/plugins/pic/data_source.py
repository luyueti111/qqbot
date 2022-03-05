from aiocqhttp import MessageSegment
from bs4 import BeautifulSoup
import requests
from random import sample


async def get_pic(query: str):
    url = 'https://www.google.com.hk/search?q={}&tbm=isch'.format(query)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    imgs = soup.find_all('img')
    imgs = [img for img in imgs if "src" in img.attrs]
    imgs = [img for img in imgs if "https" in img.attrs["src"]]
    imgs = sample(imgs, 1)[0]
    # path = "/Users/luyueti/Desktop/code/qqbot/awesome/plugins/pic/Unknown.png"
    # with open(path, "rb") as f:
    #     image = f"base64://{base64.b64encode(f.read()).decode()}"
    query_pic = MessageSegment.image(imgs.attrs["src"])
    return query_pic
