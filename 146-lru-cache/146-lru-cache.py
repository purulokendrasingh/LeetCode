class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lrus = deque()
        self.c = capacity
        self.len = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lrus.remove(key)
            self.lrus.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lrus.remove(key)
            self.lrus.append(key)
        elif self.len < self.c:
            self.cache[key] = value
            self.lrus.append(key)
            self.len += 1
        else:
            temp = self.lrus.popleft()
            self.cache.pop(temp, None)
            self.cache[key] = value
            self.lrus.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)