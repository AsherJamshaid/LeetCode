class Solution {
public:
    int minimumChairs(string s) {
        int total = 0;
        int ans = -1;

        for(int i = 0 ;i < s.length();i++){
            if(s[i] == 'E'){
                total++;
            }
            else{
                total-=1;
            }
            if(total > ans){
                ans = total;
            }
        }
        return ans;
    }
};
