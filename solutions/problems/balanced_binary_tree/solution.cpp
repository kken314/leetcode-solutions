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
private:
int DFS(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        int maxDepthLeft = DFS(node->left);
        int maxDepthRight = DFS(node->right);
        int diffDepth = abs(maxDepthRight - maxDepthLeft);

        if (maxDepthLeft == -1 || maxDepthRight == -1 || diffDepth > 1) {
            return -1;
        } 

        return 1 + max(maxDepthLeft, maxDepthRight);
    }
    
public:
    bool isBalanced(TreeNode* root) {
        return DFS(root) != -1;
    }
};