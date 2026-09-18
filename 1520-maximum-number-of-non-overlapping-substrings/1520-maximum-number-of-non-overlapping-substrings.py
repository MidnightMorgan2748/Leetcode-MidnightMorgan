class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        intervals = []
        for i in range(n):
            if first[s[i]] != i:
                continue
            start, end = i, last[s[i]]
            j = start
            valid = True
            while j <= end:
                c = s[j]
                if first[c] < start:
                    valid = False
                    break
                end = max(end, last[c])
                j += 1
            if valid:
                intervals.append((start, end))
        intervals.sort(key = lambda x: x[1])
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        return res
