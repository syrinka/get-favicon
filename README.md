## Usage

- `poetry install`
- `flask run`
- `curl http://127.0.0.1:5000/?url=...`

### In prod environment

- `poetry install --with=prod` / `poetry install --with=prod-win`
- `gunicorn app:app` / `waitresss-serve app:app`

## Configurations

- `STORE: Literal['memory', 'redis', 'filecache'] = 'memory'`
- `LRU_SIZE: int = 100`
- `REDIS_URL: str`
- `REDIS_TTL: int`
- `REQUEST_KW: dict` # in json format
