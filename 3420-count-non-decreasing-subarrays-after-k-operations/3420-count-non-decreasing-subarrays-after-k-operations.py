class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        ans = 0
        cost = 0
        dq = deque()
        j = n - 1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            cnt = 1
            while dq and dq[-1][0] < num:
                v, c = dq.pop()
                cnt += c
                cost += (num - v) * c
            dq.append([num, cnt])
            while cost > k:
                dq[0][1] -= 1
                cost -= dq[0][0] - nums[j]
                j -= 1
                if dq[0][1] == 0:
                    dq.popleft()
            ans += j - i + 1
        return ans