class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        long long i=0,temp=capacity,ans=0;
        while(i!=plants.size()){
            if(capacity>=plants[i]){
                capacity-=plants[i];
                i+=1;
                ans+=1;
            }
            else{
                ans+=2*i;
                capacity = temp;
            }
        }
        return ans;
    }
};
