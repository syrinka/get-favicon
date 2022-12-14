## Usage

- `poetry install`
- `flask run`
- `curl http://127.0.0.1:5000/?url=...`

## 数据存储

通过环境变量 `STORE` 指定

### memory

存储在内存中，重启后数据清空

### redis

存储在 Redis 中，相关环境变量：`REDIS_URL`、`REDIS_TTL`

### filecache
