import asyncio
import json
from websockets.asyncio.server import serve

class WebSocketServer: 
    async def __init__(self, host='localhost', port=8765):
        self.server = await serve(self.send_data, host, port)


    async def send_data(self, websocket, data): 
        await websocket.send(json.dumps(data))