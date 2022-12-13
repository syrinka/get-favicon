import os
from base64 import b64decode

import requests as rq
from flask import Flask, request, Response
from hashlib import md5
from pathlib import Path

from getfavicon import get_favicon_link


app = Flask(__name__)

cache = Path(__file__).parent / 'cache'


def get_path(url: str) -> Path:
    m = md5(url.encode()).hexdigest()
    return cache / m[:2] / m[2:4] / m[4:]


def get_favicon(url):
    path = get_path(url)
    if path.exists():
        blob = open(path, 'rb').read()
        return Response(blob, mimetype='image/png')

    icon_url = get_favicon_link(url, proxies={'all://': 'http://127.0.0.1:7890'})
    if icon_url.startswith('data:image'):
        b64 = icon_url.split(',', 1)[1]
        blob = b64decode(b64)

    else:
        resp = rq.get(icon_url)
        if resp.status_code == 200:
            blob = resp.content
        else:
            return ''

    os.makedirs(path.parent, exist_ok=True)
    path.write_bytes(blob)
    return Response(blob, mimetype='image/png')


@app.route('/')
def root():
    url = request.args.get('url')
    if url is None:
        return ''
    else:
        return get_favicon(url)


if __name__ == '__main__':
    app.run()