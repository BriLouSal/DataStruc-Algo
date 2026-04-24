# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # First convert the linked list into a an array
        # We know we have to return it as sorted 
        result = []

        #  ALSO! the lists is a outer_list

        for i in lists:
            current = i
            while current:
                result.append(current.val)
                current = current.next
        result.sort()
        # Now we convert it back to a linked List
        if not result:
            return None
        # Set them as None in case we have empty linked list
        new_head = None
        curr = None
        for i in result:
            if new_head is None:
                new_head = ListNode(i)
                curr = new_head
            else:
                curr.next = ListNode(i)
                curr = curr.next
        return new_head

