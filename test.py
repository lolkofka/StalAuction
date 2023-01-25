from stalApi import stalApi
from config import client_id, client_secret
import asyncio

print(client_id, client_secret)
exemplar = stalApi(client_id = client_id, client_secret = client_secret)


async def main():
    await exemplar.run()
    regions = await exemplar.get_regions()
    # print(exemplar.appToken)
    item_history = await exemplar.get_auction_history('y1q9', regions[0]['id'], True)
    print(item_history)
    await exemplar.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())