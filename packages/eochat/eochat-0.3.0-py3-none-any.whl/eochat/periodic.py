import eochat.builder
import time
import asyncio

def get_now():
    return time.time_ns() // 1000000

async def iping(conn):
    while True:
        await asyncio.sleep(5)
        await conn.send(eochat.builder.ping(get_now()))
