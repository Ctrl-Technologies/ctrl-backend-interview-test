from two_async.async_functions import method_one, method_two, method_four, method_three
import asyncio

async def main():

    """
    Question

    call async functions together and return in the order function_one, function_two, function_three, function_four.

    Many ways to call these async functions, extra points for good use of asyncio. Try and fire all at the same time
    and get the results together

    :return: None
    """
    result_list = []

    print(result_list)



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    """
    Question:
    Run main() method
    """
