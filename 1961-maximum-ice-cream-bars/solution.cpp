
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int ans = 0;
        int i = 0;

        sort(costs.begin(), costs.end());

        while (i < costs.size() && coins >= costs[i]) {
            coins -= costs[i];
            i++;
            ans++;
        }

        return ans;
    }
};
