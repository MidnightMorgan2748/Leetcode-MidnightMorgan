class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans1 = nums[n-1] - nums[2];
        int ans2 = nums[n-3] - nums[0];
        int ans3 = nums[n-2] - nums[1];
        int res = min({ans1, ans2, ans3});
        return res;
    }
};