class RandomizedSet:

    def __init__(self):
        self._list = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        self.val_to_idx[val] = len(self._list)
        self._list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
            
        val_idx = self.val_to_idx[val]
        last_val = self._list[-1]

        self.val_to_idx[last_val] = val_idx
        del self.val_to_idx[val]

        self._list[val_idx] = last_val
        self._list.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()