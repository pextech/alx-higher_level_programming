#include "lists.h"
/**
 * insert_node - function to insert a new node
 * @head: the head of the node
 * @number: the given value
 *
 * Return: the address of the new node
 **/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newnode = NULL, *cur = *head;

newnode = malloc(sizeof(listint_t));
if (newnode == NULL)
return (NULL);
newnode->n = number;
if (cur == NULL || cur->n >= number)
{
newnode->next = cur;
*head = newnode;
return (newnode);
}
while (cur && cur->next && cur->next->n < number)
cur = cur->next;
newnode->next = cur->next;
cur->next = newnode;
return (newnode);
}
