class Solution:
    def checkValidString(self, s: str) -> bool:
        a = 0
        b = 0
        for i in s:
            if i == '(':
                a += 1
                b += 1
            elif i == ')':
                a -= 1
                b -= 1
            else:
                a -= 1
                b += 1
            
            if a < 0:
                a = 0
            if b < 0:
                return False
        return a == 0