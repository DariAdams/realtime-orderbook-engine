
import asyncio
import json

from websockets.asyncio.server import serve
from market_data.feed import generate_market_data


async def handle_client(websocket):
    async for event in generate_market_data():
        await websocket.send(json.dumps(event))


async def main():
    async with serve(handle_client, "localhost", 8765):
        print("WebSocket server running on localhost:8765", flush=True)
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
