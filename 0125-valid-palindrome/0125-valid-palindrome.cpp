class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> arr;

        bool res = true;
        for (int i = 0; i < s.size(); i++){
            if (isalnum(s[i])){
                arr.push_back(tolower(s[i]));
            }
        }
        vector<char> rarr;

        for(int i = (arr.size() - 1); i >= 0; i--){
            rarr.push_back(arr[i]);
        }
        return rarr == arr;
        
    }
};