from django.core.cache import cache
from search.models import Username

REDIS_KEY_PREFIX = "user"

def _make_key(username):
    return f"{REDIS_KEY_PREFIX}:{username}"

def is_username_cached(username):
    key = _make_key(username)
    value = cache.get(key)
    print(f"Checking Redis: {key=} value={value}")
    return value  # Will return None if not cached

def get_username_from_db(username):
    exists = Username.objects.filter(name=username).exists()
    return exists

def cache_username(username, taken, timeout=3600):
    key = _make_key(username)
    cache.set(key, int(taken), timeout=timeout)
    print(f"Caching: {key=} taken={taken}")
