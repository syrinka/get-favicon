Just a simple service to get website's favicon.

Will only return the first legal favicon, so if multiple favicons are defined, it may return unexpected result.

## Usage

- `poetry install`
- `flask run`
- `curl http://127.0.0.1:5000/?url=...`

### In prod environment

**Linux**

- `poetry install --with=prod`
- `gunicorn app:app`

**Windows**

- `poetry install --with=prod-win`
- `waitresss-serve app:app`

## Configurations

- `STORE: Literal['memory', 'redis', 'filecache'] = 'memory'`
    - `memory`: Caches are stored in memory, will be flushed when restarted
    - `reids`: Caches are stored in given Redis
    - `filecache`: Caches are stored as files in `cache/`, will stay existed until manual delete it
- `LRU_SIZE: int = 100` *Not yet Implemented*
- `REDIS_URL: str`
- `REDIS_TTL: int`
- `REQUEST_KW: dict` Additional params to be passed to `httpx.get`，in json format
