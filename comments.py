import aiohttp
import asyncio
from asyncio import Semaphore
from vk_api import VK_TOKEN
from size_photo import max_size
from data import write_file


async def get_comments(post: dict, semaphore: Semaphore):

    async with aiohttp.ClientSession(trust_env=True) as session:

        async with semaphore:

            if post is not None and len(post) > 0:

                url = f"https://api.vk.com/method/wall.getComments?owner_id={post['group']}&post_id={post['post_id']}&count=100&need_likes=1&sort=asc&access_token={VK_TOKEN}&v=5.131"
                req = await session.get(url)
                src = await req.json()

                await asyncio.sleep(2)

        if 'response' in src:
            all_comments = src['response']['items']

            for comm in all_comments:

                if 'attachments' not in comm:

                    if 'p_att' not in post:
                        write_file(owner_id=post['group'], post_id=post['post_id'], p_date=post['p_date'], p_text=post['p_text'],
                                   comm_id=comm['id'], c_text=comm['text'], c_like=comm['thread']['count'])
                    else:
                        write_file(owner_id=post['group'], post_id=post['post_id'], p_date=post['p_date'], p_text=post['p_text'], p_att=post['p_att'],
                                   comm_id=comm['id'], c_text=comm['text'], c_like=comm['thread']['count'])

                elif len(comm['attachments']) == 1 and comm['attachments'][0]['type'] == 'photo':

                    if 'p_att' not in post:
                        write_file(owner_id=post['group'], post_id=post['post_id'], p_date=post['p_date'], p_text=post['p_text'],
                                   comm_id=comm['id'], c_text=comm['text'], c_att=max_size(comm['attachments'][0]['photo']['sizes']), c_like=comm['thread']['count'])

                    else:
                        write_file(owner_id=post['group'], post_id=post['post_id'], p_date=post['p_date'], p_text=post['p_text'], p_att=post['p_att'],
                                   comm_id=comm['id'], c_text=comm['text'], c_att=max_size(comm['attachments'][0]['photo']['sizes']), c_like=comm['thread']['count'])

        else:
            pass
