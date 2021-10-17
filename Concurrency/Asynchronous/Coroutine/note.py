import asyncio
import time


def supply():
    yield sample("Test1~", "Test1", 4)
    yield sample("Test2~", "Test2", 2)


async def sample(msg1, msg2, delayed):
    print("Entered", delayed)  # see how other function starts before prev ends

    await asyncio.sleep(1)  # await passes the control to the event loop
    print(msg1)

    await asyncio.sleep(delayed)
    print(msg2)


async def this():
    tasks = [asyncio.create_task(_) for _ in supply()]
    await tasks[0]
    await tasks[1]
    # first create all tasks and then use await


async def bad_this():
    for _ in supply():
        await _  # here u are awaiting before creating all tasks


async def gather():
    await asyncio.gather(*supply())  # ease


def do_test(coroutine):
    tok = time.time()
    asyncio.run(coroutine)
    print("\"", coroutine.__name__, "\"", "took:", time.time() - tok)


do_test(this())
do_test(bad_this())
do_test(gather())
