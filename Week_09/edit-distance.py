class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) == 0:
            return len(word1)
        elif len(word1) == 0:
            return len(word2)
        m = [ [0 for i in range(len(word2))] for j in range(len(word1))]
        p = 0
        for j in range(len(word2)): #初始化第0行
            if word1[0] == word2[j]:
                p = 1
            m[0][j] = j + 1 - p
        p = 0
        for i in range(0, len(word1)): #初始化第0列
            if word1[i] == word2[0]:
                p = 1
            m[i][0] = i + 1 - p

        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = min(m[i - 1][j - 1], m[i - 1][j], m[i][j - 1]) + 1
        return m[-1][-1]