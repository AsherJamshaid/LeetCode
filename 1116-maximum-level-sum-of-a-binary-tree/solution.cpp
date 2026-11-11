/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if(root==nullptr){
            return 0;
        }
        int ans =0,sum=0;
        int max = INT_MIN;
        int level=1;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            int n=q.size();
            sum=0;
            for(int i=0;i<n;i++){
                TreeNode*node = q.front();
                q.pop();
                sum+=node->val;
        
                if(node->left !=nullptr)
                    q.push(node->left);
                if(node->right !=nullptr)
                    q.push(node->right);
            }
            if(sum>max){
                max=sum;
                ans = level;
            }
            level++;
            }
        return ans;   
    }
};
