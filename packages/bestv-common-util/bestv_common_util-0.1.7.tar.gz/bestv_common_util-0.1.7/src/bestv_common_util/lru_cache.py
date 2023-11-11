import time
from datetime import datetime


class LRUCache:
    def __init__(self, capacity: int, cache_ttl_ms=-1, cache_empty=False):
        self.capacity = capacity
        self.cache = {}
        self.lru = []
        self.init_ms = LRUCache.current_ms()
        self.cache_ttl_ms = cache_ttl_ms
        self.cache_empty = cache_empty

    @staticmethod
    def current_ms():
        return round(time.time() * 1000)

    def get(self, key):
        if key not in self.cache:
            return
        value = self.cache[key]
        if value and isinstance(value, list):
            if self.cache_ttl_ms < 0:
                self.lru.remove(key)
                self.lru.append(key)
                return value[0]
            else:
                if LRUCache.current_ms() - self.init_ms - int(value[1]) > self.cache_ttl_ms:
                    del self.cache[key]
                    self.lru.remove(key)
                else:
                    self.lru.remove(key)
                    self.lru.append(key)
                    return value[0]

    def put(self, key, value) -> None:
        if self.cache_empty or value is not None:
            if key in self.cache:
                self.lru.remove(key)
            if len(self.cache) >= self.capacity:
                del self.cache[self.lru[0]]
                self.lru.pop(0)
            self.cache[key] = [value, LRUCache.current_ms() - self.init_ms]
            self.lru.append(key)



# print(time.monotonic())
# print(round(time.time() * 1000))
# # print(int(time.strftime("%f")))
# print(datetime.now().microsecond)
# print(int(datetime.now().strftime("%f")))
#
# lru_cache = LRUCache(15, 100000, cache_empty=True)
# lru_cache.put('key-none', 15)
# for i in range(10):
#     lru_cache.put(f'key-{i}', f'100 + {i}')
#     # time.sleep(1)
# lru_cache.put('key-none', None)
#
# print(lru_cache.get('key-3'))
# print(lru_cache.get('key-none'))
