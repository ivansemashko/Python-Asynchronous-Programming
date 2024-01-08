import aiohttp
import asyncio
import time

start_time = time.time()


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 151):
            url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
            async with session.get(url) as response:
                pokemon = await response.json()
                print(pokemon['name'])


asyncio.run(main())
end_time = time.time()
print('Execution in seconds: ', int(end_time - start_time))
