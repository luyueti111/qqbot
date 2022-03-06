from nonebot import on_request, RequestSession


@on_request('friend')
async def _(session: RequestSession):

    if 'lyt' in session.event.comment:
        await session.approve()
        return

    await session.reject('请说暗号')