class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {}
        self.freq_list = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1

        node = self.key_node[key]
        self.touc(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self.touc(node)
            return

        if len(self.key_node) == self.capacity:
            evict_key, _ = self.freq_list[self.min_freq].popitem(last=False)
            del self.key_node[evict_key]

        self.min_freq = 1
        new_node = Node(key, value)
        self.key_node[key] = new_node
        self.freq_list[1][key] = new_node

    def touc(self, node: Node):
        prev = node.freq
        cur = prev + 1
        node.freq = cur

        del self.freq_list[prev][node.key]
        if not self.freq_list[prev]:
            del self.freq_list[prev]
            if prev == self.min_freq:
                self.min_freq += 1

        self.freq_list[cur][node.key] = node