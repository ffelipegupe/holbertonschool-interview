#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_node - function that creates a binary tree node
 * @parent: pointer to the parent node
 * @value: value of the new node
 * 
 * Return: The address of the new node, or NULL if it failed
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
    binary_tree_t *new = malloc(sizeof(binary_tree_t));
    if (new == NULL)
        return (NULL);
    
    if (parent == NULL)
    {
        new->n = value;
        new->parent = NULL;
        new->left = new->right = NULL;
        return (new);
    }
    else
    {
        new->parent = parent;
        new->n = value;
        new->left = new->right = NULL;
        return (new);
    }
    
    return (NULL);
}
