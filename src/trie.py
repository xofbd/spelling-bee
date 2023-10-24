class Trie:
    def __init__(self, size, data=None):
        self.size = size
        self.array = [None] * self.size
        self.data = data

    def __getitem__(self, key):
        return self._get(key, index=0)

    def _get(self, sequence, index=0):
        if len(sequence) == index:
            return self.data if self is not None else None

        node = self.array[sequence[index]]

        if node is not None:
            return node._get(sequence, index=index+1)
        else:
            return None

    def get(self, key, default=None):
        val = self.__getitem__(key)

        return val if val is not None else default

    def __setitem__(self, key, val):
        self._set(key, val, index=0)

    def _set(self, sequence, val, index=0):
        if len(sequence) == index:
            self.data = val
            return

        node = self.array[sequence[index]]

        if node is not None:
            node._set(sequence, val, index=index+1)
        else:
            node = Trie(self.size)
            self.array[sequence[index]] = node
            node._set(sequence, val, index+1)


class CharTrie(Trie):
    def __init__(self, data):
        self.alphabet_size = 26
        super().__init__(self.alphabet_size, data=data)

    def __getitem__(self, key):
        indices = [self.calc_index(s) for s in key]

        return super().__getitem__(indices)

    def __setitem__(self, key, val):
        indices = [self.calc_index(s) for s in key]
        super()._set(indices, val, index=0)

    @staticmethod
    def calc_index(key):
        return ord(key.lower()) - ord("a")
