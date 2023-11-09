import time


class Cache():

    async def save(self, key, value, expire=0):
        pass

    async def get(self, key):
        pass


class MemoryCache():
    def __init__(self):
        self.cache = {}

    async def save(self, key, value, expire=0):
        self.cache[key] = (value, time.time() + expire if expire > 0 else 0)

    async def get(self, key):
        value, expire = self.cache.get(key) or (None, 0)
        if value and expire > 0 and expire < time.time():
            self.cache.pop(key)
            return None
        return value
