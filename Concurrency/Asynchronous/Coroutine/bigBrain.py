import asyncio
import time


# of course, by big brain i refer to the ppl who created asynchronous process

async def sample(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def this():
    task_1 = asyncio.create_task(sample(3, "Test 1"))
    task_2 = asyncio.create_task(sample(2, "Test 2"))
    print(task_1)
    print(task_2)

    await task_1
    print("bruh")
    # note this won't be printed even tho it's test2's statement printed first,
    # flow is decided internally in the event loop
    # for now we are gonna use the simple and dirty event loop
    # some of this are predictions of mine so as to understand this for myself well. Please correct me if i am wrong.
    await task_2


"""
We can we get "Test2" printed before the "Test1"
This is because we are sleeping for 3 seconds we do task2 where we sleep for 2 seconds, since we got no other, 
"""

tok = time.time()
asyncio.run(this())
print(time.time() - tok)  # see we saved time
