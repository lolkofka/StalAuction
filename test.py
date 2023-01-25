from stalApi import stalApi
from config import client_id, client_secret
import asyncio

exemplar = stalApi(client_id = client_id, client_secret = client_secret)


async def main():
    await exemplar.run()
    regions = await exemplar.get_regions()
    print(exemplar.appToken)
    print(regions)
    await exemplar.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())