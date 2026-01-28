class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int size = nums.size();
        int max = 0;
        sort(nums.begin(),nums.end());
        for(int i = 0;i<size;i++){
            int count = 1;
            for(int j = i+1;j<size;j++){
                if(nums[i] == nums[j]){
                    count+=1;
                }
            }
            if (count > (size/2)){
                max = nums[i];
            }
        }
        return max;
    }
};
