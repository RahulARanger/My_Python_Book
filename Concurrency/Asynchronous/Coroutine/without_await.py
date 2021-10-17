import asyncio

async def sample():
    print("this is also a coroutine")


async def do_test():
    await sample()


asyncio.run(sample())
asyncio.run(do_test())
