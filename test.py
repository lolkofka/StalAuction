from stalApi import stalApi
import asyncio

exemplar = stalApi(client_id = 30, client_secret = '0SmJSabjQrtShTfwVkNXADLdQiehMGRwyPxZmOYf')


async def main():
    await exemplar.run()
    regions = await exemplar.get_regions()
    print(regions)
    await exemplar.close()

asyncio.run(main())