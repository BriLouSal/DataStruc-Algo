
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # We can use backtracking for this endeavour, as we want to grab the unique
        # permutations, so I purpose that we use the backtracking algo to grab those unique
        # combination
        nums = list(range(1, n+1))

        visited =  [False] * len(nums)

        self.count = 0
        self.result = ""

        def backtracking(current_path):
            if self.result:
                return
            if len(current_path) == n:
                self.count += 1
                if self.count == k:
                    self.result = "".join(map(str, current_path))
                return
            for i in range(n):
                if visited[i]: 
                    continue
                visited[i] = True
                current_path.append(nums[i])
                backtracking(current_path)
        
                current_path.pop()
                visited[i] = False

        backtracking([])

        return self.result 