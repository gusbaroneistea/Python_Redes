import asyncio
import aiohttp

async def main():

    async with aiohttp.ClientSession() as sesion:

        async with sesion.get(
            "https://jsonplaceholder.typicode.com/todos/1"
        ) as respuesta:

            datos = await respuesta.json()

            print("Código:", respuesta.status)
            print("Título:", datos["title"])


asyncio.run(main())
