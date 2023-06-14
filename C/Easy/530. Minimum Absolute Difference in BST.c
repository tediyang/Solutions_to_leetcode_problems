/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define min(a, b) (((a) < (b)) ? (a) : (b))
#define abs(a) (((a) < 0) ? (-a) : (a))

int getMinimumDifference(struct TreeNode* root){
    int node_values[10]; /*this is not enough for the testcases */
    int i = 0;

    void node_value(struct TreeNode* node, int *i)
    {
        if (node == NULL)
            return;

        node_value(node->left, i);
        node_values[*i] = node->val;
        *i = *i + 1;
        node_value(node->right, i);
    }

    node_value(root, &i);

    int size = i + 1;

    int min_diff = 100000;
    for (int j = 1; j < size; j++)
    {
        min_diff = min(min_diff, abs(node_values[j] - node_values[j - 1]));
    }
    
    return min_diff;
}