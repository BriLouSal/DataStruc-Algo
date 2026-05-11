class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # So we have to return a nested list, all right we can do that
        # I purpose that we should do is that we can do *matrix and zip it
        # We can do this in 5 lines or less haha
        return [list(x) for x in zip(*matrix)]