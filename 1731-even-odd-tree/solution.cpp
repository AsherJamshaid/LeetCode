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
    bool isEvenOddTree(TreeNode* root) {
        if(root==nullptr){
            return true;
        }
        queue<TreeNode*>q;
        q.push(root);
        int level=0;
        while(!q.empty()){
            int n=q.size();
            vector<int>temp;
            for(int i=0;i<n;i++){
                TreeNode*node = q.front();
                q.pop();
                if(level%2==0){
                    if(node->val%2==0){
                        return false;
                    }
                    temp.push_back(node->val);
                }
                else{
                    if(node->val%2!=0){
                        return false;
                    }
                    temp.push_back(node->val);
                }
                if(node->left!=nullptr){
                    q.push(node->left);
                }
                if(node->right!=nullptr){
                    q.push(node->right);
                }
            }
            if(level%2==0){
                if(!is_sorted(temp.begin(),temp.end(),less_equal<int>())){
                    return false;
                }
            }
            else if(level%2!=0){
                if(!is_sorted(temp.begin(),temp.end(),greater_equal<int>())){
                    return false;
                }
            }
            level++;
        }
        return true;
    }
};
