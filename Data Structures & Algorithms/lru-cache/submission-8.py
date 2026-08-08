class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            valu = self.cache[key]
            L = self.cache.pop(key)
            self.cache[key] = valu
            return L
        
        return -1  

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            c = len(self.cache)
            if c <self.cap:
                self.cache[key] = value
                c+=1
            elif c == self.cap:
                index = 0
                key_to_pop = list(self.cache.keys())[index]
                self.cache.pop(key_to_pop)
                self.cache[key] = value
                c+=1
        else:
            L = self.cache.pop(key)
            self.cache[key] = value
            
