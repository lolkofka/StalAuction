import aiohttp


class stalApi:

    def __init__(self, client_id, client_secret, url="https://eapi.stalcraft.net/"):
        self.__api_url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.appToken = 'UnAuthorizated'
        self.authHeader = {"Authorization": f"Bearer {self.appToken}"}
        self.session = aiohttp.ClientSession()


    async def __request_get(self, endpoint, headers = None, apiUrl = None):
        apiUrl = apiUrl if apiUrl else self.__api_url
        url = apiUrl+endpoint
        print(url)
        async with self.session.post(url, params = headers) as resp:
            r = await resp.json()
        return r


    async def get_regions(self):
        endpoint = 'regions'
        r = await self.__request_get(endpoint, self.authHeader)
        return r


    async def get_auction_history(self, region, item_id):
        endpoint = f'{region}/auction/{item_id}/history'
        r = await self.__request_get(endpoint, self.authHeader)
        return r


    async def run(self):
        endpoint = 'oauth/token'
        headers = {
            "client_id": str(self.client_id), 
            "client_secret": self.client_secret, 
            "grant_type": "client_credentials"
            }
        r = await self.__request_get(endpoint, headers, apiUrl = 'https://exbo.net/')
        self.appToken = r.get('access_token')
        return r


    async def close(self):
        await self.session.close()