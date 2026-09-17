/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    void PreOrder(TreeNode* node, vector<string>& vec) {
        if (node == nullptr) 
        {
            vec.push_back("null");
            return;
        }
        
        vec.push_back(to_string(node->val));
        PreOrder(node->left, vec);
        PreOrder(node->right, vec);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<string> vecofp;
        vector<string> vecofq;
        PreOrder(p, vecofp);
        PreOrder(q, vecofq);
        return vecofp==vecofq;
    }
};
