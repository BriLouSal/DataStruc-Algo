class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_arr = [x for x in nums if x % 2 == 0]
        odd_arr =  [x for x in nums if (x % 2) != 0]

        ans = [0] * len(nums)
        for i in range(len(ans)):
            if i % 2 == 0:
                ans[i] = even_arr[i//2]
            else:
                ans[i] = odd_arr[i // 2]
        return ans