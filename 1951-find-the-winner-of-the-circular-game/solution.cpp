class Solution {
public:
    int findTheWinner(int n, int k) {
        queue<int> circle;
        for(int i = 1;i<=n;i++){
            circle.push(i);
        }
        while (circle.size() > 1) {
        for (int i = 1; i < k; i++) {
            int front = circle.front();
            circle.pop();
            circle.push(front);
        }
        circle.pop();
        }

    return circle.front();
    }
};
