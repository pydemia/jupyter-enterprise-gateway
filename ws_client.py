import asyncio
import websockets
async def connect():
    async with websockets.connect("ws://127.0.0.1:8081/") as websocket:
        await websocket.send("hello world")
        print(f"Reuqest headers:\n{websocket.request_headers}")
        response = await websocket.recv()
        print(f"Response headers:\n{websocket.response_headers}")
        print(response)
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())