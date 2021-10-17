import asyncio


async def sample():
    print("before sleep")
    await asyncio.sleep(1)
    print("after sleep")
    return 69  # while :)


async def do_tests():
    future = await sample()
    print(future, type(future))


asyncio.run(do_tests())
