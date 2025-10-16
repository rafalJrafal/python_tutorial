import asyncio
import time

async def task(name, delay):
    print(f"task {name} started")
    await asyncio.sleep(delay)
    print(f"task {name} done")


async def main():
    await asyncio.gather(task("X", 3), task("Y", 1), task("Z", 2))

asyncio.run(main())