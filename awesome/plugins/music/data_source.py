import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


async def get_song_id(song: str):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.set_capability(
        'unhandledPromptBehavior', 'accept')
    chrome_options.add_argument("--window-size=1920,1050")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(
        '--disable-software-rasterizer')  # 解决GL报错问题
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')  # 关闭声音
    chrome_options.add_argument('--window-position=700,0')
    chrome_options.add_argument('--log-level=3')

    driver = webdriver.Chrome(executable_path='{}/chromedriver-2'.format(os.getcwd()), chrome_options=chrome_options)


    url = "https://music.163.com/#/search/m/?s={}".format(song)
    driver.get(url)
    driver.delete_all_cookies()

    with open('{}/awesome/plugins/music/cookies.txt'.format(os.getcwd()), 'r') as cookief:
        cookieslist = json.load(cookief)
        for cookie in cookieslist:
            driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(1.5)
    driver.switch_to.frame(driver.find_element(by=By.ID, value="g_iframe"))
    time.sleep(1)

    song_id = driver.find_element(by=By.CLASS_NAME, value="text").find_element(By.XPATH, './*')
    href = song_id.get_attribute('href')
    song_id = href.split('id=')[1]
    driver.close()

    return song_id
