from flask import Flask, request, Response
from getfavicon import get_favicon_link, get_favicon_blob

from config import config
from store import get_store


app = Flask(__name__)
store = get_store()


async def get_favicon(url):
    if store.exists(url):
        blob = store.get(url)
    else:
        kw = {
            'proxies': {'all://': 'http://127.0.0.1:7890'}
        }
        icon_url = await get_favicon_link(url, **kw)
        print(icon_url)
        blob = await get_favicon_blob(icon_url, **kw)
        store.set(url, blob)

    if not blob:
        return Response(status=404)
    else:
        return Response(blob, content_type='image/png')


@app.route('/')
async def root():
    url = request.args.get('url')
    if url is None:
        return Response(status=400)
    else:
        return await get_favicon(url)


if __name__ == '__main__':
    app.run(debug=True)