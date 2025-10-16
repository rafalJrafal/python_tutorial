import asyncio

async def printAfterTimeout(text, timeout = 3):
    await asyncio.sleep(timeout)
    print(text)

async def main():
    await printAfterTimeout("ala", 4)
    await printAfterTimeout("ma kota", 2)

    task_a = asyncio.create_task(printAfterTimeout("ala", 3))
    task_b = asyncio.create_task(printAfterTimeout("ma", 4))
    task_c = asyncio.create_task(printAfterTimeout("kota", 6))

    await task_b
    await task_c
    await task_a

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(printAfterTimeout("hello", 1))
        tasl2 = tg.create_task(printAfterTimeout("world", 3))

asyncio.run(main())