#include <stdlib.h>
#include "binary_trees.h"

/**
 * heap_insert - function that creates a binary tree node
 * @root: double pointer to the root node of the Heap
 * @value: value to store in the node to be inserted
 *
 * Return: The address of the inserted node, or NULL on failure
 */
heap_t *heap_insert(heap_t **root, int value)
{

	if (*root == NULL)
	{
		*root = binary_tree_node(*root, value);
		return (*root);
	}
	else
	{
		return (NULL);
	}
	return (NULL);
}
