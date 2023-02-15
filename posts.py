from size_photo import max_size
import aiohttp
import asyncio
from asyncio import Semaphore
from vk_api import VK_TOKEN


async def get_posts(owner_id: int, semaphore: Semaphore) -> list:

    async with aiohttp.ClientSession(trust_env=True) as session:

        async with semaphore:

            url = f'https://api.vk.com/method/wall.get?owner_id={owner_id}&count=100&access_token={VK_TOKEN}&v=5.131'
            req = await session.get(url)
            src = await req.json()

            await asyncio.sleep(2)

        if 'response' in src:
            all_posts = src['response']['items']

            suit_post = []

            for post in all_posts:

                if len(post['attachments']) == 0:  # пост с <= 1 картинок
                    suit_post.append({"group": owner_id, "post_id": post['id'], "p_date": post['date'], "p_text": post['text']})

                elif len(post['attachments']) == 1 and post['attachments'][0]['type'] == 'photo':
                    suit_post.append({"group": owner_id, "post_id": post['id'], "p_date": post['date'], "p_text": post['text'], "p_att": max_size(post['attachments'][0]['photo']['sizes'])})

            return suit_post

        else:
            return []
