import asyncio

async def main(name = "", timeout = 1):
    print(f"{name}: hello :)")
    await asyncio.sleep(timeout)
    print(f"{name}: bye :)")

with asyncio.Runner() as runner:
    runner.run(main("process A"))
    runner.run(main("process B"))