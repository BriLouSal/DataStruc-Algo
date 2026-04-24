# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # What we know, we should clearly make a new list and convert them back to Listnode
        # and that new list checks if that head is less than the x, we pass that via continue
        # Consider no head, then return head
        if not head or not head.next:
            return head
        # We want to create like a list that filters 
        # out if the Node is smaller or larger than 3

        res = []
        less = []
        vals = head
        while vals:
            if vals.val < x:
                less.append(vals.val)
                vals = vals.next
            else:
                res.append(vals.val)
                vals = vals.next
        #  preserve the original relative order of the nodes in each of the two partitions.
        # SO DO NOT SoRT THE LIST
        new_res = less + res
        
        new_head = ListNode(new_res[0])
        curr = new_head
        for i in range(1, len(new_res)):
            curr.next = ListNode(new_res[i])
            curr = curr.next
            
        return new_head
        

    