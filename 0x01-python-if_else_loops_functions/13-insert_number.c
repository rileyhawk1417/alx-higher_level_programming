#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Entry point
 * @head: The head of the node
 * @number: int value
 * Return: Return the address of the newly added node
 * Description: The function adds a number in the list.
 * The number is added into the list in ascending order
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode;
listint_t *currentNode = *head;
newNode = malloc(sizeof(listint_t));

if (!newNode)
	return (NULL);

newNode->n = number;
/*NOTE:If number is negative & less than the current number */
if (currentNode == NULL || currentNode->n >= number)
{
newNode->next = currentNode;
*head = newNode;
return (newNode);
}

/*NOTE:If the number is less than current number but not negative */
while (currentNode && currentNode->next && currentNode->next->n < number)
	currentNode = currentNode->next;

newNode->next = currentNode->next;
currentNode->next = newNode;

return (newNode);
}
