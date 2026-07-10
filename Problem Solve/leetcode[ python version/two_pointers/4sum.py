class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Store combinations that lead to target.
        # We avoid pure backtracking because choosing 4 numbers directly can lead to O(n^4).
        # This uses pair sums instead.

        nums.sort()

        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        unique_nums = sorted(freq.keys())
        res = set()
        pair_sums = {}
        pair_seen = {}
        n = len(unique_nums)
        for i in range(n):
            for j in range(i, n):
                a = unique_nums[i]
                b = unique_nums[j]
                if a == b and freq[a] < 2:
                    continue
                pair_sum = a + b
                if pair_sum not in pair_sums:
                    pair_sums[pair_sum] = []

                pair_sums[pair_sum].append((a, b))

        for curr in pair_sums:
            comp = target - curr
            if comp not in pair_sums:
                continue
            for i, j in pair_sums[curr]:
                for k, l in pair_sums[comp]:
                    res_qu = [i,j,k,l]
                    res_qu.sort()
                    used = {}
                    valid = True
                    for x in res_qu:
                        used[x] = used.get(x, 0) + 1
                        if used[x] > freq[x]:
                            valid = False
                            break
                    if valid:
                        res.add(tuple(res_qu))

        return [list(x) for x in res]