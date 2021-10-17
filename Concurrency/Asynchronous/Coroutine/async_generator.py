import asyncio


async def sample():
    for _ in range(10):
        yield _
        await asyncio.sleep(1)


async def do_test():
    # this is still a coroutine, not a generator print(sample())
    test = sample()

    print(test)
    async for _ in test:  # we use async for loop to handle async generator
        print(_)


async def do_manual():
    test = sample()


asyncio.run(do_test())
