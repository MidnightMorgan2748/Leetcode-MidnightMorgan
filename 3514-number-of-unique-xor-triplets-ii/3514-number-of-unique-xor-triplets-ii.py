class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        pair_counts = {}
        for j in range(n):
            val_j = nums[j]
            for k in range(j, n):
                p_xor = val_j ^ nums[k]
                pair_counts[p_xor] = pair_counts.get(p_xor, 0) + 1
        unique_results = set()
        for x in nums:
            for p_xor in pair_counts:
                unique_results.add(x ^ p_xor)
                
        return len(unique_results)
