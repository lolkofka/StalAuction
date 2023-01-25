from stalApi import stalApi
import asyncio

exemplar = stalApi(client_id = 0, client_secret = 'tokentokentoken')


async def main():
    await exemplar.run()
    regions = await exemplar.get_regions()
    print(regions)
    await exemplar.close()

asyncio.run(main())