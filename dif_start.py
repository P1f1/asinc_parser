import asyncio
import time
from asyncio import Semaphore
from data import create_file
from comments import get_comments
from dif_groups import get_domain, get_owner
from posts import get_posts


async def start():

    semaphore = Semaphore(5)

    domains = get_domain()  # получаем короткие названия групп из ссылок
    owner_id = await asyncio.gather(*[get_owner(d, semaphore) for d in domains])  # получаем owner_id групп

    posts_from_group = await asyncio.gather(*[get_posts(o, semaphore)for o in owner_id])

    await asyncio.gather(*[get_comments(post, semaphore) for posts in posts_from_group for post in posts])


if __name__ == '__main__':

    create_file()

    s = time.time()
    asyncio.run(start())
    print(f'Время работы: {time.time() - s}')
