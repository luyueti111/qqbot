import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

q = "刘墉"
driver = webdriver.Chrome()
url = "https://search.bilibili.com/all?keyword={}".format(q)
driver.get(url)
# i = input()
#
# with open('cookies.txt', 'w') as f:
#     f.write(json.dumps(driver.get_cookies()))
#
# exit()
driver.delete_all_cookies()
with open('cookies.txt', 'r') as cookief:
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)
video_card = driver.find_element(by=By.XPATH, value='//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/a')
print(video_card.text)
print(video_card.get_attribute("href"))
print(video_card.get_attribute("title"))

cover = driver.find_element(by=By.XPATH, value="//*[@id=\"all-list\"]/div[1]/div[2]/ul/li[1]/div/div[3]/span[4]/a")
print(cover.text)