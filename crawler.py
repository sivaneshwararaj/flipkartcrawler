import asyncio
from aiohttp import ClientSession
import settings
import helper as help

def save_resposne(responses):
    for markup in responses:
        product_name,price,url=help.extract_values(markup)
        help.extract_save_data(product_name,price,url)


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()

async def run():
    tasks = []
    with open(settings.start_file,"r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # skip blank and commented out lines
            async with ClientSession() as session:
                task = asyncio.ensure_future(fetch(line, session))
                tasks.append(task)
                responses = await asyncio.gather(*tasks)
                save_resposne(responses)





loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)
loop.close()