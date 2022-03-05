import requests
from bs4 import BeautifulSoup
from random import sample
url = 'https://www.google.com.hk/search?q=测试&tbm=isch'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
imgs = soup.find_all('img')

imgs = [img for img in imgs if "src" in img.attrs]
imgs = [img for img in imgs if "https" in img.attrs["src"]]
imgs = sample(imgs, 1)

print(imgs)


exit()
print(imgs[5].attrs["src"])