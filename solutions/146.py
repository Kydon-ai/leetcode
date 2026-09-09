from __future__ import annotations
class LinkList:
    def __init__(self,key:int=0,value:int=0,next:LinkList | None=None,pre:LinkList | None=None):
        self.value = value
        self.key = key
        self.next = next
        self.pre = pre
    @classmethod
    def create_empty_link(cls):
        a,b = cls(),cls()
        a.next=b;a.pre=b
        b.next=a;b.pre=a
        return a,b

class LRUCache:
    def __init__(self, capacity: int):
        self.head,self.tail = LinkList.create_empty_link()
        self.capacity = capacity
        self.size = 0
        self.recoder = dict() #  int -> LinkList

    def get(self, key: int) -> int:
        node:LinkList|None = self.recoder.get(key,None)
        if node:
            self.remove_node(node)
            self.add_node(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        new_node = LinkList(key,value)
        old_node = self.recoder.get(key,None)
        if old_node:
            self.remove_node(old_node)
        self.add_node(new_node)

        if self.size > self.capacity:
            self.remove_node(self.tail.pre)
        

    def remove_node(self,head:LinkList) -> None:
        pre,next = head.pre,head.next
        pre.next = next
        next.pre = pre
        self.size -=1
        del self.recoder[head.key]
        del head
    
    def add_node(self,node:LinkList) ->None:
        pre,next = self.head,self.head.next
        pre.next = node;node.next=next
        next.pre = node;node.pre=pre
        self.size +=1
        self.recoder[node.key] = node


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

print("*"*20)
obj = LRUCache(1)
obj.put(2,1)
print(obj.get(2))
