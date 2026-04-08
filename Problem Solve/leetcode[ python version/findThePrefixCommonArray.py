class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # We can just do a set intersection and sort it!
        freq = [0] * (len(A)+1)
        C = []
        cout = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                cout += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                cout += 1
            C.append(cout)
        return C