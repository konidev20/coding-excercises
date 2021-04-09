// https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

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

void preOrder(struct node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}