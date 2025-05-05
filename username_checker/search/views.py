from django.http import JsonResponse
from .utils.redis_cache import is_username_cached, get_username_from_db, cache_username

def check_username(request):
    username = request.GET.get("username")
    if not username:
        return JsonResponse({"error": "Username is required"}, status=400)

    cached = is_username_cached(username)
    if cached is not None:
        return JsonResponse({"username": username, "taken": bool(int(cached)), "from": "redis"})

    taken = get_username_from_db(username)
    cache_username(username, taken)
    return JsonResponse({"username": username, "taken": taken, "from": "db"})
