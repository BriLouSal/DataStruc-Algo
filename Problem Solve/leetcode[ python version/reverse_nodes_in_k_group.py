# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First we convert linked list into a list, and we have to compare k if it's
        # bigger than the val and then we append it into left

        r  = []
        v = head

        # If the number of 
        # nodes is not a multiple of k then left-out nodes

        while v:
            r.append(v.val)
            v = v.next
        
        rev_list  = []
        for i in range(0, len(r), k):
            res = r[i:i+k]
            if len(res) == k:
                rev_list.extend(res[::-1])
            #  in the end, should remain as it is.
            else:
                rev_list.extend(res)

    
        new_head = ListNode(rev_list[0])
        curr = new_head
        for i in range(1, len(rev_list)):
            curr.next = ListNode(rev_list[i])
            curr = curr.next
            
        return new_head
        