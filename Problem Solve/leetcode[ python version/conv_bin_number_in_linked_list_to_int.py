class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # I see what to do here, we gotta convert it the linked list into a string
        # join them and then return it in base 2 int(num, 2)
        # First we convert linked list into list
        curr = head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        # Use the string to .join(str(i) for i in list)
        conv = "".join(str(i) for i in result)
        return int(conv, 2)
            
