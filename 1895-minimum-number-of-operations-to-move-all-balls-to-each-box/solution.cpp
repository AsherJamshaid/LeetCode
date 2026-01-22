class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> answer(n, 0);
        vector<int> boxesInt(n, 0);

        for(int i = 0; i < n; i++)
            boxesInt[i] = (boxes[i] == '1' ? 1 : 0);

        // Left to Right
        int ballsLeft = 0, opsLeft = 0;
        for(int i = 0; i < n; i++){
            answer[i] += opsLeft;
            if(boxesInt[i] == 1) ballsLeft++;
            opsLeft += ballsLeft;
        }

        // Right to Left
        int ballsRight = 0, opsRight = 0;
        for(int i = n-1; i >= 0; i--){
            answer[i] += opsRight;
            if(boxesInt[i] == 1) ballsRight++;
            opsRight += ballsRight;
        }

        return answer;
    }
};

