from flask import Flask, request, Response
from getfavicon import get_favicon

from config import config
from store import get_store


app = Flask(__name__)
store = get_store()


async def get(url):
    if store.exists(url):
        data = store.get(url)
        mime, blob = data[:13].rstrip().decode(), data[13:]
    else:
        kw = {
            'proxies': {'all://': 'http://127.0.0.1:7890'}
        }
        blob, mime = await get_favicon(url, **kw)

        # image/gif
        # image/png
        # image/x-icon
        # image/svg+xml
        data = mime.encode().ljust(13) + blob
        store.set(url, data)

    if not blob:
        return Response(status=404)
    else:
        return Response(blob, content_type=mime, mimetype=mime)


@app.route('/')
async def root():
    url = request.args.get('url')
    if url is None:
        return Response(status=400)
    else:
        return await get(url)


if __name__ == '__main__':
    app.run(debug=True)