class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if (tokens.size() == 1){
            return stoi(tokens[0]);
        }
        stack<int> st;
        int ans = 0;
        for(int i = 0;i<tokens.size();i++){
            if (tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/"){
                int num1 = st.top();
                st.pop();
                int num2 = st.top();
                st.pop();
                if (tokens[i] == "+"){
                    ans = num2 + num1;
                }
                else if(tokens[i] == "-"){
                    ans = num2-num1;
                }
                else if(tokens[i] == "/"){
                    ans = num2 / num1;
                }
                else{
                    ans = num2 * num1;
                }
                st.push(ans);
            }
            
            else
                st.push(stoi(tokens[i]));
            
        }
        return ans;
    }
};
