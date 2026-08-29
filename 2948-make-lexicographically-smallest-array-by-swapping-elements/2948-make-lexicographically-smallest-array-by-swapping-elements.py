class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        groups = []
        current_group = [indexed_nums[0]]
        
        for i in range(1, n):
            if indexed_nums[i][0] - indexed_nums[i - 1][0] <= limit:
                current_group.append(indexed_nums[i])
            else:
                groups.append(current_group)
                current_group = [indexed_nums[i]]
        groups.append(current_group)
        
        ans = [0] * n
        for group in groups:
            indices = sorted(item[1] for item in group)
            for idx, item in zip(indices, group):
                ans[idx] = item[0]
                
        return ans