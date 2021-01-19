#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Function that inserts a number into a sorted singly linked list
 *
 * Return: The address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t));
    listint_t *tmp = *head;

    if (new == NULL)
        return (NULL);
    
    new->n = number;
    new->next = NULL;

    if (*head == NULL)
    {
        new = add_nodeint_end(head, number);
        return (new);
    }

    if (new == NULL)
    {
        return (NULL);
    }
    if (tmp->n >= number)
    {
        new->next = *head;
        *head = new;
        return (new);
    }
    while (tmp->next != NULL)
    {
        if (tmp->next->n >= number)
        {
            new->next = tmp->next;
            tmp->next = new;
            return (new);
        }
        tmp = tmp->next;
    }

    return (NULL);
}
