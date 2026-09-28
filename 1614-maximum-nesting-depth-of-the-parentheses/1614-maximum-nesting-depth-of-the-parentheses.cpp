class Solution {
public:
    int maxDepth(string s) {
        stack<char> suka;
        int res = 0;
        for (char c : s){
            if (c == '('){
                suka.push(c);
                res = max(res, (int)suka.size());
            } else if (c == ')'){
                suka.pop();
            }
        }
        return res;

    }
};