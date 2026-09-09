# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        count = 1
        p = self
        res = "["
        while p:
            res +=f"{p.val},"
            count +=1
            p = p.next
        return res + "]"
        
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) ->ListNode | None:
        if k==1:
            return head
        p0 = ListNode()
        p0.next = head
        pp = h = t = p = p0
        pre = pp
        pp = pp.next
        while pp:
            h = pp
            for i in range(k):
                if i == k-1:
                    t = pp
                if pp:
                    pp = pp.next 
                else:
                    return p0.next
            new_head,new_tail = self.reverse_part(h,t)
            pre.next = new_head
            new_tail.next = pp
            pre = new_tail
            print("查看转换：",pre.val,new_head.val,new_tail.val,new_tail.next)
            print("中途print:",p0.next)
        return p0.next

            
    
    def reverse_part(self,head:ListNode | None,tail:ListNode | None)-> tuple[ListNode | None,ListNode | None]:
        print("进入节点：",head.val,tail.val)
        p = head
        stop = tail.next
        pre,current = head,head.next
        while current !=stop:
            print(f"当前current：{current.val},{tail.val}")
            _ = current.next
            current.next= pre
            pre,current = current,_

        return pre,p
    

def list_to_listnode(list:list[int]) -> ListNode:
    p = p0 = ListNode()
    for i in list:
        p0.next = ListNode(i)
        p0 = p0.next
    return p.next


s = Solution()

# head = [1,2,3,4,5]; k = 2;
head = [1,2,3,4,5]; k = 3;
head = [1,2,3,4,5,6];k=3;
head = list_to_listnode(head)
print(head)
print(s.reverseKGroup(head=head,k=k))