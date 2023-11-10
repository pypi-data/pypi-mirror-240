# FreeImageHost

Unofficial wrapper for the freeimagehost website api

# Install
```bash
$ python3 -m pip install freeimagehost
```

## Example
```python
from imagehost import ImageHost

cl = ImageHost('api_key...')

#local image
image = cl.upload(
    'image.png'
)

#url image
image2 = cl.upload(
    'https://example.com/image.png',
    'url'
)

#base64 image
image3 = cl.upload(
    'b64 string...',
    'b64'
)

print(image['image']['url'])
print(image2['image']['url'])
print(image3['image']['url'])
```

## Asyncio Example
```python
import asyncio
from imagehost.aio import ImageHost

async def main():
    cl = ImageHost('api_key....')
    
    #local image
    image = await cl.upload(
        'image.png'
    )
    
    #url image
    image2 = await cl.upload(
        'https://example.com/image.png',
        'url'
    )
    
    #base64 image
    image3 = await cl.upload(
        'b64 string...',
        'b64'
    )
    
    print(image['image']['url'])
    print(image2['image']['url'])
    print(image3['image']['url'])


asyncio.run(main())
```