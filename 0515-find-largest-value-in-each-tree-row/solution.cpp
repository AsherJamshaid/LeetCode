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
    vector<int> largestValues(TreeNode* root) {
        if(root==nullptr){
            return {};
        }
        vector<int>res;
        queue<TreeNode*>q;
        q.push(root);
        int max = INT_MIN;
        while(!q.empty()){
            int n=q.size();
            max = INT_MIN;
            for(int i=0;i<n;i++){
                TreeNode*node = q.front();
                q.pop();
                if(node->val > max){
                    max = node->val;
                }
                if(node->left !=nullptr)
                    q.push(node->left);
                if(node->right !=nullptr)
                    q.push(node->right);
            }
            res.push_back(max);
        }
        return res;
    }
};
