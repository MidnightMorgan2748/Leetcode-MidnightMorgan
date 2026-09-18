class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        vector<int> arr;
        unordered_map<int, int> mp;

        for (int i : nums){
            mp[i]++;
            if (mp[i] > 1){
                return true;
            }
        }
        return false;
    }
};