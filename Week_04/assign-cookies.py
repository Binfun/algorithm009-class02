class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi, si, kids = 0, 0, 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                kids += 1
                si += 1
                gi += 1
            else:
                si += 1
        return kids
