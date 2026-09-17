class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] *n
        left = 0
        curr_sum = 0
        best_at_left = float('inf')
        result = float('inf')

        for right in range(n):
            curr_sum  += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == target:
                curr_length = right - left + 1
                if left  > 0 and min_len[left - 1] != float('inf'):
                    result = min(result, curr_length + min_len[left -1])
                best_at_left = min(best_at_left, curr_length)
            min_len[right] = best_at_left
        return result if result != float('inf') else -1