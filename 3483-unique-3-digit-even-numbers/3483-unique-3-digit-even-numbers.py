class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        return len({int("".join(map(str, p))) for p in permutations(digits, 3) if p[0] != 0 and int("".join(map(str, p))) % 2 == 0})