class Solution {
public:
    int minInsertions(string s) {
        int res = 0;
        int need = 0;
        for (char c : s){
            if (c == '('){
                if (need % 2 == 1){
                    res++;
                    need--;
                }
                need += 2;
            }
            else{
                need--;
                if (need < 0){
                    res++;
                    need += 2;
                }
            }
        }
        return res + need;

    }
};