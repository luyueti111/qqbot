import os

import pandas as pd
import requests


async def get_weather_of_city(city: str) -> str:
    city_df = pd.read_excel("{}/awesome/plugins/weather/AMap_adcode_citycode_20210406.xlsx".format(os.getcwd()))
    temp = city_df[city_df.apply(lambda x: city in x["中文名"], 1)]
    if len(temp) == 0:
        return "输入的城市不存在，请尝试使用更短的名称输入（如'运城市'改为'运城'）"

    city_code = temp.iat[0, 1]
    r = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?",
                     params={"key": "f313e065ec610ab761eee51a81fcadb2",
                             "city": city_code,
                             "extensions": "all"})
    weather_info = r.json()
    weather_info = weather_info["forecasts"][0]["casts"][0]
    weather_detail = "{}天气：白天天气{}, 夜晚天气{}, 白天平均温度{}，夜晚平均温度{}, 白天风向{}, 晚上风向{}, " \
                     "白天风力{}, 晚上风力{}".format(temp.iat[0, 0], *list(weather_info.values())[2:])
    return weather_detail
