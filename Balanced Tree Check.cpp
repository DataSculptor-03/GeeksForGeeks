

/* A binary tree node structure

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

/*class Solution{
    public:
    //Function to check whether a binary tree is balanced or not.
    bool isBalanced(Node *root)
    {
        //  Your Code here
    }
};*/


class Solution{
    public:
    int height(Node* root){
        if(root==nullptr)
            return 0;
            
        return 1+max(height(root->left), height(root->right));
    }
    
    bool isBalanced(Node *root)
    {
        //  Your Code here
        if(root==nullptr)
            return true;
        if(abs(height(root->left)-height(root->right))>1)
            return false;
            
        return (isBalanced(root->left) && isBalanced(root->right));
    }
};
