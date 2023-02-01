import asyncio
import websockets
async def handler(ws, path):
    data = await ws.recv()
    reply = f"Data received: {data}"
    await ws.send(reply)
if __name__ == "__main__":
    start_server = websockets.serve(handler, "127.0.0.1", 8081)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()