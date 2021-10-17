import asyncio
import threading


async def sample(delay):
    await asyncio.sleep(delay)
    print(threading.currentThread())


def start(delay):
    asyncio.run(sample(delay))  # high level API


threading.Thread(target=start, args=(3, )).start()
start(2)
# use asyncio.run() if we are satisfied with this
# if used in different thread, new event loop is created
