import asyncio
from websockets.asyncio.client import connect

async def main():

    async with connect("ws://localhost:8765") as websocket:

        for numero in range(1, 4):

            mensaje = "Mensaje numero " + str(numero)

            await websocket.send(mensaje)

            respuesta = await websocket.recv()

            print("Servidor:", respuesta)

asyncio.run(main())
