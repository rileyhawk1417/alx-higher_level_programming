#include "lists.h"
#include <stdio.h>


/**
 * reverse_list: Entry point
 * @head: The start of the link list
 * Return: NULL
 * Description: Reverse the list
 */
void reverse_list(listint_t **head)
{
listint_t *previousNode = NULL;
listint_t *currentNode = *head;
listint_t *nextNode = NULL;

while (currentNode)
{
nextNode = currentNode->next;
currentNode->next = previousNode;
currentNode = nextNode;
}

*head = previousNode;
}

/**
 * is_palindrome: Entry point
 * @head: The start of the link list
 * Return: int value
 * Description: Check if list is palindrome
 * then return 0 if not. Then return 1 if it is
 */
int is_palindrome(listint_t **head){
listint_t *fastNode = *head;
listint_t *slowNode = *head;
listint_t *tmpNode = *head;
listint_t *duplicateNode = NULL;

if (*head == NULL || (*head)->next == NULL)
	return (1);

while (1)
{
	fastNode = fastNode->next->next;
	if (!fastNode)
	{
		duplicateNode = slowNode->next;
		break;
	}

	if (!fastNode->next)
	{
		duplicateNode = slowNode->next->next;
		break;
	}

slowNode = slowNode->next;
}

reverse_list(&duplicateNode);

while (duplicateNode && tmpNode)
{
	if (tmpNode->n == duplicateNode->n)
	{
		duplicateNode = duplicateNode->next;
		tmpNode = tmpNode->next;
	}
	else
		return (0);
}

if (!duplicateNode)
	return (1);

return (0); 
}
