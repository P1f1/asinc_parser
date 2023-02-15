import asyncio
from asyncio import Semaphore
import aiohttp
from vk_api import VK_TOKEN


def get_domain() -> list:
    domains = []

    with open('links', 'r') as file:
        for line in file.readlines():
            domains.append(line[15:].strip())

    return domains


async def get_owner(domain: str, semaphore: Semaphore) -> int:

    async with aiohttp.ClientSession() as session:

        async with semaphore:
            req = await session.get(f'https://api.vk.com/method/wall.get?domain={domain}&count=10&access_token={VK_TOKEN}&v=5.131')
            src = await req.json()

            await asyncio.sleep(2)

        if 'response' in src:
            return src['response']['items'][0]['owner_id']


if __name__ == '__main__':
    pass
