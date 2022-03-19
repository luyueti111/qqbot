import json
import os
import re

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


import requests_html

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}


def get_cover(bv):
    Catch = requests.get(url=bv, headers=headers)
    Cover_url = re.findall('rel="apple-touch-icon" href="(.*?)@57w_57h_1c.png"', Catch.text)[0]
    bs0up = bs4.BeautifulSoup(Catch.content, "lxml")
    up = bs0up.find_all('a', {"class": "username"})[0]
    intro = bs0up.find_all('span', {"class": "desc-info-text"})
    if not intro:
        intro.text = '暂无介绍'
    return Cover_url, up.text.strip(), intro.text.strip()


async def get_video_info(query):
    url = 'https://search.bilibili.com/all?keyword={}'.format(query)
    req = requests_html.HTMLSession()
    responses = req.get(url, headers=headers)
    bsp = bs4.BeautifulSoup(responses.content, "lxml")
    tlt = bsp.find_all('a', {"class": "img-anchor"})[0]

    href = 'https://' + tlt.attrs['href'][2:]

    title = tlt.attrs['title']
    cover, content, intro = get_cover(href)
    return href, title, content, cover

