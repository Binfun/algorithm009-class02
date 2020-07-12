class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        t = [0] * 1001
        r = []
        for i in arr1: t[i] += 1
        for i in arr2:
            for j in range(0, t[i]):
                r.append(i)
            t[i] = 0
        for k in range(0, len(t)):
            for j in range(0, t[k]):
                r.append(k)
        return r