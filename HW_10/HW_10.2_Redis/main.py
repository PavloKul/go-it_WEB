import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f():
    x = 'Redis in progress'
    print(x)
    return x


f()

