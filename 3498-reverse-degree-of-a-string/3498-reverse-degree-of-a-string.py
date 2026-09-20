class Solution:
    def reverseDegree(self, s: str) -> int:
        lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        mp = {}
        p = 26
        for i in lis:
            mp[i] = p
            p -= 1
        res = 0
        for i in range(len(s)):
            val = (i+1) * mp[s[i]]
            res += val
        return res