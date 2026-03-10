class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_list = list(address)

        for i in range(len(new_list)):
            if new_list[i] == ".":
                new_list[i] = '[.]'
        
        return "".join(new_list)