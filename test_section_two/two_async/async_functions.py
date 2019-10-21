import asyncio
import aiohttp
import time


async def method_one():
    """
    A method that makes the task sleep
    :return: "method_one:done"
    """
    await asyncio.sleep(10)
    return "method_one:done"


async def method_two():
    """
    API Call to simulate network wait.
    :return:
    """
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    url = "http://bnb.data.bl.uk/doc/resource/007446989.json"
    start = time.time()
    async with aiohttp.ClientSession(loop=loop) as client:
        async with client.get(url) as response:
            assert response.status == 200
            await response.json()
            return "method_two: Time for API to respond = {}seconds".format((time.time() - start))


async def method_three():
    """
    Method just adds x + y over two for loops.
    :return:
    """
    results = []
    for x in range(0, 100):
        for y in range(0, 100):
            results.append(x+y)

    return "method_two: number of results = {}".format(len(results))


async def method_four(n=30):
    """
    Fibonacci numbers via recursion
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return await method_four(n - 1) + await method_four(n - 2)
