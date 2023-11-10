import httpx

from imagehost.exceptions import SourceTypeInvalid, ApiError


class ImageHost:
    def __init__(self, api_key: str):
        """
        :param api_key: Your api key, which can be obtained at https://freeimage.host/page/api
        """
        self.api_key = api_key

    async def upload(self, source: str, source_type='path') -> dict:
        """
        :param source_type: The image type, pass "path" (it is already standard) for an image path, pass "b64" for an
        image base64 string and pass "url" for an image url.
        :param source: The image can be a url, a base64 string
        or a path. :return: A dictionary containing various information about the image that was sent and the link
        itself.
        """

        api_key = self.api_key
        api = 'https://freeimage.host/api/1/upload'

        cl = httpx.AsyncClient()

        if source_type == 'path':
            with open(source, 'rb') as file:
                source = file.read()
            req = await cl.post(
                api,
                data={
                    'key': api_key,
                    'format': 'json'
                },
                files={'source': source},
                timeout=None
            )
        elif source_type == 'b64' or source_type == 'url':
            req = await cl.post(
                api,
                data={
                    'key': api_key,
                    'source': source,
                    'format': 'json'
                }
            )
        else:
            await cl.aclose()
            raise SourceTypeInvalid

        await cl.aclose()

        if req.status_code != 200:
            req_json = req.json()
            raise ApiError(
                req_json['error']['message'],
                req_json['status_code']
            )
        else:
            return req.json()
