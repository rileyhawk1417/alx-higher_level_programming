#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode;
listint_t *currentNode = *head;
newNode = malloc(sizeof(listint_t));

if (!newNode)
	return (NULL);
while (currentNode && currentNode->next && currentNode->next->n < number)
	currentNode = currentNode->next;

newNode->n = number;
newNode->next = currentNode->next;
currentNode->next = newNode;

return (newNode);
}
