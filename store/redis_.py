from redis import Redis
from config import config


class RedisStore(object):
    conn: Redis

    def __init__(self) -> None:
        self.conn = Redis.from_url(config.redis_url)

    def get(self, key):
        return self.conn.get(key)

    def set(self, key, value):
        self.conn.set(key, value, ex=config.redis_ttl)

    def exists(self, key):
        return self.conn.exists(key)