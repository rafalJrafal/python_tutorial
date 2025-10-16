
import asyncio
from asyncServerData import *
from websockets.asyncio.client import connect

async def run():
    async with connect(f"ws://{server_address}:{server_port}") as websocket:
        for i in range(0,10000):
            await websocket.send(f"Hi {i}")
            message = await websocket.recv()
            print(message)

if __name__ == "__main__":
    asyncio.run(run())