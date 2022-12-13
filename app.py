import os

from flask import Flask, request, Response
from hashlib import md5
from pathlib import Path

from getfavicon import get_favicon_link, get_favicon_blob


app = Flask(__name__)

cache = Path(__file__).parent / 'cache'


def get_path(url: str) -> Path:
    m = md5(url.encode()).hexdigest()
    return cache / m[:2] / m[2:4] / m[4:]


async def get_favicon(url):
    path = get_path(url)
    if path.exists():
        blob = open(path, 'rb').read()
        return Response(blob, mimetype='image/png')

    kw = {
        'proxies': {'all://': 'http://127.0.0.1:7890'}
    }
    icon_url = await get_favicon_link(url, **kw)
    blob = await get_favicon_blob(icon_url, **kw)

    if not blob:
        return blob
    else:
        os.makedirs(path.parent, exist_ok=True)
        path.write_bytes(blob)
        return Response(blob, mimetype='image/png')


@app.route('/')
async def root():
    url = request.args.get('url')
    if url is None:
        return ''
    else:
        return await get_favicon(url)


if __name__ == '__main__':
    app.run()