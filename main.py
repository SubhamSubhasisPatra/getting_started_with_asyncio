import asyncio
from time import sleep


async def get_user_data():
    sleep(2)
    return {"name": "Subham", "age": 21}


async def sol():
    result = await get_user_data()
    return result


print(asyncio.run(sol()))
