class MyHashMap:

    def __init__(self):
        self.key_set = set()
        self.keys = []
        self.vals = []

    def put(self, key: int, value: int) -> None:
        if key not in self.key_set:
            self.key_set.add(key)
            self.keys.append(key)
            self.vals.append(value)
        else:
            idx = self.keys.index(key)
            self.vals[idx] = value

    def get(self, key: int) -> int:
        if key in self.key_set:
            idx = self.keys.index(key)
            return self.vals[idx]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.key_set:
            self.key_set.remove(key)
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.vals[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)