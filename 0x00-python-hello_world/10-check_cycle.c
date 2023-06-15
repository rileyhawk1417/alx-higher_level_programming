#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Entry point
 * @list: listint_t value
 * Return: int value
 * Description: Returns 0 if no cycle is found
 * returns 1 if cycle is found within list
*/
int check_cycle(listint_t *list)
{
listint_t *fasterNode = list;
listint_t *normalNode = list;
if (list == NULL)
	return (0);
while (normalNode != NULL && fasterNode->next)
{
normalNode = normalNode->next;
fasterNode = fasterNode->next->next;
if (normalNode == fasterNode)
	return (1);

}
return (0);
}
