class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int size = nums.size();
        
        sort(nums.begin(),nums.end());
        bool flag = false;
        for(int i = 0 ;i < size;i++){
            if(i == size-1){
                break;
            }
            else if(nums[i] == nums[i+1]){
                 flag = true;
                 break;
           }
        }
        if(flag == true){
            return true;
        }
        else{
            return false;
        }
}


};
