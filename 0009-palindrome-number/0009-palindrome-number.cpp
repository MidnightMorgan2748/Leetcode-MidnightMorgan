class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        vector<char> arr;

        for (int i = 0; i < s.size(); i++){
            arr.push_back(s[i]);
        }
        vector<char> rarr;

        for (int i = (s.size() - 1); i >= 0; i--){
            rarr.push_back(arr[i]);
        }

        return rarr == arr;


        
    }
};