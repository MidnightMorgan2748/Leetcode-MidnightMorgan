class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def a(cur, b, c):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return
            if b < n:
                cur.append('(')
                a(cur, b +1, c)
                cur.pop()
            if c < b:
                cur.append(')')
                a(cur, b, c + 1)
                cur.pop()
        a([], 0, 0)
        return res