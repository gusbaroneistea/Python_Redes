import asyncio
from websockets.asyncio.server import serve

async def responder(websocket):

    async for mensaje in websocket:

        print("Mensaje recibido:", mensaje)

        await websocket.send("Recibí: " + mensaje)

async def main():

    async with serve(responder, "localhost", 8765):

        print("Servidor esperando conexiones...")

        await asyncio.Future()

asyncio.run(main())