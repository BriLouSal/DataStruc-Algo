# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # So we'd want to do is convert the linked_list as a list first
        # and then we'd probably want to manipulate the list via reversal
        # so we create a new array based arr = result[-k:] + result[:-k]

        # ALSO TO FIX THE division by error problem in my solution we need to handle the case
        # if head is None or k is 0

        if not head or not head.next:
            return head


            
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next




        if k >= len(result):
            k = k % len(result)
        new_res = result[-k:] + result[:-k]
        if k == 0:
            return head


        new_head = ListNode(new_res[0])
        curr = new_head
        for i in range(1, len(new_res)):
            curr.next = ListNode(new_res[i])
            curr = curr.next
            
        return new_head