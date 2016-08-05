# SimpleCache
Simple file based cache using `pickle` module.

## Usage
```sh
$ cd your_repo
$ git submodule add https://github.com/cprn/simplecache.git
```

```python
#!/usr/bin/python3
from simplecache.cache import PickleCache

timeout_seconds = 30
cache = PickleCache('test.cache', timeout_seconds)

try:
    data_id = 123
    costly_data = cache.get(data_id)
    print("Loaded from cache!")
except KeyError:
    print("Data not in cache or to old, caching...")
    costly_data = {
            "this": "data",
            "is": "very expensive to get otherwise",
            }
    cache.add(123, costly_data)
    cache.save()

print(costly_data['is'])
```

## Behavior
First run:
```sh
Cache empty...
Data not in cache or to old, caching...
very expensive to get otherwise
```

Second run before timeout:
```sh
Cache loaded...
Loaded from cache!
very expensive to get otherwise
```

Second run after timeout:
```sh
Cache loaded...
Data not in cache or to old, caching...
very expensive to get otherwise
```
