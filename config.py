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
