from hashlib import md5
from pathlib import Path


cache = Path(__file__).parent.parent / 'cache'

def get_path(key: str) -> Path:
    m = md5(key.encode()).hexdigest()
    return cache / m[:2] / m[2:4] / m[4:]


class FilecacheStore(object):
    def get(self, key):
        path = get_path(key)
        return path.read_bytes()

    def set(self, key, value):
        path = get_path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)

    def exists(self, key):
        path = get_path(key)
        return path.exists()
