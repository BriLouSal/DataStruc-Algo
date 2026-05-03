class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # So what we know is that we can use Area to find width and length
        # Question is how? we know width cannot be larger length
        # and we have to return it as L, and Width...
        # and it has to be at the smallest, so we can do is sqr root and int
        # and then do floor division, we can reverse engineer
        # the output from the examples, so we know that area = 37
        # and we know that 37 is not a squared number, so a way that this is possible
        # is that we can do let that be -1 so per step we decrease by 1 and if the w
        # is divisible by the area, we can get the length and width so area // w, w

        sqr_area = int(sqrt(area))
        for w in range(sqr_area, 0, -1):
            if area % w == 0:
                return [area // w, w]
