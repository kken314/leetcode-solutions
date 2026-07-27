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
    int maxDepth(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }

        int maxDepthLeft = maxDepth(node->left);
        int maxDepthRight = maxDepth(node->right);

        int currDiameter = maxDepthLeft + maxDepthRight;
        maxDiameter = max(maxDiameter, currDiameter);

        return 1 + max(maxDepthLeft, maxDepthRight);
    }

public:
    int maxDiameter = 0;
    int diameterOfBinaryTree(TreeNode* root) {

        maxDepth(root);

        return maxDiameter;
    }
};