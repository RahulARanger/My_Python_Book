import asyncio


async def wht():
    print("Hello")
    await asyncio.sleep(1)
    print("There")


print(wht)

# we are not supposed to call the coroutine as it is
print(wht())  # coroutine + warning

asyncio.run(wht())  # we need to pass the coroutine
