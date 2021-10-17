import asyncio
import time


async def sample(msg1, msg2, delayed):
    print("Entered", delayed)
    await asyncio.sleep(1)
    print(msg1)
    await asyncio.sleep(delayed)
    print(msg2)


async def this():
    task_1 = asyncio.create_task(sample("Test1~", "Test1", 4))
    task_2 = asyncio.create_task(sample("Test2~", "Test2", 2))
    # first create all tasks and then use await since awaiting for a task immeditaly starts the loop
    await task_1
    await task_2


async def bad_this():
    await asyncio.create_task(sample("Test1~", "Test1", 4))
    await asyncio.create_task(sample("Test2~", "Test2", 2))
    # same as the sync process if the tasks are properly scheduled.


tok = time.time()
asyncio.run(this())
print(time.time() - tok)
tok = time.time()
asyncio.run(bad_this())
print(time.time() - tok)

# yeah bad way to note time, but this is fast and dirty
