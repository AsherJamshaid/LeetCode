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
    void inorder(TreeNode*root,vector<int>&temp){
        if(root==nullptr){
            return;
        }
        inorder(root->left,temp);
        temp.push_back(root->val);
        inorder(root->right,temp);
    }
    vector<int> findMode(TreeNode* root) {
        vector<int>temp;
        vector<int>res;
        inorder(root,temp);
        int count=0;
        int mfreq = 0;
        unordered_map<int,int>m;
        for(int x:temp){
            m[x]++;
        }
        for(auto x:m){
            mfreq=max(mfreq,x.second);
        }
        for(auto x:m){
            if(x.second == mfreq){
                res.push_back(x.first);
            }
        }
        return res;
    }
};
