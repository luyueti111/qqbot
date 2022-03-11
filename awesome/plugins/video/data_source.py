import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


async def get_video_info(q: str):
    driver = webdriver.Chrome()
    url = "https://search.bilibili.com/all?keyword={}".format(q)
    driver.get(url)

    driver.delete_all_cookies()
    with open('{}/awesome/plugins/video/cookies.txt'.format(os.getcwd()), 'r') as cookief:
        cookieslist = json.load(cookief)
        for cookie in cookieslist:
            driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(3)

    rand = random.randint(1, 3)
    video_card = driver.find_element(by=By.XPATH,
                                     value='//*[@id="all-list"]/div[1]/div[2]/ul/li[{}]/a'.format(rand))
    url = video_card.get_attribute("href")
    url = url.split("?")[0]

    title = video_card.get_attribute("title")

    cover = driver.find_element(by=By.XPATH,
                                value="//*[@id=\"all-list\"]/div[1]/div[2]/ul/li[{}]/a/div/div[1]/img".format(rand))
    cover = cover.get_attribute("src")

    content = driver.find_element(by=By.XPATH,
                                  value="//*[@id=\"all-list\"]/div[1]/div[2]/ul/li[{}]/div/div[3]/span[4]/a".format(rand)).text
    content = "来自up:"+content
    driver.close()
    return url, title, content, cover
