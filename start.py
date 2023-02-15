import asyncio
from groups import get_groups
from posts import get_posts
import time
from asyncio import Semaphore
from data import create_file
from comments import get_comments


async def start() -> None:

    semaphore = Semaphore(5)  # ограничение на 5 запросов за раз

    groups = await get_groups()  # получаем список групп пользователя

    posts_from_group = await asyncio.gather(*[get_posts(o, semaphore) for o in groups])  # n постов к каждой группе

    await asyncio.gather(*[get_comments(post, semaphore) for posts in posts_from_group for post in posts])


if __name__ == '__main__':

    create_file()

    s = time.time()
    asyncio.run(start())
    print(f'Время работы: {time.time()-s}')
