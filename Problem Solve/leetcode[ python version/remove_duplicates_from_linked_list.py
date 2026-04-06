# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We'd want to convert it to a set and then the final result should be a ListNode
        set_head = set()
        current = head
        while current:
            set_head.add(current.val)
            current = current.next
        # Now we have to convert it back to a ListNode
        node_of_set = ListNode(0)
        
        current = node_of_set
        for val in sorted(set_head):
            current.next = ListNode(val)
            current = current.next
        return node_of_set.next