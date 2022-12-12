from typing import Union

import httpx
from lxml.etree import HTML
from urllib.parse import urljoin


REL_LIST = ('icon', 'shortcut icon')


def from_html(text: str) -> Union[str, None]:
    tree = HTML(text)
    for e in tree.cssselect('link'):
        if 'href' not in e.attrib:
            continue
        if not e.attrib.get('rel') in REL_LIST:
            continue
        return e.attrib['href']
    return None


def from_url(url: str, default='/favicon.ico', **kw) -> Union[str, None]:
    link = from_html(httpx.get(url, **kw).text)
    if link is None:
        link = default
    if link is None:
        return None

    if link.startswith('data:image'):
        return link
    else:
        return urljoin(url, link)
