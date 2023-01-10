class Node:
    
    def __init__(self, key, val, freq, next = None, prev = None):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = next
        self.prev = prev
        
class Frequency:
    
    def __init__(self):
        self.head = Node(-1,-1,-1)
        self.tail = Node(inf, inf, inf, prev = self.head)
        self.head.next = self.tail
        self.dic = {}
        self.frequency = {}
    
    def insert_last(self, node):
        cur = self.tail
        node.prev = cur.prev
        cur.prev.next = node
        cur.prev = node
        node.next = cur
        
        self.dic[node.key] = node
        if node.freq in self.frequency:
            self.frequency[node.freq].append(node)
        else:
            self.frequency[node.freq] = [node]

            
    def remove(self, node):
        del self.dic[node.key]
        
        self.frequency[node.freq].remove(node)
        if not self.frequency[node.freq]:
            del self.frequency[node.freq]
        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        
    def update(self, node):
        self.frequency[node.freq].remove(node)
        if not self.frequency[node.freq]:
            del self.frequency[node.freq]
        
        node.freq += 1
        if node.freq in self.frequency:
            self.frequency[node.freq].append(node)
        else:
            self.frequency[node.freq] = [node]
        
        self.remove(node)
        self.insert_last(node)
        
    def less_frequent(self) -> Node:
        freq = 1
        node = None
        while not node:
            if freq in self.frequency:
                node = self.frequency[freq][0]
            freq += 1
        
        return node
        
    def get(self, key) -> Node:
        return self.dic[key]
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.space = True
        if capacity == 0:
            self.space = False
        self.head = {}
        self.freq = Frequency()

    def get(self, key: int) -> int:
        if key not in self.head:
            return -1
        
        temp = self.freq.get(key)
        self.freq.update(temp)
        return self.head[key]

    def put(self, key: int, value: int) -> None:
        if not self.space:
            return
        
        if key in self.head:
            self.head[key] = value
            self.freq.update(self.freq.get(key))
        else:
            node = Node(key,value,1)
            if self.capacity:
                self.head[key] = value
                self.capacity -= 1
                self.freq.insert_last(node)
            else:
                temp = self.freq.less_frequent()
                self.freq.remove(temp)
                del self.head[temp.key]
                self.head[key] = value
                self.freq.insert_last(node)
                
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)