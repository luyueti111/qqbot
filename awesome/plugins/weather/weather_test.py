import pandas as pd
import requests

city = "运城市"
city_df = pd.read_excel("AMap_adcode_citycode_20210406.xlsx")
print(city_df)

temp = city_df[city_df.apply(lambda x: city in x["中文名"], 1)]
print(temp.iat[0, 1])
exit()

r = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?",
                 params={"key": "f313e065ec610ab761eee51a81fcadb2",
                         "city": "110101",
                         "extensions": "all"})
weather_info = r.json()
weather_info = weather_info["forecasts"][0]["casts"][0]
weather_detail = "今天的日期是{}, 周{}, 白天天气{}, 夜晚天气{}, 白天平均温度{}，夜晚平均温度{}, 白天风向{}, 晚上风向{}, " \
                 "白天风力{}, 晚上风力{}".format(*list(weather_info.values()))
print(weather_detail)

