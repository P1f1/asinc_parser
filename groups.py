import asyncio
import aiohttp
from vk_api import VK_TOKEN, USER_ID


async def get_groups(url=f'https://api.vk.com/method/groups.get?user_id={USER_ID}&access_token={VK_TOKEN}&v=5.131') -> list:

    async with aiohttp.ClientSession() as session:

        req = await session.get(url)
        src = await req.json()

        groups_own = []

        for owner_id in src['response']['items']:

            groups_own.append(f'-{owner_id}')

        return groups_own


if __name__ == '__main__':
    pass
