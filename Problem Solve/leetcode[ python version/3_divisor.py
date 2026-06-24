class Solution:
    def isThree(self, n: int) -> bool:

        count = 0
        if n <= 1:
            count = n 

        for i in range(1, int(n ** 0.5)+1):
            if n % i == 0:
                if i * i == n:
                    count += 1
                else:
                    count += 2




        return count == 3