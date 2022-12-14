from typing import Union, Tuple
from base64 import b64decode

import httpx
from lxml.etree import HTML


REL_LIST = ('icon', 'shortcut icon')


def get_href(html: str) -> Union[Tuple[str, Union[str, None]], Tuple[None, None]]:
    tree = HTML(html)
    for e in tree.cssselect('link'):
        if 'href' not in e.attrib:
            continue
        if e.attrib.get('rel') in REL_LIST:
            return e.attrib['href'], e.attrib.get('type')
    return None, None


async def get_favicon(url, **kw) -> Union[Tuple[bytes, str], None]:
    """
    :rtype: (bytes, str) | favicon blob and its mimetype
    :rtype: None | if favicon resource not found
    """
    resp = httpx.get(url, **kw)
    base_url = resp.url
    href, mime = get_href(resp.text)
    if href is None:
        href = '/favicon.ico'
    if mime == 'image/vnd.microsoft.icon':
        mime = 'image/x-icon'

    if href.startswith('data:image'):
        assert mime
        b64 = href, mime.split(',', 1)[1]
        blob = b64decode(b64)

    else:
        link = base_url.join(href)
        async with httpx.AsyncClient(**kw) as client:
            resp = await client.get(link)
            if resp.status_code == 200:
                blob = resp.content
            else:
                return None
            if mime is None:
                mime = resp.headers['content-type'] or 'image/png'

    return blob, mime
