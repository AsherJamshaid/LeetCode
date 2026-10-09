class Solution {
    void flip(vector<int>& A, int idx) {
        for(int i = 0; i <= idx/2; ++i) {
            int temp  = A[i];
            A[i] = A[idx - i];
            A[idx - i] = temp;     
        }
    }

public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> result;

        for(int i = arr.size() - 1; i > 0; --i) {
            for(int j = 0; j <= i; ++j) {
                if(arr[j] == i + 1) {
                    if(j != 0) {              
                        flip(arr, j);
                        result.push_back(j + 1);
                    }
                    break;
                }
            }

            if(arr[i] == i + 1) continue;    

            flip(arr, i);
            result.push_back(i + 1);
        }

        return result;
    }
};
