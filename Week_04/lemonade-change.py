
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            elif i == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                five += 1
        return True
