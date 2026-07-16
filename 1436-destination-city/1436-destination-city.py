class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = []
        b = []
        for i in paths:
            a.append(i[0])
            b.append(i[1])
        c = set(a)
        d = set(b)
        e = list(d - c)
        return e[0]