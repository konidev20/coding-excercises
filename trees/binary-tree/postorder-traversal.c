// https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct node
{

    int data;
    struct node *left;
    struct node *right;
};

void postOrder(struct node *root)
{
    if (root != NULL)
    {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}