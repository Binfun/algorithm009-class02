class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0
        for i in t:
            if i in d:
                if d[i] != 0:
                    d[i] -= 1
                else:
                    del[d[i]]
            else:
                return False
        if d:
            return False
        else:
            return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 定义默认布尔值参与后续运算
        result = True
        # 利用 Python 数据结构 set 去重去序
        set_tmp = set(s)
        # 先判断组成字符串的各个字符元素是否一致
        if set_tmp == set(t):
            for i in set_tmp:
                # 利用逻辑运算符判断各个字符元素的数量一致，均为 True 才输出 True
                result = result and (s.count(i) == t.count(i))
        else:
            result = False
        return (result)

