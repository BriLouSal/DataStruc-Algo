class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # We can just do a convert of the list of each node, if we're just gonna merge it
        result_one = []
        result_two = []
        current_val = list1
        while current_val:
            result_one.append(current_val.val)
            current_val = current_val.next
        current_val = list2
        while current_val:
            result_two.append(current_val.val)
            current_val = current_val.next
        # Delete the list iteration from a to b, and replace it with result_two
        result_one[a:b+1] = result_two
        
        new_head = ListNode(result_one[0])
        curr = new_head
        for i in range(1, len(result_one)):
            curr.next = ListNode(result_one[i])
            curr = curr.next
            
        return new_head