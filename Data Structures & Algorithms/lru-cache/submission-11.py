# class ListNode:
class Node:
    def __init__(self, key, value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def removed(self,node):
        nxt, prev = node.next,node.prev
        prev.next , nxt.prev = nxt,prev
    def added(self,node):
        S = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev = S
        S.next = node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removed(node)
            self.added(node)
            return node.value
        
        return -1  

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            c = len(self.cache)
            neww = Node(key,value)
            if c <self.cap:
                self.cache[key] = neww
                self.added(neww)
                c+=1
            elif c == self.cap:
                old = self.head.next
                del self.cache[old.key]
                self.cache[key] = neww
                self.removed(old)
                self.added(neww)
                c+=1
        else:
            n = self.cache[key]
            self.removed(n)
            n.value = value
            del self.cache[key]
            self.cache[key] = n
            self.added(n)
            
            
