/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    
     if((p==NULL&&q!=NULL)||(p!=NULL&&q==NULL))
        return 0;
     if(p==NULL&&q==NULL)
       return 1;
       int left=isSameTree(p->left,q->left);
       int right=isSameTree(p->right,q->right);
       if((left==right)&&(left==1))
          {
              if(p->val==q->val)
              return 1;
              else
              return 0;
              
          }
       else
          return 0;
    
    
    
    
}