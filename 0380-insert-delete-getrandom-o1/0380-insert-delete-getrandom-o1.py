class RandomizedSet:

    def __init__(self):
        self._list = []
        self._pos_by_val = {}

    def insert(self, val: int) -> bool:
        if val in self._pos_by_val:
            return False

        self._pos_by_val[val] = len(self._list)
        self._list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self._pos_by_val:
            return False
            
        val_pos = self._pos_by_val[val]
        last_val = self._list[-1]
        if val == last_val:
            del self._pos_by_val[val]
        else:
            self._list[val_pos] = last_val
            del self._pos_by_val[val]
            self._pos_by_val[last_val] = val_pos
        
        self._list.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()