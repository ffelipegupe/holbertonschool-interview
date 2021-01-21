#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head to the list
 *
 * Return: 0, if not palindrome; 1, if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int len = 0, buff[5400], is = 1;
	int i;

	if (!*head || !((*head)->next))
		return (1);

	for (i = 0; tmp; i++)
	{
		buff[i] = tmp->n;
		tmp = tmp->next;
	}

	for (len = 1, i = 0; i < len; i++)
	{
		if (buff[i] != buff[len - 1 - i])
		{
			is = 0;
			break;
		}
	}
	return (is);
}
