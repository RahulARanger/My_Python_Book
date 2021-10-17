import asyncio


async def sample_this(code, sleep=False):
    # now task: 1 enters with sleep = True
    if sleep:
        await asyncio.sleep(0)
        # even tho it doesn't sleep, but the control of the program is transferred to the loop
        # which it calls the task: 2

    # task: 2 enters without sleep, since there's no await it doesn't return to the loop before printing
    print(code)  # prints the things we need
    # return or return None or another await brings the control to the tasks


async def do_tests():
    await asyncio.gather(sample_this("#1", True), sample_this("#2"))
    # every time we do this thing, somethings is added to event loop
    # here two tasks are added
    # so asyncio's default loop (which is dirty and not recommended to use for big things)
    # considers that it needs to two this tasks cleverly and efficiently


asyncio.run(do_tests())
