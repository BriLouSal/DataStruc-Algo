# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # Ok so we can have a situation where we can just append the linked list into a list
        result = []
        # Current value
        current_val = head
        while current_val:
            result.append(current_val.val)
            current_val = current_val.next
        
        result.reverse()
        
        new_head = ListNode(result[0])
        curr = new_head
        for i in range(1, len(result)):
            curr.next = ListNode(result[i])
            curr = curr.next
            
        return new_head