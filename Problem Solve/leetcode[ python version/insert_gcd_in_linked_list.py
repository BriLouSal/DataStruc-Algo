import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        # We use the two iteration, and we append gcd(i, j) between the list 
        # so res[i:j] = res: Between every pair of adjacent nodes, 
        # insert a new node with a value equal to the greatest common divisor of them.
        # so between i and i+1(j)
        i = 0
        while len(res) - 1 > i:
            j = i+1
            gcd_val = math.gcd(res[i], res[j])
            res[j:j] = [gcd_val]
            i+=2
        new_head = ListNode(res[0])
        curr = new_head
        for i in res[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return new_head
        