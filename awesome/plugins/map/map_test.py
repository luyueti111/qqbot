import requests

ak = "LqrQ3TurNDKLGDC3X6xO1sclQeEqgEb8"
url = "https://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak={}".format(ak)

r = requests.get(url,
                 params={
                     "query": "美食",
                     "tag": "美食",
                     "regin": "北京",
                     "city_limit": True,
                     "output": "json",
                     "scope": 2,
                     "page_size": 20,
                     "photo_show": True,
                     "filter": "sort_name:overall_rating|sort_rule:0",
                     "ak": ak
                 })
print(r.json())
