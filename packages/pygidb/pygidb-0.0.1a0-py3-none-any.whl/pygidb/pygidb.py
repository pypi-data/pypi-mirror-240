from aiohttp import ClientSession
from pygidb.constants import DEFAULT_QUERY, DEFAULT_RESULT
from urllib.parse import urlencode

from pygidb.types.api import Response
from pygidb.types.characters import Character


class GenshinDBException(Exception):
    def __init__(self, error_text, error_code):
        super().__init__(error_text)
        self.message = error_text
        self.code = error_code


class GenshinDBOptions:
    def __init__(self, query=DEFAULT_QUERY, result=DEFAULT_RESULT):
        self._query_languages = query
        self._result_language: str = result

    def to_dict(self):
        return {
            'query_languages': ','.join(self._query_languages),
            'result_language': self._result_language
            }


class GenshinDB:
    def __init__(self, options=None):
        self.options = options
        if not self.options:
            self.options = GenshinDBOptions()

        self.client = ClientSession()
        self.base_url = 'https://gidb.nix13.pw'

    def __del__(self):
        pass

    async def __request(self, folder: str, query: str, **kwargs) -> Response:
        params = urlencode({**self.options.to_dict(), **kwargs})
        async with self.client.get(f'{self.base_url}/{folder}/{query}?{params}') as r:
            json = await r.json()
            res = Response(**json)
            if res.error:
                raise GenshinDBException(**res.response)
            return res

    async def get_characters(self) -> dict[str, list[str]]:
        res = await self.__request('characters', '')
        return res.response[0]

    async def get_character(
        self, name: str, images=False, stats=False, url=False
    ) -> Character:
        res = await self.__request('characters', name, images=images,
                                   stats=stats, url=url)
        return Character(**res.response)
