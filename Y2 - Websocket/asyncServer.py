import asyncio
from asyncServerData import *

from websockets.asyncio.server import serve

async def run(websocket):
    async for message in websocket:
        print(f"server side message = {message}")
        await websocket.send(f"{message} from server")

async def main():
    async with serve(run, server_address, server_port) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())