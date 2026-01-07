class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # First grab the accounts and return a sum of it via list comphrension
        new_list = [sum(x) for x in accounts]
        new_list.sort(reverse=True)
        return new_list[0]
        