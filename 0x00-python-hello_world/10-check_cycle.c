#include "lists.h"
/**
 * check_cycle - check whether a cycle exist in a linked list
 * @list: the head of the linked list
 *
 * Return: 1 if there is a cycle 0 otherwise
 **/
int check_cycle(listint_t *list)
{
listint_t *fast = list, *slow = list;

if (list == NULL || list->next == NULL)
return (0);
while(fast && slow && fast->next)
{
fast = fast->next->next;
slow = slow->next;
if (fast == slow)
return (1);
}
return (0);
}
