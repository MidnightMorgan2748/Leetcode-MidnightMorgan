from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        levels = self.n.bit_length() + 1
        # st[i][j] := max(nums[j..j + 2^i - 1])
        self.st = [[0] * (self.n + 1) for _ in range(levels)]
        for idx, val in enumerate(nums):
            self.st[0][idx] = val

        for i in range(1, self.n.bit_length() + 1):
            half = 1 << (i - 1)
            span = 1 << i
            for j in range(0, self.n - span + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + half])
    def query(self, l: int, r: int) -> int:
        """Returns max(nums[l..r])."""
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])
class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        ones = s.count('1')
        zero_groups, zero_group_index = self._get_zero_groups(s)
        if not zero_groups:
            return [ones] * len(queries)
        st = SparseTable(self._get_adjacent_group_length_sums(zero_groups))
        ans = []
        for l, r in queries:
            gl = zero_group_index[l]
            gr = zero_group_index[r]
            left = -1 if gl == -1 else (
                zero_groups[gl].length - (l - zero_groups[gl].start)
            )
            right = -1 if gr == -1 else (r - zero_groups[gr].start + 1)
            end_group_for_r = gr if s[r] == '1' else gr - 1
            start_adj, end_adj = self._map_to_adjacent_group_indices(
                gl + 1, end_group_for_r
            )
            active_sections = ones
            if s[l] == '0' and s[r] == '0' and gl + 1 == gr:
                active_sections = max(active_sections, ones + left + right)
            elif start_adj <= end_adj:
                active_sections = max(
                    active_sections, ones + st.query(start_adj, end_adj)
                )
            if s[l] == '0' and gl + 1 <= end_group_for_r:
                active_sections = max(
                    active_sections, ones + left + zero_groups[gl + 1].length
                )
            if s[r] == '0' and gl < gr - 1:
                active_sections = max(
                    active_sections, ones + right + zero_groups[gr - 1].length
                )
            ans.append(active_sections)
        return ans
    def _get_zero_groups(self, s: str) -> Tuple[List[Group], List[int]]:
        zero_groups: List[Group] = []
        zero_group_index: List[int] = []
        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(Group(start=i, length=1))
            zero_group_index.append(len(zero_groups) - 1)
        return zero_groups, zero_group_index
    def _get_adjacent_group_length_sums(
        self, zero_groups: List[Group]
    ) -> List[int]:
        return [
            zero_groups[i].length + zero_groups[i + 1].length
            for i in range(len(zero_groups) - 1)
        ]
    def _map_to_adjacent_group_indices(
        self, start_group_index: int, end_group_index: int
    ) -> Tuple[int, int]:
        return start_group_index, end_group_index - 1