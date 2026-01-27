class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        int size = nums.size();
        vector <int> result;
        for(int i = 0;i<size;i++){
            if(nums[i] % 2 == 0){
                result.insert(result.begin(),0);
            }
            else{
                result.insert(result.begin(),1);
            }
        }
        sort(result.begin(),result.end());
        return result;
    }
};
