from environs import Env


__all__ = [
    'store',
    'lru_size',
    'redis_url',
    'filecache_path'
]

e = Env()
e.read_env()

class config(object):
    store = e.str('STORE', 'memory')
    assert store in ('memory', 'redis', 'filecache')

    lru_size = e.int('LRU_SIZE', 100)
    redis_url = e.str('REDIS_URL', None)
    redis_ttl = e.int('REDIS_TTL', None)

    request_kw = e.json('REQUEST_KW', {})
