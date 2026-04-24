# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We'd want to remove the nth term of the iteration of the linked list and keep the n+1
        # first we convert to list, and then we can do a slicing of the list, and 
        # then keep the right side after the indeces is removed and merge it with the left index
        if not head or not head.next:
            return None

        res = []
        v = head
        while v:
            res.append(v)
            v = v.next
        target_ind = len(res) - n
        res = res[:target_ind]  + res[target_ind +1:]
        # If empty after, such as that there's nothing left
        if not res:
            return None
        
        for i in range(len(res) - 1):
            res[i].next = res[i+1]
            
        res[-1].next = None
        
        return res[0]

         