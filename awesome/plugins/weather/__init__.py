from nonebot import on_command, CommandSession

from .data_source import get_weather_of_city


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
        while not city:
            city = (await session.aget(prompt='要查询的城市名称不能为空呢，请重新输入')).strip()
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)