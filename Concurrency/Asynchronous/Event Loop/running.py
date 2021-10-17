import asyncio
import threading


async def sample():
    ...


loop = asyncio.get_event_loop()
loop.create_connection()

print("stopped")  # won't come here unless stopped manually
