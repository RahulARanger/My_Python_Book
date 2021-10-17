import asyncio


async def sample_1():
    print("sample_1")


async def sample_2():
    print("sample_2")


# sample_1 ans sample_2 coroutines are chained
async def chain_them():
    await sample_1()
    await sample_2()


asyncio.run(chain_them())
