# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # So we wanna merge them together,  via list1_conv_list + list2_conv_list and then return back to 
        # a linked list
        if not list1 and not list2:
            return None
        curr = list1
        var_1 = []
        while curr: 
            var_1.append(curr.val)
            curr = curr.next

        curr = list2
        var_2 = []
        while curr:
            var_2.append(curr.val)
            curr = curr.next

        # Convet it from a list to a linked list, we can just do a sorted of the two lists and then convert it back to a linked list

        new_list = sorted(var_1 + var_2)
        new_head = ListNode(new_list[0])
        current = new_head
        
        for i in range(1, len(new_list)):
            current.next = ListNode(new_list[i])
            current = current.next
            
        return new_head


        