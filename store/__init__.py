from config import config

def get_store():
    if config.store == 'memory':
        from .memory import MemoryStore
        return MemoryStore()
    if config.store == 'filecache':
        from .filecache import FilecacheStore
        return FilecacheStore()