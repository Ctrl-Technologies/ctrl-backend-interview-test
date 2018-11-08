# from .async_functions import async_functions
# from async
import asyncio
from .async_functions import method_one


async def run_functions_synchronous():
    result_list = []

    result_list.append(await method_one())
    return result_list


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop_result = loop.run_until_complete(run_functions_synchronous)
    # print(loop_result)
    # call async functions with eventloop
    pass

