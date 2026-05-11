# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        # So we're swapping nodes...
        for i in range(0, len(result) - 1, 2):
            result[i], result[i+1] = result[i+1],result[i]

        dummy = ListNode(0)
        curr = dummy
        for val in result:
            curr.next = ListNode(val)
            curr = curr.next     
        return dummy.next