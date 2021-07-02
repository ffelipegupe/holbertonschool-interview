#include "list.h"
/**
 * add_node_begin - add a new node to the beginning of a circular linked list
 * @list: the list to modify
 * @str: the string to copy into the new node
 *
 * Return: Address of the new node, or NULL on failure
 */
List *add_node_begin(List **list, char *str)
{
	List *last, *node = NULL;

	node = malloc(sizeof(List));

	if (node == NULL)
		return (NULL);
	node->str = strdup(str);
	if (!node->str)
	{
		free(node);
		return (NULL);
	}
	if (*list == NULL)
	{
		node->next = node->prev = node;
		*list = node;
		return (node);
	}
	last = (*list)->prev;
	node->next = (*list);
	node->prev = last;
	(*list)->prev = last->next = node;
	*list = node;

	return (node);
}
/**
 * add_node_end - Adds a new node to the end of a double circular linked list
 * @list: head
 * @str: String
 *
 * Return: Address of the new element, or NULL on failure
 */
List *add_node_end(List **list, char *str)
{
	List *last, *node = NULL;

	node = malloc(sizeof(List));

	if (node == NULL || str == NULL)
		return (NULL);

	node->str = strdup(str);
	if (!node->str)
	{
		free(node);
		return (NULL);
	}
	if (*list == NULL)
	{
		node->next = node->prev = node;
		*list = node;
		return (node);
	}
	last = (*list)->prev;
	last->next = node;
	node->next = *list;
	node->prev = last;
	(*list)->prev = node;

	return (node);
}
